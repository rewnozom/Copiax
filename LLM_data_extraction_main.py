#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LLM-baserad Produktinformationsextraktor

Huvudskript som binder ihop alla komponenter och ger användaren ett kommandoradsgränssnitt
för att styra systemet. Detta skript möjliggör:

1. Extrahering av kompatibilitetsinformation och tekniska specifikationer från produktdokumentation
2. Bearbetning av enskilda produkter, hela kataloger eller produktlistor i CSV-filer
3. Parallell bearbetning med konfigurerbart antal arbetartrådar
4. Real-tidsvisualisering av framsteg och resultat
5. Detaljerade loggningsalternativ
6. Rapportgenerering och analys

Användning:
    python main.py [kommando] [alternativ]

Kommandon:
    process-product       Bearbeta en enskild produkt
    process-directory     Bearbeta alla produkter i en katalog
    process-csv           Bearbeta produkter listade i en CSV-fil
    start-workflow        Starta arbetsflödeshanteraren i kontinuerligt läge
    create-config         Skapa en standardkonfigurationsfil
    validate-config       Validera en konfigurationsfil
    test-connection       Testa anslutning till LLM-tjänsten
    generate-faq-answer   Generera svar på vanliga frågor baserat på extraherad information
"""

import os
import sys
import argparse
import logging
import json
import time
import datetime
import signal
import random
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Importera paket innan våra egna moduler för att undvika importfel
try:
    import yaml
    import colorama
    colorama.init()  # Initiera färgstöd för Windows
except ImportError:
    pass

# Importera våra moduler
from config import ConfigManager
from visualisering import setup_logger, LogCategory
from client import LLMClient
from Processor.ProductProcessor import ProductProcessor
from workflow.Arbetsflödeshantering import ProcessingQueue, JobPriority
from workflow.Arbetsflödeshantering import Worker
from workflow.Arbetsflödeshantering import BatchProcessor
from workflow.Arbetsflödeshantering import WorkflowManager, JobScheduler


def setup_argparse() -> argparse.ArgumentParser:
    """
    Konfigurerar kommandoradsargument
    
    Returns:
        argparse.ArgumentParser: Konfigurerad argumenttolkare
    """
    parser = argparse.ArgumentParser(
        description="LLM-baserad Produktinformationsextraktor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exempel:
  python main.py process-product --product-id "assa310-50" --file-path data/assa310-50.md
  python main.py process-directory --directory data/products --pattern "*.md" --batch-size 10
  python main.py process-csv --csv-file product_list.csv --id-column product_id --path-column file_path
  python main.py start-workflow --config config.yaml
  python main.py generate-faq-answer --product-id "assa310-50" --question "Vilka trycken passar till Assa 310-50?"
        """
    )
    
    # Skapa subparser för olika kommandon
    subparsers = parser.add_subparsers(dest="command", help="Kommando att utföra")
    
    # Allmänna alternativ
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--config", type=str, help="Sökväg till konfigurationsfil")
    parent_parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], 
                            default="INFO", help="Loggnivå")
    parent_parser.add_argument("--log-file", type=str, help="Sökväg till loggfil")
    parent_parser.add_argument("--output-dir", type=str, help="Katalog att spara resultat i")
    parent_parser.add_argument("--verbose", action="store_true", help="Visa detaljerad information")
    parent_parser.add_argument("--no-color", action="store_true", help="Inaktivera färgkodad utskrift")
    
    # process-product
    parser_product = subparsers.add_parser("process-product", parents=[parent_parser], 
                                        help="Bearbeta en enskild produkt")
    parser_product.add_argument("--product-id", type=str, required=True, help="ID för produkten")
    parser_product.add_argument("--file-path", type=str, required=True, help="Sökväg till filen")
    parser_product.add_argument("--extract-compatibility", action="store_true", 
                              help="Extrahera kompatibilitetsinformation")
    parser_product.add_argument("--extract-technical", action="store_true", 
                              help="Extrahera tekniska specifikationer")
    parser_product.add_argument("--extract-faq", action="store_true", 
                              help="Extrahera FAQ-data")
    
    # process-directory
    parser_dir = subparsers.add_parser("process-directory", parents=[parent_parser], 
                                     help="Bearbeta alla produkter i en katalog")
    parser_dir.add_argument("--directory", type=str, required=True, help="Katalog att bearbeta")
    parser_dir.add_argument("--pattern", type=str, default="*.md", 
                          help="Filnamnsmönster att matcha (default: *.md)")
    parser_dir.add_argument("--batch-size", type=int, default=10, 
                          help="Antal produkter per batch (default: 10)")
    parser_dir.add_argument("--workers", type=int, default=4, 
                          help="Antal parallella arbetartrådar (default: 4)")
    parser_dir.add_argument("--priority", choices=["LOW", "NORMAL", "HIGH", "CRITICAL"], 
                         default="NORMAL", help="Prioritet för jobben (default: NORMAL)")
    parser_dir.add_argument("--recursive", action="store_true", 
                          help="Sök rekursivt i underkataloger")
    
    # process-csv
    parser_csv = subparsers.add_parser("process-csv", parents=[parent_parser], 
                                     help="Bearbeta produkter listade i en CSV-fil")
    parser_csv.add_argument("--csv-file", type=str, required=True, help="Sökväg till CSV-filen")
    parser_csv.add_argument("--id-column", type=str, required=True, 
                         help="Kolumnnamn för produkt-ID")
    parser_csv.add_argument("--path-column", type=str, required=True, 
                         help="Kolumnnamn för filsökväg")
    parser_csv.add_argument("--encoding", type=str, default="utf-8", 
                         help="Teckenkodning för CSV-filen (default: utf-8)")
    parser_csv.add_argument("--delimiter", type=str, default=",", 
                         help="Avgränsare för CSV-filen (default: ,)")
    parser_csv.add_argument("--batch-size", type=int, default=10, 
                          help="Antal produkter per batch (default: 10)")
    parser_csv.add_argument("--workers", type=int, default=4, 
                          help="Antal parallella arbetartrådar (default: 4)")
    parser_csv.add_argument("--priority", choices=["LOW", "NORMAL", "HIGH", "CRITICAL"], 
                         default="NORMAL", help="Prioritet för jobben (default: NORMAL)")
    
    # start-workflow
    parser_workflow = subparsers.add_parser("start-workflow", parents=[parent_parser], 
                                         help="Starta arbetsflödeshanteraren i kontinuerligt läge")
    parser_workflow.add_argument("--workers", type=int, default=4, 
                              help="Antal parallella arbetartrådar (default: 4)")
    parser_workflow.add_argument("--queue-dir", type=str, help="Katalog att övervaka för nya jobb")
    parser_workflow.add_argument("--queue-interval", type=int, default=5, 
                                help="Intervall i sekunder mellan kontroller av kökatalogen (default: 5)")
    
    # create-config
    parser_config = subparsers.add_parser("create-config", parents=[parent_parser], 
                                       help="Skapa en standardkonfigurationsfil")
    parser_config.add_argument("--output", type=str, required=True, 
                            help="Sökväg att spara konfigurationsfilen till")
    parser_config.add_argument("--format", choices=["yaml", "json"], default="yaml", 
                            help="Format för konfigurationsfilen (default: yaml)")
    
    # validate-config
    parser_validate = subparsers.add_parser("validate-config", parents=[parent_parser], 
                                         help="Validera en konfigurationsfil")
    parser_validate.add_argument("--config-file", type=str, required=True, 
                              help="Sökväg till konfigurationsfilen att validera")
    
    # test-connection
    parser_test = subparsers.add_parser("test-connection", parents=[parent_parser], 
                                     help="Testa anslutning till LLM-tjänsten")
    parser_test.add_argument("--provider", choices=["ollama", "lmstudio", "oobabooga"], 
                          help="LLM-tjänstleverantör att testa")
    parser_test.add_argument("--model", type=str, help="Modell att testa")
    parser_test.add_argument("--base-url", type=str, help="Bas-URL för LLM-tjänsten")
    
    # generate-faq-answer
    parser_faq = subparsers.add_parser("generate-faq-answer", parents=[parent_parser], 
                                     help="Generera svar på vanliga frågor baserat på extraherad information")
    parser_faq.add_argument("--product-id", type=str, required=True, help="ID för produkten")
    parser_faq.add_argument("--question", type=str, required=True, help="Frågan att besvara")
    parser_faq.add_argument("--result-file", type=str, 
                          help="Sökväg till resultatfil från tidigare bearbetning")
    
    return parser


def init_application(args: argparse.Namespace) -> tuple:
    """
    Initialiserar applikationen baserat på kommandoradsargument
    
    Args:
        args: Kommandoradsargument
        
    Returns:
        tuple: (config_manager, logger, visualizer)
    """
    # Ladda konfiguration
    config_path = args.config if hasattr(args, 'config') and args.config else None
    config_manager = ConfigManager(config_path)
    
    # Åsidosätt med argumentvärden
    if hasattr(args, 'log_level') and args.log_level:
        config_manager.set("general.log_level", args.log_level)
    
    if hasattr(args, 'output_dir') and args.output_dir:
        config_manager.set("general.output_dir", args.output_dir)
    
    if hasattr(args, 'workers') and args.workers:
        config_manager.set("general.max_workers", args.workers)
    
    # Konfigurera färgläge
    use_colors = not (hasattr(args, 'no_color') and args.no_color)
    config_manager.set("general.visualization.use_colors", use_colors)
    
    # Konfigurera verbose-läge
    verbose = hasattr(args, 'verbose') and args.verbose
    config_manager.set("general.verbose", verbose)
    
    # Skapa kataloger
    config_manager.ensure_directories()
    
    # Konfigurera loggning
    from . import setup_logger
    log_config = {
        'log_level': config_manager.get("general.log_level", "INFO"),
        'log_file': args.log_file if hasattr(args, 'log_file') and args.log_file else None,
        'use_colors': use_colors
    }
    logger, visualizer = setup_logger(log_config)
    
    return config_manager, logger, visualizer


def process_single_product(args: argparse.Namespace, config_manager: ConfigManager, 
                          logger: logging.Logger, visualizer) -> None:
    """
    Bearbetar en enskild produkt
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    logger.info(f"Bearbetar produkt {args.product_id} från fil {args.file_path}")
    
    # Skapa LLM-klient
    llm_client = LLMClient(config_manager.get("llm", {}), logger, visualizer)
    
    # Verifiera anslutning
    if not llm_client.verify_connection():
        logger.error("Kunde inte ansluta till LLM-tjänsten, avbryter")
        return
    
    # Konfigurera extraktion
    extraction_config = config_manager.get("extraction", {}).copy()
    
    if hasattr(args, 'extract_compatibility') and args.extract_compatibility:
        extraction_config["compatibility"] = extraction_config.get("compatibility", {})
        extraction_config["compatibility"]["enabled"] = True
    
    if hasattr(args, 'extract_technical') and args.extract_technical:
        extraction_config["technical"] = extraction_config.get("technical", {})
        extraction_config["technical"]["enabled"] = True
    
    if hasattr(args, 'extract_faq') and args.extract_faq:
        extraction_config["faq"] = extraction_config.get("faq", {})
        extraction_config["faq"]["enabled"] = True
    
    # Skapa produktprocessor
    processor = ProductProcessor(extraction_config, llm_client, logger, visualizer)
    
    # Bearbeta produkten
    start_time = time.time()
    result = processor.process_product(args.product_id, args.file_path)
    processing_time = time.time() - start_time
    
    # Validera resultatet
    validation = processor.validate_result(result)
    
    # Spara resultatet
    output_dir = Path(config_manager.get("general.output_dir", "./nlp_bot_engine/data/"))
    output_dir = output_dir / ("validated" if validation.valid else "unvalidated")
    success, saved_path = processor.save_result(result, output_dir)
    
    if success:
        logger.info(f"Sparade resultat till {saved_path}")
        
        # Spara strukturerad data
        structured_dir = Path(config_manager.get("general.output_dir", "./nlp_bot_engine/data/")) / "structured"
        saved_files = processor.save_structured_data(result, structured_dir)
        
        if saved_files:
            logger.info(f"Sparade strukturerad data i {len(saved_files)} filer")
    else:
        logger.error("Kunde inte spara resultat")
    
    # Visa sammanfattning
    logger.info(f"Bearbetning slutförd på {processing_time:.2f} sekunder")
    logger.info(f"Status: {result.status.value}")
    logger.info(f"Kompatibilitetsrelationer: {result.get_compatibility_count()}")
    logger.info(f"Tekniska specifikationer: {result.get_technical_count()}")
    
    if result.errors:
        logger.error(f"Fel: {len(result.errors)}")
        for error in result.errors[:5]:  # Visa bara de första 5 felen
            logger.error(f"  - {error}")
        
        if len(result.errors) > 5:
            logger.error(f"  ... och {len(result.errors) - 5} till")
    
    if validation.valid:
        logger.info("Validering: OK")
    else:
        logger.warning("Validering: MISSLYCKAD")
        for error in validation.errors[:5]:  # Visa bara de första 5 felen
            logger.warning(f"  - {error}")
        
        if len(validation.errors) > 5:
            logger.warning(f"  ... och {len(validation.errors) - 5} till")


def process_directory(args: argparse.Namespace, config_manager: ConfigManager, 
                     logger: logging.Logger, visualizer) -> None:
    """
    Bearbetar alla produkter i en katalog
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    logger.info(f"Bearbetar katalog {args.directory} med mönster {args.pattern}")
    
    # Uppdatera konfiguration
    config_manager.set("general.max_workers", args.workers)
    config_manager.set("workflow.batch_size", args.batch_size)
    
    # Skapa nödvändiga objekt
    llm_client = LLMClient(config_manager.get("llm", {}), logger, visualizer)
    
    # Verifiera anslutning
    if not llm_client.verify_connection():
        logger.error("Kunde inte ansluta till LLM-tjänsten, avbryter")
        return
    
    # Skapa processeringskö
    processing_queue = ProcessingQueue(config_manager.get("workflow", {}), logger)
    
    # Skapa processor
    processor = ProductProcessor(config_manager.get("extraction", {}), llm_client, logger, visualizer)
    
    # Skapa arbetsflödeshanterare
    workflow_manager = WorkflowManager(config_manager, logger, visualizer)
    
    # Starta arbetsflödeshanteraren
    workflow_manager.start()
    
    try:
        # Bearbeta katalogen
        directory = Path(args.directory)
        priority = JobPriority[args.priority]
        
        # Hitta filer
        glob_pattern = "**/" + args.pattern if args.recursive else args.pattern
        reports = workflow_manager.process_directory(directory, glob_pattern, args.batch_size, priority)
        
        # Visa sammanfattning
        total_products = sum(report["total_products"] for report in reports)
        enqueued_products = sum(report["enqueued_products"] for report in reports)
        
        logger.info(f"Bearbetning slutförd. Lade till {enqueued_products}/{total_products} produkter i kön")
        
        # Vänta tills alla jobb är färdiga
        if enqueued_products > 0:
            logger.info("Väntar på att alla jobb ska slutföras...")
            
            # Visa status med jämna mellanrum
            while not processing_queue.is_empty() or len(workflow_manager.processing_queue.active_jobs) > 0:
                status = workflow_manager.get_status()
                queue_status = status["queue"]
                
                logger.info(
                    f"Status: {queue_status['completed_jobs']}/{enqueued_products} slutförda, "
                    f"{queue_status['active_jobs']} aktiva, "
                    f"{queue_status['failed_jobs']} misslyckade"
                )
                
                # Visa i visualizer om tillgänglig
                if visualizer:
                    visualizer.display_markdown(
                        f"# Arbetsflödesstatus\n\n"
                        f"- **Slutförda jobb:** {queue_status['completed_jobs']}/{enqueued_products}\n"
                        f"- **Aktiva jobb:** {queue_status['active_jobs']}\n"
                        f"- **Misslyckade jobb:** {queue_status['failed_jobs']}\n"
                        f"- **Återstående i kö:** {queue_status['pending_jobs']}\n"
                    )
                
                # Vänta en stund innan nästa uppdatering
                time.sleep(5)
            
            # Visa slutlig status
            status = workflow_manager.get_status()
            queue_status = status["queue"]
            
            logger.info(
                f"Alla jobb slutförda. Resultat: "
                f"{queue_status['completed_jobs']} slutförda, "
                f"{queue_status['failed_jobs']} misslyckade"
            )
            
            # Visa i visualizer om tillgänglig
            if visualizer:
                visualizer.display_markdown(
                    f"# Bearbetning slutförd\n\n"
                    f"- **Slutförda jobb:** {queue_status['completed_jobs']}/{enqueued_products}\n"
                    f"- **Misslyckade jobb:** {queue_status['failed_jobs']}\n"
                )
    
    finally:
        # Stoppa arbetsflödeshanteraren
        workflow_manager.stop()
        workflow_manager.join(timeout=5)


def process_csv(args: argparse.Namespace, config_manager: ConfigManager, 
               logger: logging.Logger, visualizer) -> None:
    """
    Bearbetar produkter listade i en CSV-fil
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    logger.info(f"Bearbetar CSV-fil {args.csv_file}")
    
    # Uppdatera konfiguration
    config_manager.set("general.max_workers", args.workers)
    config_manager.set("workflow.batch_size", args.batch_size)
    
    # Skapa nödvändiga objekt
    llm_client = LLMClient(config_manager.get("llm", {}), logger, visualizer)
    
    # Verifiera anslutning
    if not llm_client.verify_connection():
        logger.error("Kunde inte ansluta till LLM-tjänsten, avbryter")
        return
    
    # Skapa processeringskö
    processing_queue = ProcessingQueue(config_manager.get("workflow", {}), logger)
    
    # Skapa processor
    processor = ProductProcessor(config_manager.get("extraction", {}), llm_client, logger, visualizer)
    
    # Skapa arbetsflödeshanterare
    workflow_manager = WorkflowManager(config_manager, logger, visualizer)
    
    # Starta arbetsflödeshanteraren
    workflow_manager.start()
    
    try:
        # Bearbeta CSV-filen
        csv_file = Path(args.csv_file)
        priority = JobPriority[args.priority]
        
        # Bearbeta CSV
        reports = workflow_manager.process_csv(
            csv_file, args.id_column, args.path_column,
            args.batch_size, priority, args.encoding, args.delimiter
        )
        
        # Visa sammanfattning
        if reports:
            total_products = sum(report["total_products"] for report in reports)
            enqueued_products = sum(report["enqueued_products"] for report in reports)
            
            logger.info(f"Bearbetning slutförd. Lade till {enqueued_products}/{total_products} produkter i kön")
            
            # Vänta tills alla jobb är färdiga
            if enqueued_products > 0:
                logger.info("Väntar på att alla jobb ska slutföras...")
                
                # Visa status med jämna mellanrum
                while not processing_queue.is_empty() or len(workflow_manager.processing_queue.active_jobs) > 0:
                    status = workflow_manager.get_status()
                    queue_status = status["queue"]
                    
                    logger.info(
                        f"Status: {queue_status['completed_jobs']}/{enqueued_products} slutförda, "
                        f"{queue_status['active_jobs']} aktiva, "
                        f"{queue_status['failed_jobs']} misslyckade"
                    )
                    
                    # Visa i visualizer om tillgänglig
                    if visualizer:
                        visualizer.display_markdown(
                            f"# Arbetsflödesstatus\n\n"
                            f"- **Slutförda jobb:** {queue_status['completed_jobs']}/{enqueued_products}\n"
                            f"- **Aktiva jobb:** {queue_status['active_jobs']}\n"
                            f"- **Misslyckade jobb:** {queue_status['failed_jobs']}\n"
                            f"- **Återstående i kö:** {queue_status['pending_jobs']}\n"
                        )
                    
                    # Vänta en stund innan nästa uppdatering
                    time.sleep(5)
                
                # Visa slutlig status
                status = workflow_manager.get_status()
                queue_status = status["queue"]
                
                logger.info(
                    f"Alla jobb slutförda. Resultat: "
                    f"{queue_status['completed_jobs']} slutförda, "
                    f"{queue_status['failed_jobs']} misslyckade"
                )
                
                # Visa i visualizer om tillgänglig
                if visualizer:
                    visualizer.display_markdown(
                        f"# Bearbetning slutförd\n\n"
                        f"- **Slutförda jobb:** {queue_status['completed_jobs']}/{enqueued_products}\n"
                        f"- **Misslyckade jobb:** {queue_status['failed_jobs']}\n"
                    )
        else:
            logger.error("Ingen bearbetning utfördes")
            
    finally:
        # Stoppa arbetsflödeshanteraren
        workflow_manager.stop()
        workflow_manager.join(timeout=5)


def start_workflow(args: argparse.Namespace, config_manager: ConfigManager, 
                  logger: logging.Logger, visualizer) -> None:
    """
    Startar arbetsflödeshanteraren i kontinuerligt läge
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    logger.info("Startar arbetsflödeshanteraren i kontinuerligt läge")
    
    # Uppdatera konfiguration
    config_manager.set("general.max_workers", args.workers)
    
    # Konfigurera köövervakningskatalog
    queue_dir = None
    if hasattr(args, 'queue_dir') and args.queue_dir:
        queue_dir = Path(args.queue_dir)
        queue_dir.mkdir(exist_ok=True, parents=True)
        logger.info(f"Övervakar katalog {queue_dir} för nya jobb")
    
    # Skapa arbetsflödeshanterare
    workflow_manager = WorkflowManager(config_manager, logger, visualizer)
    
    # Starta arbetsflödeshanteraren
    workflow_manager.start()
    
    try:
        logger.info("Arbetsflödeshanteraren är redo. Tryck Ctrl+C för att avsluta")
        
        # Visa statusmeddelande
        if visualizer:
            visualizer.display_markdown(
                f"# Arbetsflödeshanterare startad\n\n"
                f"- **Antal arbetare:** {args.workers}\n"
                f"- **Konfiguration:** {args.config or 'standard'}\n"
                f"- **Övervakningskatalog:** {queue_dir or 'Ingen'}\n\n"
                f"Arbetsflödeshanteraren är redo. Tryck **Ctrl+C** för att avsluta.\n"
            )
        
        # Huvudloop för att övervaka kökatalogen
        queue_interval = args.queue_interval if hasattr(args, 'queue_interval') else 5
        
        while True:
            if queue_dir:
                # Kontrollera om det finns nya jobbfiler i kökatalogen
                job_files = list(queue_dir.glob("*.json"))
                
                for job_file in job_files:
                    try:
                        with open(job_file, 'r', encoding='utf-8') as f:
                            job_data = json.load(f)
                        
                        # Validera jobbdata
                        if "product_id" in job_data and "file_path" in job_data:
                            product_id = job_data["product_id"]
                            file_path = job_data["file_path"]
                            priority = JobPriority[job_data.get("priority", "NORMAL")]
                            
                            # Lägg till jobbet i kön
                            job_id = workflow_manager.enqueue_product(product_id, file_path, priority)
                            
                            if job_id:
                                logger.info(f"Lade till jobb för produkt {product_id} från fil {job_file}")
                                
                                # Flytta jobbfilen till en bearbetad-katalog
                                processed_dir = queue_dir / "processed"
                                processed_dir.mkdir(exist_ok=True, parents=True)
                                
                                job_file.rename(processed_dir / job_file.name)
                            else:
                                logger.error(f"Kunde inte lägga till jobb från fil {job_file}")
                                
                                # Flytta jobbfilen till en fel-katalog
                                error_dir = queue_dir / "error"
                                error_dir.mkdir(exist_ok=True, parents=True)
                                
                                job_file.rename(error_dir / job_file.name)
                        else:
                            logger.error(f"Ogiltig jobbfil {job_file}: saknar product_id eller file_path")
                            
                            # Flytta jobbfilen till en fel-katalog
                            error_dir = queue_dir / "error"
                            error_dir.mkdir(exist_ok=True, parents=True)
                            
                            job_file.rename(error_dir / job_file.name)
                    
                    except Exception as e:
                        logger.error(f"Fel vid bearbetning av jobbfil {job_file}: {str(e)}")
                        
                        # Flytta jobbfilen till en fel-katalog
                        try:
                            error_dir = queue_dir / "error"
                            error_dir.mkdir(exist_ok=True, parents=True)
                            
                            job_file.rename(error_dir / job_file.name)
                        except Exception as move_error:
                            logger.error(f"Kunde inte flytta jobbfil {job_file}: {str(move_error)}")
            
            # Visa status
            status = workflow_manager.get_status()
            queue_status = status["queue"]
            
            logger.info(
                f"Status: {queue_status['completed_jobs']} slutförda, "
                f"{queue_status['active_jobs']} aktiva, "
                f"{queue_status['failed_jobs']} misslyckade, "
                f"{queue_status['pending_jobs']} väntande"
            )
            
            # Visa i visualizer om tillgänglig
            if visualizer:
                visualizer.display_markdown(
                    f"# Arbetsflödesstatus\n\n"
                    f"- **Slutförda jobb:** {queue_status['completed_jobs']}\n"
                    f"- **Aktiva jobb:** {queue_status['active_jobs']}\n"
                    f"- **Misslyckade jobb:** {queue_status['failed_jobs']}\n"
                    f"- **Väntande jobb:** {queue_status['pending_jobs']}\n"
                    f"- **Schemalagda jobb:** {status['scheduled_jobs']}\n\n"
                    f"Senaste uppdatering: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
            
            # Vänta en stund innan nästa iteration
            time.sleep(queue_interval)
    
    except KeyboardInterrupt:
        logger.info("Avbruten av användaren")
    finally:
        # Stoppa arbetsflödeshanteraren
        workflow_manager.stop()
        workflow_manager.join(timeout=5)
        
        logger.info("Arbetsflödeshanteraren har stoppats")


def create_config(args: argparse.Namespace, config_manager: ConfigManager, 
                 logger: logging.Logger, visualizer) -> None:
    """
    Skapar en standardkonfigurationsfil
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    output_path = Path(args.output)
    
    # Kontrollera filformatet
    if args.format == "yaml" and not output_path.suffix in [".yaml", ".yml"]:
        output_path = output_path.with_suffix(".yaml")
    elif args.format == "json" and not output_path.suffix == ".json":
        output_path = output_path.with_suffix(".json")
    
    # Spara konfigurationen
    if config_manager.save_config(output_path):
        logger.info(f"Skapade standardkonfigurationsfil: {output_path}")
        
        # Visa konfiguration
        if args.verbose:
            config_manager.print_config()
    else:
        logger.error(f"Kunde inte skapa konfigurationsfil: {output_path}")


def validate_config(args: argparse.Namespace, config_manager: ConfigManager, 
                   logger: logging.Logger, visualizer) -> None:
    """
    Validerar en konfigurationsfil
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    config_file = Path(args.config_file)
    
    if not config_file.exists():
        logger.error(f"Konfigurationsfilen existerar inte: {config_file}")
        return
    
    # Ladda och validera konfigurationen
    test_config = ConfigManager(config_file)
    validation_errors = test_config.validate()
    
    if validation_errors:
        logger.error(f"Konfigurationsfilen har {len(validation_errors)} fel:")
        
        for error in validation_errors:
            logger.error(f"  - {error.path}: {error.message}")
        
        # Visa i visualizer om tillgänglig
        if visualizer:
            visualizer.display_error(
                f"Konfigurationsfilen {config_file} har {len(validation_errors)} fel"
            )
    else:
        logger.info(f"Konfigurationsfilen {config_file} är giltig")
        
        # Visa konfiguration
        if args.verbose:
            test_config.print_config()
        
        # Visa i visualizer om tillgänglig
        if visualizer:
            visualizer.display_markdown(
                f"# Konfigurationsvalidering\n\n"
                f"Konfigurationsfilen **{config_file}** är giltig.\n"
            )


def test_connection(args: argparse.Namespace, config_manager: ConfigManager, 
                   logger: logging.Logger, visualizer) -> None:
    """
    Testar anslutning till LLM-tjänsten
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    # Uppdatera konfiguration
    if hasattr(args, 'provider') and args.provider:
        config_manager.set("llm.provider", args.provider)
    
    if hasattr(args, 'model') and args.model:
        config_manager.set("llm.model", args.model)
    
    if hasattr(args, 'base_url') and args.base_url:
        config_manager.set("llm.base_url", args.base_url)
    
    # Skapa LLM-klient
    llm_client = LLMClient(config_manager.get("llm", {}), logger, visualizer)
    
    # Testa anslutning
    logger.info("Testar anslutning till LLM-tjänsten...")
    
    if llm_client.verify_connection():
        logger.info("Anslutning till LLM-tjänsten lyckades")
        
        # Skapa en enkel prompttest
        test_prompt = "Detta är ett test. Svara med 'Anslutningstest lyckades!'."
        logger.info("Skickar testprompt...")
        
        response = llm_client.get_completion(test_prompt)
        
        if response.successful:
            logger.info(f"Fick svar från LLM-tjänsten: {response.text}")
            logger.info(f"Tokens: {response.total_tokens}, Latens: {response.latency_ms} ms")
            
            # Visa i visualizer om tillgänglig
            if visualizer:
                visualizer.display_markdown(
                    f"# LLM-anslutningstest\n\n"
                    f"Anslutning till LLM-tjänsten **lyckades**.\n\n"
                    f"## Testprompt\n\n"
                    f"{test_prompt}\n\n"
                    f"## Svar\n\n"
                    f"{response.text}\n\n"
                    f"- **Tokens:** {response.total_tokens}\n"
                    f"- **Latens:** {response.latency_ms} ms\n"
                )
        else:
            logger.error(f"Fick felaktigt svar från LLM-tjänsten: {response.error}")
            
            # Visa i visualizer om tillgänglig
            if visualizer:
                visualizer.display_error(
                    f"Anslutning lyckades men kunde inte få ett svar: {response.error}"
                )
    else:
        logger.error("Kunde inte ansluta till LLM-tjänsten")
        
        # Visa i visualizer om tillgänglig
        if visualizer:
            visualizer.display_error("Kunde inte ansluta till LLM-tjänsten")


def generate_faq_answer(args: argparse.Namespace, config_manager: ConfigManager, 
                       logger: logging.Logger, visualizer) -> None:
    """
    Genererar svar på vanliga frågor baserat på extraherad information
    
    Args:
        args: Kommandoradsargument
        config_manager: Konfigurationshanterare
        logger: Logger
        visualizer: Visualiserare
    """
    product_id = args.product_id
    question = args.question
    
    logger.info(f"Genererar svar på frågan '{question}' för produkt {product_id}")
    
    # Skapa LLM-klient
    llm_client = LLMClient(config_manager.get("llm", {}), logger, visualizer)
    
    # Verifiera anslutning
    if not llm_client.verify_connection():
        logger.error("Kunde inte ansluta till LLM-tjänsten, avbryter")
        return
    
    # Skapa produktprocessor
    processor = ProductProcessor(config_manager.get("extraction", {}), llm_client, logger, visualizer)
    
    # Ladda tidigare resultat om angivet
    result = None
    if hasattr(args, 'result_file') and args.result_file:
        result_file = Path(args.result_file)
        
        if result_file.exists():
            try:
                with open(result_file, 'r', encoding='utf-8') as f:
                    result_data = json.load(f)
                
                # Skapa ProductResult från resultatdatan
                from . import ProductResult, ExtractionStatus
                
                result = ProductResult(product_id=result_data["product_id"])
                result.status = ExtractionStatus(result_data["status"])
                result.compatibility = result_data.get("compatibility", {})
                result.technical = result_data.get("technical", {})
                result.faq_data = result_data.get("faq_data", {})
                
                logger.info(f"Laddade resultat från {result_file}")
            except Exception as e:
                logger.error(f"Kunde inte ladda resultat från {result_file}: {str(e)}")
                result = None
    
    # Generera svar
    answer = processor.generate_faq_answer(product_id, question, result)
    
    # Spara svar
    output_dir = Path(config_manager.get("general.output_dir", "./nlp_bot_engine/data/")) / "faq_answers"
    output_dir.mkdir(exist_ok=True, parents=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    answer_file = output_dir / f"{product_id}_answer_{timestamp}.md"
    
    try:
        with open(answer_file, 'w', encoding='utf-8') as f:
            f.write(f"# Svar på fråga: {question}\n\n")
            f.write(answer)
        
        logger.info(f"Sparade svar till {answer_file}")
    except Exception as e:
        logger.error(f"Kunde inte spara svar: {str(e)}")
    
    # Visa svar
    logger.info("Svar:")
    logger.info("-" * 40)
    logger.info(answer)
    logger.info("-" * 40)
    
    # Visa i visualizer om tillgänglig
    if visualizer:
        visualizer.display_markdown(
            f"# Svar på fråga\n\n"
            f"**Fråga:** {question}\n\n"
            f"**Produkt:** {product_id}\n\n"
            f"## Svar\n\n"
            f"{answer}\n"
        )


def main():
    """Huvudfunktion"""
    # Konfigurera argumenttolkare
    parser = setup_argparse()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialisera applikationen
    config_manager, logger, visualizer = init_application(args)
    
    # Logga start
    logger.info(f"Startar LLM-baserad Produktinformationsextraktor: {args.command}")
    
    try:
        # Utför lämplig åtgärd baserat på kommando
        if args.command == "process-product":
            process_single_product(args, config_manager, logger, visualizer)
        elif args.command == "process-directory":
            process_directory(args, config_manager, logger, visualizer)
        elif args.command == "process-csv":
            process_csv(args, config_manager, logger, visualizer)
        elif args.command == "start-workflow":
            start_workflow(args, config_manager, logger, visualizer)
        elif args.command == "create-config":
            create_config(args, config_manager, logger, visualizer)
        elif args.command == "validate-config":
            validate_config(args, config_manager, logger, visualizer)
        elif args.command == "test-connection":
            test_connection(args, config_manager, logger, visualizer)
        elif args.command == "generate-faq-answer":
            generate_faq_answer(args, config_manager, logger, visualizer)
        else:
            logger.error(f"Okänt kommando: {args.command}")
    
    except KeyboardInterrupt:
        logger.info("Avbruten av användaren")
    except Exception as e:
        logger.error(f"Oväntat fel: {str(e)}")
        logger.error(traceback.format_exc())
        
        # Visa i visualizer om tillgänglig
        if visualizer:
            visualizer.display_error(f"Oväntat fel: {str(e)}", e)
    
    finally:
        # Logga avslut
        logger.info("LLM-baserad Produktinformationsextraktor avslutad")


if __name__ == "__main__":
    main()