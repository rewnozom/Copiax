# Project Details

# Table of Contents
- [..\core\config.py](#-core-configpy)
- [..\core\data_manager.py](#-core-data_managerpy)
- [..\core\engine.py](#-core-enginepy)
- [..\dialog\response_generator.py](#-dialog-response_generatorpy)
- [..\dialog\templates.py](#-dialog-templatespy)
- [..\nlp\context_manager.py](#-nlp-context_managerpy)
- [..\nlp\entity_extractor.py](#-nlp-entity_extractorpy)
- [..\nlp\intent_analyzer.py](#-nlp-intent_analyzerpy)
- [..\nlp\processor.py](#-nlp-processorpy)


# ..\..\core\config.py
## File: ..\..\core\config.py

```py
# ..\..\core\config.py
# nlp_bot_engine/core/config.py

import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List

class BotConfig:
    """
    Konfigurationshanterare för botmotorn.
    Hanterar konfigurationsparametrar och standardvärden.
    """
    
    def __init__(self, config_dict: Dict[str, Any] = None):
        """
        Initialisera konfiguration med givna parametrar eller standardvärden
        
        Args:
            config_dict: Konfigurationsparametrar som dict
        """
        config_dict = config_dict or {}
        
        # Hitta rotkatalogen för projektet
        # Om vi kör från Github/main.py, då är root_dir = Github
        # Om vi kör från nlp_bot_engine/någon_fil.py, då är root_dir = parent av nlp_bot_engine
        current_file = Path(__file__).resolve()
        if "nlp_bot_engine" in str(current_file):
            # Vi är i nlp_bot_engine-modulen
            root_dir = current_file.parent.parent.parent  # Gå upp från core/config.py till förälder av nlp_bot_engine
        else:
            # Antar att vi kör från annan plats, använd current working directory
            root_dir = Path(os.getcwd())
        
        # Bassökvägar relativt rotkatalogen
        self.root_dir = root_dir
        self.base_dir = root_dir / config_dict.get("base_dir", "data")
        self.integrated_data_dir = root_dir / config_dict.get("integrated_data_dir", "integrated_data")
        self.cache_dir = root_dir / config_dict.get("cache_dir", "cache")
        
        # Skapa om de inte existerar
        self.integrated_data_dir.mkdir(exist_ok=True, parents=True)
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        
        # Produktdatakatalog
        self.products_dir = self.integrated_data_dir / "products"
        
        # Debug-logga faktiska sökvägar
        print(f"Script running from: {os.getcwd()}")
        print(f"Root directory: {self.root_dir.absolute()}")
        print(f"Base directory: {self.base_dir.absolute()}")
        print(f"Integrated data directory: {self.integrated_data_dir.absolute()}")
        print(f"Products directory: {self.products_dir.absolute()}")
        print(f"Products directory exists: {self.products_dir.exists()}")
        
        # Sök också efter alternativa platser om produktkatalogen inte finns
        if not self.products_dir.exists():
            alt_product_dirs = [
                root_dir / "data" / "integrated_data" / "products",
                root_dir / "nlp_bot_engine" / "data" / "integrated_data" / "products",
                root_dir.parent / "integrated_data" / "products"
            ]
            
            for alt_dir in alt_product_dirs:
                if alt_dir.exists():
                    print(f"Found alternative products directory: {alt_dir}")
                    self.products_dir = alt_dir
                    self.integrated_data_dir = alt_dir.parent
                    break
        
        # NLP-inställningar
        self.use_nlp = config_dict.get("use_nlp", True)
        self.spacy_model = config_dict.get("spacy_model", "sv_core_news_lg")  # Svenska (stor modell)
        self.embeddings_model = config_dict.get("embeddings_model", "KBLab/sentence-bert-swedish-cased")
        self.min_confidence = config_dict.get("min_confidence", 0.6)
        
        # Svarsalternativ
        self.response_settings = config_dict.get("response_settings", {})
        self.max_search_results = config_dict.get("max_search_results", 5)
        
        # Svarsgenerering
        self.response_templates = config_dict.get("response_templates", {
            "technical": "# Tekniska specifikationer för {product_name}\n\n" +
                         "**Artikelnummer:** {product_id}\n\n{specifications}",
            "compatibility": "# Kompatibilitetsinformation för {product_name}\n\n" +
                             "**Artikelnummer:** {product_id}\n\n{compatibility}",
            "summary": "# {product_name}\n\n" +
                       "**Artikelnummer:** {product_id}\n\n" +
                       "{description}\n\n{specifications}\n\n{compatibility}"
        })
        
        # Prestandainställningar
        self.cache_enabled = config_dict.get("cache_enabled", True)
        self.cache_ttl = config_dict.get("cache_ttl", 3600)  # 1 timme
        self.max_workers = config_dict.get("max_workers", os.cpu_count())
        
        # Debug och loggning
        self.debug = config_dict.get("debug", False)
        self.verbose = config_dict.get("verbose", False)
        
        # Återkoppling och lärande
        self.enable_learning = config_dict.get("enable_learning", False)
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Konvertera konfigurationen till en dictionary
        
        Returns:
            Dict representation av konfigurationen
        """
        return {
            "base_dir": str(self.base_dir),
            "integrated_data_dir": str(self.integrated_data_dir),
            "cache_dir": str(self.cache_dir),
            "products_dir": str(self.products_dir),
            "use_nlp": self.use_nlp,
            "spacy_model": self.spacy_model,
            "embeddings_model": self.embeddings_model,
            "min_confidence": self.min_confidence,
            "response_settings": self.response_settings,
            "max_search_results": self.max_search_results,
            "response_templates": self.response_templates,
            "cache_enabled": self.cache_enabled,
            "cache_ttl": self.cache_ttl,
            "max_workers": self.max_workers,
            "debug": self.debug,
            "verbose": self.verbose,
            "enable_learning": self.enable_learning
        }
    
    def update(self, new_config: Dict[str, Any]) -> None:
        """
        Uppdatera konfigurationen med nya parametrar
        
        Args:
            new_config: Nya konfigurationsparametrar
        """
        # Återinitiera med kombinerade konfigurationer
        current_config = self.to_dict()
        current_config.update(new_config)
        self.__init__(current_config)
```

---

# ..\..\core\data_manager.py
## File: ..\..\core\data_manager.py

```py
# ..\..\core\data_manager.py
# nlp_bot_engine/core/data_manager.py

import json
import os
import re
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from collections import defaultdict

from .config import BotConfig

logger = logging.getLogger(__name__)

class DataManager:
    """
    Hanterar data och index för produkter och deras egenskaper.
    Ansvarar för att läsa, söka och extrahera produktinformation.
    """
    
    def __init__(self, config: BotConfig):
        """
        Initialisera datahanteraren med konfiguration
        
        Args:
            config: Konfigurationsobjekt
        """
        self.config = config
        
        # Grundläggande sökvägar
        self.integrated_data_dir = config.integrated_data_dir
        self.products_dir = config.products_dir
        
        # Debug-loggning för att se sökvägar
        logger.debug(f"Integrated data directory: {self.integrated_data_dir}")
        logger.debug(f"Products directory: {self.products_dir}")
        logger.debug(f"Products directory exists: {self.products_dir.exists()}")
        
        # Ladda index
        self.indices = self.load_indices()
        
        # Skapa product_names.json om det inte finns
        self._create_product_names_index_if_needed()
        
        # Bygg omvänt index för produktnamn till ID
        self.name_to_id_map = {}
        for product_id, data in self.indices.get("product_names", {}).items():
            name = data.get("name", "").lower()
            if name:
                self.name_to_id_map[name] = product_id
        
        # Cache för produktdata
        self.product_cache = {}
        
        logger.info(f"DataManager initialiserad med {len(self.name_to_id_map)} produkter")
    
    def _create_product_names_index_if_needed(self):
        """
        Skapa product_names.json om det inte finns genom att samla information från produktmappar
        """
        if "product_names" not in self.indices or not self.indices["product_names"]:
            logger.info("Skapar product_names.json från tillgänglig produktdata")
            product_names = {}
            
            # Gå igenom alla produktmappar
            if self.products_dir.exists():
                for product_dir in self.products_dir.iterdir():
                    if product_dir.is_dir():
                        product_id = product_dir.name
                        
                        # Försök hitta produktnamn från summary.jsonl
                        summary_path = product_dir / "summary.jsonl"
                        if summary_path.exists():
                            try:
                                with open(summary_path, 'r', encoding='utf-8') as f:
                                    summary_data = json.loads(f.readline())
                                    if "product_name" in summary_data:
                                        product_names[product_id] = {
                                            "name": summary_data["product_name"]
                                        }
                                        continue
                            except Exception:
                                pass
                        
                        # Fallback till full_info.md för att hitta en rubrik
                        full_info_path = product_dir / "full_info.md"
                        if full_info_path.exists():
                            try:
                                with open(full_info_path, 'r', encoding='utf-8') as f:
                                    for line in f:
                                        if line.startswith('# ') or line.startswith('## '):
                                            product_names[product_id] = {
                                                "name": line.strip('# \n')
                                            }
                                            break
                                    continue
                            except Exception:
                                pass
                        
                        # Fallback till generisk produkt
                        product_names[product_id] = {
                            "name": f"Produkt {product_id}"
                        }
            
            # Spara index
            if product_names:
                self.indices["product_names"] = product_names
                try:
                    indices_dir = self.integrated_data_dir / "indices"
                    indices_dir.mkdir(exist_ok=True, parents=True)
                    
                    index_path = indices_dir / "product_names.json"
                    with open(index_path, 'w', encoding='utf-8') as f:
                        json.dump(product_names, f, ensure_ascii=False, indent=2)
                    
                    logger.info(f"Skapade product_names.json med {len(product_names)} produkter")
                except Exception as e:
                    logger.error(f"Kunde inte spara product_names.json: {str(e)}")
    
    def load_indices(self) -> Dict[str, Dict[str, Any]]:
        """
        Ladda alla indexfiler för sökning och åtkomst
        
        Returns:
            Dict med alla index
        """
        index_types = [
            "article_numbers.json",
            "ean_numbers.json",
            "compatibility_map.json", 
            "technical_specs_index.json",
            "text_search_index.json",
            "product_names.json"
        ]
        
        # Initiera indices-dictionary
        indices = {}
        
        # Kontrollera om indices-katalogen finns
        indices_dir = self.integrated_data_dir / "indices"
        logger.debug(f"Looking for indices in: {indices_dir}")
        logger.debug(f"Indices directory exists: {indices_dir.exists()}")
        
        # Skapa katalogen om den inte finns
        indices_dir.mkdir(exist_ok=True, parents=True)
        
        # Ladda varje indextyp
        for index_name in index_types:
            logger.debug(f"Attempting to load index: {index_name}")
            index_data = self._load_index(index_name)
            
            # Extrahera basnamnet utan filändelse för nyckeln
            key = index_name.split('.')[0]
            indices[key] = index_data
        
        return indices
    
    def _load_index(self, index_name: str) -> Dict[str, Any]:
        """
        Ladda ett specifikt index från fil
        
        Args:
            index_name: Filnamnet för indexet
            
        Returns:
            Index som dict eller tom dict vid fel
        """
        index_path = self.integrated_data_dir / "indices" / index_name
        logger.debug(f"Loading index from: {index_path}")
        logger.debug(f"File exists: {index_path.exists()}")
        
        # Försök ladda JSON-fil
        try:
            if index_path.exists():
                with open(index_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.debug(f"Successfully loaded JSON index {index_name} with {len(data)} entries")
                    return data
        except Exception as e:
            logger.error(f"Kunde inte ladda JSON-index {index_name}: {str(e)}")
        
        # Försök med JSONL-fil om JSON misslyckades
        jsonl_path = self.integrated_data_dir / "indices" / index_name.replace('.json', '.jsonl')
        logger.debug(f"Trying JSONL index: {jsonl_path}")
        logger.debug(f"JSONL exists: {jsonl_path.exists()}")
        
        try:
            if jsonl_path.exists():
                data = {}
                with open(jsonl_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip() and not line.startswith('#'):
                            entry = json.loads(line)
                            # Anpassa efter olika index-strukturer
                            if "product_id" in entry:
                                key = entry["product_id"]
                                data[key] = entry
                            elif index_name == "product_names.jsonl" and "id" in entry:
                                key = entry["id"]
                                data[key] = {"name": entry.get("name", f"Produkt {key}")}
                                
                logger.debug(f"Successfully loaded JSONL index {jsonl_path.name} with {len(data)} entries")
                return data
        except Exception as e:
            logger.error(f"Kunde inte ladda JSONL-index {jsonl_path.name}: {str(e)}")
        
        # Returnera tom dict om ingen fil kunde laddas
        return {}
    
    def get_technical_specs(self, product_id: str, params: str = "") -> Dict[str, Any]:
        """
        Hämta tekniska specifikationer för en produkt
        
        Args:
            product_id: Produktens ID
            params: Extra parametrar (t.ex. filterinställningar)
            
        Returns:
            Dict med specifikationer och status
        """
        product_dir = self.products_dir / product_id
        tech_path = product_dir / "technical_specs.jsonl"
        
        if not tech_path.exists():
            return {
                "status": "error",
                "message": "Inga tekniska specifikationer tillgängliga"
            }
        
        try:
            # Läs tekniska specifikationer
            specs = []
            with open(tech_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        specs.append(json.loads(line))
            
            # Gruppera specifikationer efter kategori
            grouped_specs = defaultdict(list)
            for spec in specs:
                category = spec.get("category", "Övrigt")
                grouped_specs[category].append(spec)
            
            # Filtrera baserat på parametrar om det finns
            if params:
                # Tolka parametrar som filter
                filter_terms = [term.lower() for term in params.split()]
                
                # Filtrera både kategorier och specifikationer
                filtered_specs = defaultdict(list)
                for category, category_specs in grouped_specs.items():
                    if any(term in category.lower() for term in filter_terms):
                        filtered_specs[category] = category_specs
                    else:
                        # Filtrera individuella specifikationer
                        matching_specs = []

                        for spec in category_specs:
                            name = spec.get("name", "").lower()
                            value = str(spec.get("raw_value", "")).lower()
                            if any(term in name or term in value for term in filter_terms):
                                matching_specs.append(spec)
                        
                        if matching_specs:
                            filtered_specs[category] = matching_specs
                
                # Använd filtrerade specifikationer om några matchningar hittades
                if filtered_specs:
                    grouped_specs = filtered_specs
            
            # Formatera specifikationer för presentation
            formatted_specs = []
            for category, category_specs in grouped_specs.items():
                formatted_specs.append(f"## {category}")
                for spec in sorted(category_specs, key=lambda x: x.get("importance", "normal"), reverse=True):
                    name = spec.get("name", "")
                    value = spec.get("raw_value", "")
                    unit = spec.get("unit", "")
                    
                    if name and value:
                        formatted_spec = f"- **{name}:** {value}"
                        if unit and unit not in value:
                            formatted_spec += f" {unit}"
                        formatted_specs.append(formatted_spec)
                
                formatted_specs.append("")  # Tomrad mellan kategorier
            
            return {
                "status": "success",
                "specs": specs,
                "specs_by_category": dict(grouped_specs),
                "formatted_text": "\n".join(formatted_specs)
            }
            
        except Exception as e:
            logger.error(f"Fel vid läsning av tekniska specifikationer för {product_id}: {str(e)}")
            return {
                "status": "error",
                "message": f"Kunde inte läsa tekniska specifikationer: {str(e)}"
            }
    
    def get_compatibility_info(self, product_id: str, params: str = "") -> Dict[str, Any]:
        """
        Hämta kompatibilitetsinformation för en produkt
        
        Args:
            product_id: Produktens ID
            params: Extra parametrar (t.ex. filterinställningar)
            
        Returns:
            Dict med kompatibilitetsinformation och status
        """
        product_dir = self.products_dir / product_id
        compat_path = product_dir / "compatibility.jsonl"
        
        if not compat_path.exists():
            return {
                "status": "error",
                "message": "Ingen kompatibilitetsinformation tillgänglig"
            }
        
        try:
            # Läs kompatibilitetsinformation
            relations = []
            with open(compat_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        relations.append(json.loads(line))
            
            # Gruppera relationer efter typ
            grouped_relations = defaultdict(list)
            for relation in relations:
                rel_type = relation.get("relation_type", "Övrigt")
                grouped_relations[rel_type].append(relation)
            
            # Filtrera baserat på parametrar om det finns
            if params:
                # Tolka parametrar som filter
                filter_terms = [term.lower() for term in params.split()]
                
                # Filtrera både relationstyper och relaterade produkter
                filtered_relations = defaultdict(list)
                for rel_type, type_relations in grouped_relations.items():
                    if any(term in rel_type.lower() for term in filter_terms):
                        filtered_relations[rel_type] = type_relations
                    else:
                        # Filtrera individuella relationer
                        matching_relations = []
                        for relation in type_relations:
                            related_product = relation.get("related_product", "").lower()
                            if any(term in related_product for term in filter_terms):
                                matching_relations.append(relation)
                        
                        if matching_relations:
                            filtered_relations[rel_type] = matching_relations
                
                # Använd filtrerade relationer om några matchningar hittades
                if filtered_relations:
                    grouped_relations = filtered_relations
            
            # Formatera relationer för presentation
            formatted_relations = []
            
            # Definiera visningsnamn för relationstyper
            relation_display = {
                "direct": "Kompatibel med",
                "fits": "Passar till",
                "requires": "Kräver",
                "recommended": "Rekommenderas med",
                "designed_for": "Designad för",
                "accessory": "Tillbehör till",
                "replacement": "Ersätter",
                "replaced_by": "Ersätts av",
                "not_compatible": "Ej kompatibel med"
            }
            
            for rel_type, type_relations in grouped_relations.items():
                # Använd visningsnamn om tillgängligt, annars formatera relationstypen
                display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
                formatted_relations.append(f"## {display_name}")
                
                for relation in sorted(type_relations, key=lambda x: x.get("confidence", 0), reverse=True):
                    related_product = relation.get("related_product", "")
                    numeric_ids = relation.get("numeric_ids", [])
                    
                    if related_product:
                        relation_text = f"- {related_product}"
                        if numeric_ids:
                            relation_text += f" (Art.nr: {numeric_ids[0]})"
                        formatted_relations.append(relation_text)
                
                formatted_relations.append("")  # Tomrad mellan kategorier
            
            return {
                "status": "success",
                "relations": relations,
                "relations_by_type": dict(grouped_relations),
                "formatted_text": "\n".join(formatted_relations)
            }
            
        except Exception as e:
            logger.error(f"Fel vid läsning av kompatibilitetsinformation för {product_id}: {str(e)}")
            return {
                "status": "error",
                "message": f"Kunde inte läsa kompatibilitetsinformation: {str(e)}"
            }
    
    def get_product_summary(self, product_id: str, params: str = "") -> Dict[str, Any]:
        """
        Hämta sammanställning av produktinformation
        
        Args:
            product_id: Produktens ID
            params: Extra parametrar (ej använt för närvarande)
            
        Returns:
            Dict med sammanställd produktinformation och status
        """
        product_dir = self.products_dir / product_id
        summary_path = product_dir / "summary.jsonl"
        
        if not summary_path.exists():
            # Om ingen cachad sammanfattning finns, generera dynamiskt
            return self.generate_dynamic_summary(product_id)
        
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        summary = json.loads(line)
                        break
                else:
                    # Fallback om ingen giltig rad hittades
                    return self.generate_dynamic_summary(product_id)
            
            # Formatera sammanfattningen
            formatted_sections = []
            
            # Lägg till produktnamn och grundläggande info
            if summary.get("product_name"):
                formatted_sections.append(f"# {summary['product_name']}")
            else:
                formatted_sections.append(f"# Produkt {product_id}")
            
            # Lägg till identifierare
            id_section = ["## Identifierare"]
            for id_type, values in summary.get("identifiers", {}).items():
                if values:
                    id_section.append(f"- **{id_type}:** {', '.join(values)}")
            if len(id_section) > 1:
                formatted_sections.extend(id_section)
                formatted_sections.append("")  # Tomrad
            
            # Lägg till beskrivning
            if summary.get("description"):
                formatted_sections.append("## Beskrivning")
                formatted_sections.append(summary["description"])
                formatted_sections.append("")  # Tomrad
            
            # Lägg till viktiga specifikationer
            if summary.get("key_specifications"):
                formatted_sections.append("## Viktiga specifikationer")
                for spec in summary["key_specifications"]:
                    name = spec.get("name", "")
                    value = spec.get("value", "")
                    unit = spec.get("unit", "")
                    if name and value:
                        spec_text = f"- **{name}:** {value}"
                        if unit and unit not in value:
                            spec_text += f" {unit}"
                        formatted_sections.append(spec_text)
                formatted_sections.append("")  # Tomrad
            
            # Lägg till kompatibilitetsinformation
            if summary.get("key_compatibility"):
                formatted_sections.append("## Kompatibilitet")
                
                # Gruppera efter relationstyp
                compat_by_type = defaultdict(list)
                for relation in summary["key_compatibility"]:
                    compat_by_type[relation.get("type", "other")].append(relation)
                
                # Definiera visningsnamn för relationstyper
                relation_display = {
                    "direct": "Kompatibel med",
                    "fits": "Passar till",
                    "requires": "Kräver",
                    "recommended": "Rekommenderas med"
                }
                
                for rel_type, relations in compat_by_type.items():
                    display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
                    formatted_sections.append(f"### {display_name}")
                    
                    for relation in relations:
                        related_product = relation.get("related_product", "")
                        if related_product:
                            compat_text = f"- {related_product}"
                            if relation.get("numeric_ids"):
                                compat_text += f" (Art.nr: {relation['numeric_ids'][0]})"
                            formatted_sections.append(compat_text)
                    
                    formatted_sections.append("")  # Tomrad
            
            return {
                "status": "success",
                "summary": summary,
                "formatted_text": "\n".join(formatted_sections)
            }
            
        except Exception as e:
            logger.error(f"Fel vid läsning av produktsammanfattning för {product_id}: {str(e)}")
            return {
                "status": "error",
                "message": f"Kunde inte läsa produktsammanfattning: {str(e)}"
            }
    
    def generate_dynamic_summary(self, product_id: str) -> Dict[str, Any]:
        """
        Generera en dynamisk sammanfattning när ingen cache finns
        
        Args:
            product_id: Produktens ID
            
        Returns:
            Dict med dynamiskt genererad sammanfattning
        """
        try:
            # Skapa basis för dynamisk sammanfattning
            summary = {
                "product_id": product_id,
                "generated_at": datetime.now().isoformat(),
                "product_name": self.get_product_name(product_id),
                "description": None,
                "key_specifications": [],
                "key_compatibility": [],
                "identifiers": {}
            }
            
            # Hämta tekniska specifikationer
            tech_result = self.get_technical_specs(product_id)
            if tech_result["status"] == "success":
                # Extrahera beskrivning om sådan finns
                for spec in tech_result.get("specs", []):
                    if spec.get("category", "").lower() in ["general", "allmänt", "beskrivning", "description"]:
                        if spec.get("name", "").lower() in ["beskrivning", "description"]:
                            summary["description"] = spec.get("raw_value", "")
                
                # Välj ut de viktigaste specifikationerna (upp till 5)
                key_specs = []
                
                # Sortera efter viktighet och sedan kategori
                sorted_specs = sorted(
                    tech_result.get("specs", []),
                    key=lambda x: (
                        0 if x.get("importance") == "high" else 
                        1 if x.get("importance") == "medium" else 2,
                        x.get("category", "")
                    )
                )
                
                # Ta max 5 viktiga specifikationer
                for spec in sorted_specs[:5]:
                    key_specs.append({
                        "name": spec.get("name", ""),
                        "value": spec.get("raw_value", ""),
                        "unit": spec.get("unit", ""),
                        "category": spec.get("category", "")
                    })
                
                summary["key_specifications"] = key_specs
            
            # Hämta kompatibilitetsinformation
            compat_result = self.get_compatibility_info(product_id)
            if compat_result["status"] == "success":
                # Välj ut de viktigaste kompatibilitetsrelationerna (upp till 5)
                key_compat = []
                
                # Sortera efter viktighet (de som har produkt-ID först)
                sorted_compat = sorted(
                    compat_result.get("relations", []),
                    key=lambda x: (
                        0 if x.get("numeric_ids") else 1,
                        x.get("confidence", 0)
                    ),
                    reverse=True
                )
                
                # Ta max 5 viktiga relationer
                for relation in sorted_compat[:5]:
                    key_compat.append({
                        "type": relation.get("relation_type", ""),
                        "related_product": relation.get("related_product", ""),
                        "has_product_id": bool(relation.get("numeric_ids")),
                        "numeric_ids": relation.get("numeric_ids", [])
                    })
                
                summary["key_compatibility"] = key_compat
            
            # Hämta identifierare från artikel_info.jsonl om den finns
            ids_path = self.products_dir / product_id / "article_info.jsonl"
            if ids_path.exists():
                try:
                    ids_by_type = defaultdict(list)
                    with open(ids_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip() and not line.startswith('#'):
                                identifier = json.loads(line)
                                id_type = identifier.get("type", "")
                                value = identifier.get("value", "")
                                if id_type and value:
                                    ids_by_type[id_type].append(value)
                    
                    summary["identifiers"] = dict(ids_by_type)
                except Exception as e:
                    logger.warning(f"Kunde inte läsa identifierare för {product_id}: {str(e)}")
            
            # Återanvänd formateringslogik från get_product_summary
            result = {
                "status": "success",
                "summary": summary,
                "dynamically_generated": True
            }
            
            # Skapa formatterad text
            formatted_text = self.format_summary(summary)
            result["formatted_text"] = formatted_text
            
            return result
            
        except Exception as e:
            logger.error(f"Fel vid generering av dynamisk sammanfattning för {product_id}: {str(e)}")
            return {
                "status": "error",
                "message": f"Kunde inte generera sammanfattning: {str(e)}"
            }
    
    def format_summary(self, summary: Dict[str, Any]) -> str:
        """
        Formatera en sammanfattning som markdown-text
        
        Args:
            summary: Sammanfattningsobjektet
            
        Returns:
            Formaterad markdown-text
        """
        formatted_sections = []
        
        # Lägg till produktnamn och grundläggande info
        if summary.get("product_name"):
            formatted_sections.append(f"# {summary['product_name']}")
        else:
            formatted_sections.append(f"# Produkt {summary.get('product_id', '')}")
        
        formatted_sections.append("")  # Tomrad
        
        # Lägg till produkt-ID om det finns
        if "product_id" in summary:
            formatted_sections.append(f"**Artikelnummer:** {summary['product_id']}")
            formatted_sections.append("")  # Tomrad
        
        # Lägg till identifierare
        id_lines = []
        for id_type, values in summary.get("identifiers", {}).items():
            if values:
                id_lines.append(f"**{id_type}:** {', '.join(values)}")
        
        if id_lines:
            formatted_sections.extend(id_lines)
            formatted_sections.append("")  # Tomrad
        
        # Lägg till beskrivning
        if summary.get("description"):
            formatted_sections.append("## Beskrivning")
            formatted_sections.append(summary["description"])
            formatted_sections.append("")  # Tomrad
        
        # Lägg till viktiga specifikationer
        if summary.get("key_specifications"):
            formatted_sections.append("## Viktiga specifikationer")
            
            # Gruppera efter kategori
            specs_by_category = defaultdict(list)
            for spec in summary["key_specifications"]:
                category = spec.get("category", "Övrigt")
                specs_by_category[category].append(spec)
            
            # Lägg till per kategori
            for category, specs in specs_by_category.items():
                if len(specs_by_category) > 1:  # Om mer än en kategori, visa kategorinamn
                    formatted_sections.append(f"### {category}")
                
                for spec in specs:
                    name = spec.get("name", "")
                    value = spec.get("value", "")
                    unit = spec.get("unit", "")
                    if name and value:
                        spec_text = f"- **{name}:** {value}"
                        if unit and unit not in value:
                            spec_text += f" {unit}"
                        formatted_sections.append(spec_text)
            
            formatted_sections.append("")  # Tomrad
        
        # Lägg till kompatibilitetsinformation
        if summary.get("key_compatibility"):
            formatted_sections.append("## Kompatibilitet")
            
            # Gruppera efter relationstyp
            compat_by_type = defaultdict(list)
            for relation in summary["key_compatibility"]:
                compat_by_type[relation.get("type", "other")].append(relation)
            
            # Definiera visningsnamn för relationstyper
            relation_display = {
                "direct": "Kompatibel med",
                "fits": "Passar till",
                "requires": "Kräver",
                "recommended": "Rekommenderas med",
                "designed_for": "Designad för",
                "accessory": "Tillbehör till",
                "replacement": "Ersätter",
                "replaced_by": "Ersätts av"
            }
            
            for rel_type, relations in compat_by_type.items():
                display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
                if len(compat_by_type) > 1:  # Om mer än en relationstyp, visa typ
                    formatted_sections.append(f"### {display_name}")
                
                for relation in relations:
                    related_product = relation.get("related_product", "")
                    if related_product:
                        compat_text = f"- {related_product}"
                        if relation.get("numeric_ids"):
                            compat_text += f" (Art.nr: {relation['numeric_ids'][0]})"
                        formatted_sections.append(compat_text)
            
            formatted_sections.append("")  # Tomrad
        
        return "\n".join(formatted_sections)
    
    def get_full_info(self, product_id: str, params: str = "") -> Dict[str, Any]:
        """
        Hämta fullständig information för en produkt
        
        Args:
            product_id: Produktens ID
            params: Extra parametrar
            
        Returns:
            Dict med fullständig information och status
        """
        product_dir = self.products_dir / product_id
        full_info_path = product_dir / "full_info.md"
        
        if not full_info_path.exists():
            return {
                "status": "error",
                "message": "Ingen fullständig information tillgänglig"
            }
        
        try:
            with open(full_info_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                "status": "success",
                "content": content,
                "formatted_text": content  # Redan i markdown-format
            }
            
        except Exception as e:
            logger.error(f"Fel vid läsning av fullständig information för {product_id}: {str(e)}")
            return {
                "status": "error",
                "message": f"Kunde inte läsa fullständig information: {str(e)}"
            }
    
    def get_product_name(self, product_id: str) -> str:
        """
        Hämta produktnamn baserat på ID
        
        Args:
            product_id: Produktens ID
            
        Returns:
            Produktnamn eller generiskt namn om inget hittas
        """
        product_names = self.indices.get("product_names", {})
        if product_id in product_names:
            return product_names[product_id].get("name", f"Produkt {product_id}")
        
        # Försök hitta namnet från summary.jsonl om produkten inte finns i indices
        product_dir = self.products_dir / product_id
        summary_path = product_dir / "summary.jsonl"
        
        if summary_path.exists():
            try:
                with open(summary_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip() and not line.startswith('#'):
                            summary = json.loads(line)
                            if "product_name" in summary:
                                return summary["product_name"]
            except Exception:
                pass
                
        # Fallback till generiskt produktnamn
        return f"Produkt {product_id}"
    
    def validate_product_id(self, product_id: str) -> bool:
        """
        Validera att ett produkt-ID existerar
        
        Args:
            product_id: Produktens ID
            
        Returns:
            True om produkten existerar, annars False
        """
        product_dir = self.products_dir / product_id
        return product_dir.exists() and product_dir.is_dir()
    
    def search_products(self, query: str, max_results: int = None) -> Dict[str, Any]:
        """
        Sök efter produkter baserat på fritextfråga
        
        Args:
            query: Söktermen
            max_results: Maximalt antal resultat att returnera
            
        Returns:
            Dict med sökresultat och status
        """
        if max_results is None:
            max_results = self.config.max_search_results
        
        # Förbehandla sökfrågan
        query = query.lower()
        query_words = set(query.split())
        
        # Resultatsamling
        results = []
        
        # Sök i text-index för exakta träffar
        exact_matches = set()
        for word in query_words:
            if word in self.indices.get("text_search_index", {}):
                for product_id in self.indices["text_search_index"][word]:
                    exact_matches.add(product_id)
        
        # Lägg till exakta träffar först
        for product_id in exact_matches:
            product_name = self.get_product_name(product_id)
            results.append({
                "product_id": product_id,
                "name": product_name,
                "score": 1.0,  # Högsta poäng för exakta träffar
                "match_type": "exact"
            })
        
        # Om vi inte har tillräckligt med exakta träffar, gör fuzzy matching
        if len(results) < max_results:
            fuzzy_matches = self.find_fuzzy_matches(query, max_results=max_results-len(results))
            
            # Filtrera bort dubbletter
            existing_ids = {result["product_id"] for result in results}
            for match in fuzzy_matches:
                if match["product_id"] not in existing_ids:
                    results.append(match)
        
        # Sortera efter poäng och begränsa resultaten
        results = sorted(results, key=lambda x: x["score"], reverse=True)[:max_results]
        
        # Formatera sökresultaten för presentation
        formatted_results = ["## Sökresultat", ""]
        
        if not results:
            formatted_results.append("Inga produkter hittades som matchar din sökning.")
        else:
            for i, result in enumerate(results, 1):
                formatted_results.append(f"{i}. **{result['name']}** (Art.nr: {result['product_id']})")
            
            formatted_results.append("")
            formatted_results.append("Använd kommandot `-s <artikelnr>` för att se mer information om en produkt.")
        
        return {
            "status": "success",
            "query": query,
            "matches": results,
            "total_matches": len(results),
            "formatted_text": "\n".join(formatted_results)
        }
    
    def find_fuzzy_matches(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Hitta produkter genom fuzzy matching (ungefärlig matchning)
        
        Args:
            query: Söktermen
            max_results: Maximalt antal resultat
            
        Returns:
            Lista med matchande produkter
        """
        # Förbehandla sökfrågan
        query_words = set(query.lower().split())
        
        # Resultatsamling med poäng
        scored_matches = []
        
        # Om name_to_id_map är tom, försök fylla den direkt från produktkataloger
        if not self.name_to_id_map:
            logger.debug("name_to_id_map är tom, försöker skapa från produktkataloger")
            self._create_product_names_index_if_needed()
        
        # Gå igenom alla produktnamn och beräkna matchningspoäng
        for name, product_id in self.name_to_id_map.items():
            name_words = set(name.split())
            
            # Beräkna överlappning mellan ord
            overlap = len(query_words & name_words)
            
            # Beräkna poäng baserat på antal matchande ord och total längd
            if overlap > 0:
                score = overlap / (len(query_words) + len(name_words) - overlap)  # Jaccard-likhet
                
                # Lägg till extra poäng för längre matchningar
                if overlap > 1:
                    score += 0.1 * overlap
                
                # Straffa kortare namn (ofta generiska)
                if len(name_words) <= 2:
                    score *= 0.8
                
                # Lägg till om poängen är över ett tröskelvärde
                if score > 0.2:
                    scored_matches.append({
                        "product_id": product_id,
                        "name": name.title(),  # Gör första bokstaven stor
                        "score": score,
                        "match_type": "fuzzy"
                    })
        
        # Om vi inte hittar några matchningar, sök i produktkataloger istället
        if not scored_matches and self.products_dir.exists():
            for product_dir in self.products_dir.iterdir():
                if product_dir.is_dir():
                    product_id = product_dir.name
                    product_name = self.get_product_name(product_id)
                    
                    # Lägg till alla produkter med lägre score
                    scored_matches.append({
                        "product_id": product_id,
                        "name": product_name,
                        "score": 0.1,  # Låg score för fallback-matchningar
                        "match_type": "directory"
                    })
        
        # Sortera efter poäng och begränsa antalet resultat
        return sorted(scored_matches, key=lambda x: x["score"], reverse=True)[:max_results]
    
    def suggest_products(self, query: str, max_suggestions: int = 3) -> List[Dict[str, Any]]:
        """
        Föreslå produkter baserat på en fråga
        
        Args:
            query: Frågan eller söktermen
            max_suggestions: Maximalt antal förslag
            
        Returns:
            Lista med produktförslag
        """
        # Använd sökmotorn för att hitta relevanta produkter
        search_results = self.search_products(query, max_results=max_suggestions)
        
        # Extrahera produktförslagen
        suggestions = search_results.get("matches", [])
        
        return suggestions
    
    def find_related_products(self, product_id: str, relation_types: List[str] = None) -> List[Dict[str, Any]]:
        """
        Hitta produkter relaterade till en given produkt
        
        Args:
            product_id: Produktens ID
            relation_types: Lista med relationstyper att filtrera på
            
        Returns:
            Lista med relaterade produkter
        """
        # Hämta kompatibilitetskartan
        compat_map = self.indices.get("compatibility_map", {})
        
        if product_id not in compat_map:
            return []
        
        # Hämta alla relationer för produkten
        relations = compat_map[product_id]
        
        # Filtrera på relationstyper om angivet
        if relation_types:
            relations = [r for r in relations if r.get("relation_type") in relation_types]
        
        # Konvertera till resultatformat
        related_products = []
        for relation in relations:
            related_product = relation.get("related_product", "")
            relation_type = relation.get("relation_type", "")
            numeric_ids = relation.get("numeric_ids", [])
            
            # Försök att identifiera produkt-ID om möjligt
            target_product_id = None
            if numeric_ids:
                target_product_id = numeric_ids[0]
            elif related_product.lower() in self.name_to_id_map:
                target_product_id = self.name_to_id_map[related_product.lower()]
            
            if related_product:
                related_products.append({
                    "product_id": target_product_id,
                    "name": related_product,
                    "relation_type": relation_type,
                    "numeric_ids": numeric_ids
                })
        
        return related_products

```

---

# ..\..\core\engine.py
## File: ..\..\core\engine.py

```py
# ..\..\core\engine.py
# nlp_bot_engine/core/engine.py

import os
import re
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

from .config import BotConfig
from .data_manager import DataManager
from ..nlp.processor import NLPProcessor
from ..nlp.intent_analyzer import IntentAnalyzer
from ..nlp.entity_extractor import EntityExtractor
from ..nlp.context_manager import ContextManager
from ..dialog.response_generator import ResponseGenerator

logger = logging.getLogger(__name__)

class AdvancedBotEngine:
    """
    Avancerad botmotor med NLP-förmågor för att hantera komplexa och vaga frågor.
    Integrerar olika komponenter för språkförståelse, intentionsanalys och dynamisk svarshantering.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialisera botmotorn med konfiguration
        
        Args:
            config: Konfigurationsparametrar (använder standardvärden om None)
        """
        # Ladda konfiguration
        self.config = BotConfig(config or {})
        
        # Initiera datahanterare för index och produktdata
        self.data_manager = DataManager(self.config)
        
        # Initiera NLP-komponenter
        self.nlp_processor = NLPProcessor(self.config)
        self.intent_analyzer = IntentAnalyzer(self.config, self.nlp_processor)
        self.entity_extractor = EntityExtractor(self.config, self.nlp_processor)
        self.context_manager = ContextManager(self.config)
        
        # Initiera svarsgenereringen
        self.response_generator = ResponseGenerator(self.config)
        
        # Statistik och loggning
        self.stats = {
            "total_queries": 0,
            "successful_queries": 0,
            "command_queries": 0,
            "natural_language_queries": 0,
            "ambiguous_queries": 0,
            "failures": 0,
            "start_time": datetime.now()
        }
        
        # Historik för konversationer
        self.query_history = []
        
        # Cacheminne för tidigare svar för att förbättra prestanda
        self.response_cache = {}
        
        logger.info("AdvancedBotEngine initialiserad")
        
    def process_input(self, user_input: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Huvudingång för all användarinmatning. Hanterar både direkta kommandon och naturligt språk.
        
        Args:
            user_input: Användarens fråga eller kommando
            context: Kontextinformation som aktiv produkt, användarhistorik, etc.
            
        Returns:
            Svarsobjekt med statusuppdatering och formaterad text
        """
        # Standardisera indata
        user_input = user_input.strip()
        context = context or {}
        
        # Uppdatera statistik
        self.stats["total_queries"] += 1
        
        # Spara till historik
        query_entry = {
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "context": context.copy()  # Kopiera för att undvika referensproblem
        }
        self.query_history.append(query_entry)
        
        # Uppdatera kontext med historik
        if "query_history" not in context:
            context["query_history"] = []
        context["query_history"].append(user_input)
        
        # Kolla för strukturerade kommandon först
        command_match = re.match(r'^(-[tcfs])\s+(\S+)(.*)$', user_input)
        if command_match:
            self.stats["command_queries"] += 1
            command, product_id, params = command_match.groups()
            return self.execute_command(command, product_id, params.strip(), context)
        
        # Om inte kommando, vidare till NLP-processning för naturligt språk
        self.stats["natural_language_queries"] += 1
        return self.process_natural_language(user_input, context)
    
    def execute_command(self, command: str, product_id: str, params: str = "", 
                       context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Utför ett specifikt botkommando
        
        Args:
            command: Kommandotyp (-t, -c, -s, -f)
            product_id: Produktens ID
            params: Extra parametrar
            context: Kontextinformation
            
        Returns:
            Svarsobjekt med status och resultat
        """
        try:
            # Validera produkt-ID
            if not self.data_manager.validate_product_id(product_id):
                return {
                    "status": "error",
                    "message": f"Ogiltig produkt: {product_id}",
                    "command": command,
                    "product_id": product_id
                }
            
            # Sätt aktiv produkt i kontext
            if context is None:
                context = {}
            context["active_product_id"] = product_id
            
            # Kolla om vi har resultatet i cacheminnet
            cache_key = f"{command}:{product_id}:{params}"
            if cache_key in self.response_cache:
                logger.debug(f"Hittade cacheminne för {cache_key}")
                return self.response_cache[cache_key]
            
            # Utför kommandot
            if command == "-t":
                result = self.data_manager.get_technical_specs(product_id, params)
            elif command == "-c":
                result = self.data_manager.get_compatibility_info(product_id, params)
            elif command == "-s":
                result = self.data_manager.get_product_summary(product_id, params)
            elif command == "-f":
                result = self.data_manager.get_full_info(product_id, params)
            else:
                return {
                    "status": "error",
                    "message": f"Okänt kommando: {command}",
                    "command": command,
                    "product_id": product_id
                }
            
            # Generera ett rikt formaterat svar
            response = {
                "status": "success",
                "command": command,
                "product_id": product_id,
                "params": params,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            
            # Lägg till formaterad text från svarsgenereringen
            response_type = command[1]  # Extrahera t/c/s/f
            response["formatted_text"] = self.response_generator.format_command_response(
                response_type, product_id, result, context
            )
            
            # Cacha resultatet
            self.response_cache[cache_key] = response
            
            # Uppdatera statistik
            self.stats["successful_queries"] += 1
            
            return response
            
        except Exception as e:
            logger.error(f"Fel vid exekvering av kommando {command} för {product_id}: {str(e)}")
            self.stats["failures"] += 1
            return {
                "status": "error",
                "message": f"Ett fel uppstod: {str(e)}",
                "command": command,
                "product_id": product_id
            }
    
    def process_natural_language(self, query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Processera naturligt språk med avancerad NLP och kontextförstående
        
        Args:
            query: Användarens fråga
            context: Kontextinformation
            
        Returns:
            Svarsobjekt med analysresultat och formaterad text
        """
        try:
            # Initiera kontext om den saknas
            context = context or {}
            
            # 1. Utför NLP-förbehandling
            processed_text = self.nlp_processor.preprocess(query)
            
            # 2. Analysera kontext och lös referenser
            context_analysis = self.context_manager.analyze_context(query, context)
            
            # 3. Extrahera entiteter (produkter, egenskaper, etc.)
            entities = self.entity_extractor.extract_entities(processed_text, context)
            
            # 4. Analysera intention (vad användaren vill göra)
            intent_analysis = self.intent_analyzer.analyze_intent(processed_text, entities, context)
            
            # 5. Kombinera all information i analysobjekt
            analysis = {
                "original_query": query,
                "processed_text": processed_text,
                "entities": entities,
                "intents": intent_analysis["intents"],
                "primary_intent": intent_analysis["primary_intent"],
                "confidence": intent_analysis["confidence"],
                "context_references": context_analysis.get("references", []),
                "resolved_entities": context_analysis.get("resolved_entities", {})
            }
            
            # 6. Hantera osäkerhet om konfidensen är låg
            if intent_analysis["confidence"] < self.config.min_confidence:
                return self.handle_low_confidence(analysis, context)
                
            # 7. Hämta produktinformation eller utför sökning baserat på analys
            result = self.execute_intent(analysis, context)
            
            # 8. Generera anpassat svar baserat på intention och resultat
            response = {
                "status": "success" if result.get("status") != "error" else "error",
                "query_type": "natural_language",
                "timestamp": datetime.now().isoformat(),
                "analysis": analysis,
                "result": result
            }
            
            # Generera formaterad text från svarsgenereringen
            response["formatted_text"] = self.response_generator.generate_nl_response(
                analysis, result, context
            )
            
            # Uppdatera statistik
            if response["status"] == "success":
                self.stats["successful_queries"] += 1
            else:
                self.stats["failures"] += 1
            
            return response
            
        except Exception as e:
            logger.error(f"Fel vid processning av naturligt språk: {str(e)}")
            self.stats["failures"] += 1
            return {
                "status": "error",
                "message": f"Ett fel uppstod vid analys av din fråga: {str(e)}",
                "query": query
            }
    
    def handle_low_confidence(self, analysis: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Hantera osäkerhetsfall där botens konfidens är låg
        
        Args:
            analysis: Analysresultat från NLP-stegen
            context: Kontextinformation
            
        Returns:
            Svarsobjekt med klargörande frågor eller bästa gissning
        """
        self.stats["ambiguous_queries"] += 1
        
        # Extracta huvudintention och konfidens
        primary_intent = analysis["primary_intent"]
        confidence = analysis["confidence"]
        
        # Mycket låg konfidens - be om förtydligande
        if confidence < 0.4:
            # Generera klargörande frågor
            clarification_questions = self.generate_clarification_questions(analysis, context)
            
            return {
                "status": "needs_clarification",
                "query_type": "clarification_request",
                "analysis": analysis,
                "clarification_questions": clarification_questions,
                "formatted_text": self.response_generator.format_clarification_request(
                    analysis, clarification_questions, context
                )
            }
        
        # Medelhög konfidens - gör en kvalificerad gissning men informera användaren
        return {
            "status": "low_confidence",
            "query_type": "best_guess",
            "analysis": analysis,
            "result": self.execute_intent(analysis, context, ignore_confidence=True),
            "confidence": confidence,
            "alternative_intents": analysis["intents"][:3],  # Top 3 alternativa intentioner
            "formatted_text": self.response_generator.format_low_confidence_response(
                analysis, self.execute_intent(analysis, context, ignore_confidence=True), context
            )
        }
    
    def generate_clarification_questions(self, analysis: Dict[str, Any], context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generera lämpliga uppföljningsfrågor baserat på osäkerheten
        
        Args:
            analysis: Analysresultat från NLP-stegen
            context: Kontextinformation
            
        Returns:
            Lista med klargörande frågor och deras alternativ
        """
        questions = []
        
        # Kolla om vi har produktkandidater men är osäkra
        product_entities = [e for e in analysis["entities"] if e["type"] == "PRODUCT"]
        if product_entities and len(product_entities) > 1:
            # Flera produktkandidater - be användaren välja
            options = [{"id": e.get("product_id", ""), "name": e["text"]} for e in product_entities[:4]]
            questions.append({
                "type": "product_selection",
                "text": "Vilken av dessa produkter menar du?",
                "options": options
            })
        elif not product_entities and "PRODUCT" in analysis["entities"]:
            # Vag produktbeskrivning - föreslå sökningar
            suggested_searches = self.data_manager.suggest_products(analysis["original_query"])
            if suggested_searches:
                options = [{"id": p["product_id"], "name": p["name"]} for p in suggested_searches[:4]]
                questions.append({
                    "type": "product_suggestion",
                    "text": "Jag är inte säker på vilken produkt du menar. Är det någon av dessa?",
                    "options": options
                })
        
        # Kolla om intentionen är oklar
        if not analysis["primary_intent"] or analysis["confidence"] < 0.3:
            # Oklart vad användaren vill veta - ge alternativ
            questions.append({
                "type": "intent_selection",
                "text": "Vad vill du veta om produkten?",
                "options": [
                    {"id": "technical", "name": "Tekniska specifikationer"},
                    {"id": "compatibility", "name": "Kompatibilitetsinformation"},
                    {"id": "summary", "name": "Allmän produktinformation"},
                    {"id": "search", "name": "Sök efter produkter"}
                ]
            })
        
        # Om inga specifika frågor kunde genereras, ge en generell uppmaning
        if not questions:
            questions.append({
                "type": "general_clarification",
                "text": "Jag förstod inte riktigt din fråga. Kan du omformulera den eller vara mer specifik?",
                "options": []
            })
        
        return questions
    
    def execute_intent(self, analysis: Dict[str, Any], context: Dict[str, Any], 
                      ignore_confidence: bool = False) -> Dict[str, Any]:
        """
        Utför den identifierade intentionen baserat på analys
        
        Args:
            analysis: Analysresultat från NLP-stegen
            context: Kontextinformation
            ignore_confidence: Om True, utför även vid låg konfidens
            
        Returns:
            Resultat från den intentionsbaserade åtgärden
        """
        # Om konfidensen är för låg och vi inte ignorerar det, returnera ett tomt resultat
        if not ignore_confidence and analysis["confidence"] < self.config.min_confidence:
            return {"status": "low_confidence", "message": "Osäker tolkning av frågan"}
        
        # Identifiera huvudintention
        intent = analysis["primary_intent"]
        
        # Hämta produkt-ID om det finns i analysen
        product_id = None
        for entity in analysis["entities"]:
            if entity["type"] == "PRODUCT" and entity.get("product_id"):
                product_id = entity["product_id"]
                break
        
        # Alternativt, använd aktiv produkt från kontext
        if not product_id and context.get("active_product_id"):
            product_id = context["active_product_id"]
        
        # Utför intentionen om vi har en produkt
        if product_id:
            if intent == "technical":
                return self.data_manager.get_technical_specs(product_id)
            elif intent == "compatibility":
                return self.data_manager.get_compatibility_info(product_id)
            elif intent == "summary":
                return self.data_manager.get_product_summary(product_id)
            elif intent == "search":
                # Sök efter relaterade produkter
                search_terms = " ".join([e["text"] for e in analysis["entities"] if e["type"] != "PRODUCT"])
                return self.data_manager.search_products(search_terms)
            else:
                # Default till sammanfattning om intentionen är oklar
                return self.data_manager.get_product_summary(product_id)
        
        # Om vi inte har en produkt men intentionen är sökning
        if intent == "search" or not product_id:
            search_query = analysis["processed_text"]
            return self.data_manager.search_products(search_query)
        
        # Fallback om inget matchade
        return {
            "status": "error",
            "message": "Kunde inte utföra någon åtgärd baserat på din fråga. Var mer specifik eller ange en produkt."
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Hämta statistik om botens användning
        
        Returns:
            Statistikobjekt med användningsdata
        """
        stats = self.stats.copy()
        stats["uptime_seconds"] = (datetime.now() - stats["start_time"]).total_seconds()
        
        # Beräkna framgångsfrekvens
        if stats["total_queries"] > 0:
            stats["success_rate"] = stats["successful_queries"] / stats["total_queries"]
        else:
            stats["success_rate"] = 0
            
        return stats
    
    def learn_from_interaction(self, query: str, response: Dict[str, Any], 
                              user_feedback: Dict[str, Any] = None) -> None:
        """
        Lär från interaktioner för att förbättra framtida svar
        
        Args:
            query: Ursprunglig fråga
            response: Botens svar
            user_feedback: Användarens feedback (t.ex. var svaret hjälpsamt)
        """
        # Implementera lärande mekanismer här
        pass
```

---

# ..\..\dialog\response_generator.py
## File: ..\..\dialog\response_generator.py

```py
# ..\..\dialog\response_generator.py
# nlp_bot_engine/dialog/response_generator.py

import logging
import re
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

from ..core.config import BotConfig
from .templates import ResponseTemplates

logger = logging.getLogger(__name__)

class ResponseGenerator:
    """
    Genererar dynamiska svar baserat på intention, analys och resultat.
    Anpassar detaljnivå och formulering baserat på användarkontext.
    """
    
    def __init__(self, config: BotConfig):
        """
        Initialisera svarsgeneratorn
        
        Args:
            config: Konfigurationsobjekt
        """
        self.config = config
        self.templates = ResponseTemplates()
    
    def format_command_response(self, command_type: str, product_id: str, 
                               result: Dict[str, Any], context: Dict[str, Any]) -> str:
        """
        Formatterar svar för en kommandoförfrågan
        
        Args:
            command_type: Typen av kommando (t, c, s, f)
            product_id: Produktens ID
            result: Resultatet från kommandot
            context: Kontextinformation
            
        Returns:
            Formaterat svar som text
        """
        # Om resultatet har en status som inte är success, returnera felmeddelandet
        if result.get("status") != "success":
            return self.format_error_response(result.get("message", "Ett fel uppstod"))
        
        # Om resultatet har förformaterad text, använd den
        if "formatted_text" in result:
            return result["formatted_text"]
        
        # Annars, använd mallar baserat på kommandotyp
        if command_type == "t":
            template = self.config.response_templates.get("technical")
            return self.fill_template(template, {
                "product_name": self.get_product_name(product_id),
                "product_id": product_id,
                "specifications": result.get("formatted_text", "Ingen teknisk information tillgänglig")
            })
            
        elif command_type == "c":
            template = self.config.response_templates.get("compatibility")
            return self.fill_template(template, {
                "product_name": self.get_product_name(product_id),
                "product_id": product_id,
                "compatibility": result.get("formatted_text", "Ingen kompatibilitetsinformation tillgänglig")
            })
            
        elif command_type == "s":
            template = self.config.response_templates.get("summary")
            return self.fill_template(template, {
                "product_name": self.get_product_name(product_id),
                "product_id": product_id,
                "description": result.get("summary", {}).get("description", ""),
                "specifications": self.format_key_specifications(result.get("summary", {}).get("key_specifications", [])),
                "compatibility": self.format_key_compatibility(result.get("summary", {}).get("key_compatibility", []))
            })
            
        elif command_type == "f":
            # Full info är redan formaterad
            return result.get("content", "Ingen fullständig information tillgänglig")
        
        # Fallback
        return result.get("formatted_text", "Inget resultat att visa")
    
    def generate_nl_response(self, analysis: Dict[str, Any], result: Dict[str, Any], 
                            context: Dict[str, Any]) -> str:
        """
        Generera svar för naturligt språkförfrågningar
        
        Args:
            analysis: Analysresultat från NLP-stegen
            result: Resultat från intentionsutförande
            context: Kontextinformation
            
        Returns:
            Genererat svar
        """
        # Om resultatet har en status som inte är success, returnera felmeddelandet
        if result.get("status") == "error":
            return self.format_error_response(result.get("message", "Ett fel uppstod"))
        
        # Identifiera huvudintention och anpassa svarsstil
        primary_intent = analysis.get("primary_intent")
        
        # Kontrollera expertisgrad för att anpassa detaljnivå
        expertise_level = self.infer_expertise_level(context)
        
        # Hämta entiteter för att personalisera svaret
        entities = analysis.get("entities", [])
        
        # Identifiera eventuell produkt i entiteter
        product_id = None
        for entity in entities:
            if entity.get("type") == "PRODUCT" and entity.get("product_id"):
                product_id = entity.get("product_id")
                break
        
        # Om ingen produkt hittades i entiteter, kontrollera resultat och kontext
        if not product_id:
            product_id = result.get("product_id") or context.get("active_product_id")
        
        # Generera svar baserat på intention
        if primary_intent == "technical":
            return self.generate_technical_response(result, product_id, expertise_level)
            
        elif primary_intent == "compatibility":
            return self.generate_compatibility_response(result, product_id, expertise_level)
            
        elif primary_intent == "summary":
            return self.generate_summary_response(result, product_id, expertise_level)
            
        elif primary_intent == "search":
            return self.generate_search_response(result, analysis.get("original_query", ""), expertise_level)
        
        # Om resultatet har förformaterad text men vi inte kunde identifiera intention
        if "formatted_text" in result:
            return result["formatted_text"]
        
        # Fallback till generiskt svar
        return self.templates.get_template("generic").format(
            query=analysis.get("original_query", ""),
               timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           )
   
    def format_clarification_request(self, analysis: Dict[str, Any], 
                                    questions: List[Dict[str, Any]], 
                                    context: Dict[str, Any]) -> str:
        """
        Formatera en förfrågan om förtydligande när botten är osäker
        
        Args:
            analysis: Analysresultat från NLP-stegen
            questions: Lista med klargörande frågor
            context: Kontextinformation
            
        Returns:
            Formaterad förfrågan om förtydligande
        """
        # Om inga frågor, använd ett generiskt förtydligande
        if not questions:
            return self.templates.get_template("generic_clarification").format(
                query=analysis.get("original_query", "")
            )
        
        # Formatera den första frågan
        question = questions[0]
        question_type = question.get("type", "")
        
        if question_type == "product_selection":
            options_text = "\n".join([f"- {opt['name']} (Art.nr: {opt['id']})" 
                                        for opt in question.get("options", [])])
            
            return self.templates.get_template("product_clarification").format(
                question=question.get("text", "Vilken produkt menar du?"),
                options=options_text
            )
            
        elif question_type == "intent_selection":
            options_text = "\n".join([f"- {opt['name']}" 
                                        for opt in question.get("options", [])])
            
            return self.templates.get_template("intent_clarification").format(
                question=question.get("text", "Vad vill du veta?"),
                options=options_text
            )
            
        elif question_type == "general_clarification":
            return self.templates.get_template("generic_clarification").format(
                query=analysis.get("original_query", "")
            )
        
        # Fallback
        return self.templates.get_template("generic_clarification").format(
            query=analysis.get("original_query", "")
        )
    
    def format_low_confidence_response(self, analysis: Dict[str, Any], result: Dict[str, Any], 
                                        context: Dict[str, Any]) -> str:
        """
        Formatera svar när botten har låg konfidens men ändå gör en kvalificerad gissning
        
        Args:
            analysis: Analysresultat från NLP-stegen
            result: Resultatet från intentionsutförandet
            context: Kontextinformation
            
        Returns:
            Formaterat svar med reservationer
        """
        # Få originalsvar som skulle genererats med full konfidens
        original_response = self.generate_nl_response(analysis, result, context)
        
        # Lägg till en inledande text som indikerar osäkerhet
        confidence_disclaimer = self.templates.get_template("low_confidence_disclaimer").format(
            intent=self.get_intent_display_name(analysis.get("primary_intent", ""))
        )
        
        # Lägg till alternativa intentioner om sådana finns
        alternatives = ""
        if len(analysis.get("intents", [])) > 1:
            alt_intents = analysis.get("intents")[1:3]  # Ta upp till två alternativ
            alt_names = [self.get_intent_display_name(i["intent"]) for i in alt_intents]
            
            alternatives = self.templates.get_template("alternative_intents").format(
                alternatives=", ".join(alt_names)
            )
        
        return f"{confidence_disclaimer}\n\n{original_response}\n\n{alternatives}"
    
    def generate_technical_response(self, result: Dict[str, Any], product_id: str, 
                                    expertise_level: str) -> str:
        """
        Generera svar för tekniska frågor med anpassad detaljnivå
        
        Args:
            result: Resultatdata
            product_id: Produktens ID
            expertise_level: Användarens expertisgrad
            
        Returns:
            Formaterad teknisk information
        """
        # Om resultatet har förformaterad text, anpassa den efter expertisgrad
        if "formatted_text" in result:
            formatted_text = result["formatted_text"]
            
            # För experter, behåll all detaljerad information
            if expertise_level == "expert":
                return formatted_text
            
            # För mellanliggande nivå, behåll det mesta men förenkla vissa delar
            elif expertise_level == "intermediate":
                # Till exempel, ta bort mycket tekniska specifikationer
                return formatted_text
            
            # För nybörjare, förenkla och förtydliga
            else:
                # Lägg till förklarande text och förenkla terminologi
                intro = self.templates.get_template("technical_beginner_intro").format(
                    product_name=self.get_product_name(product_id)
                )
                return f"{intro}\n\n{formatted_text}"
        
        # Om ingen förformaterad text, generera från specs
        specs = result.get("specs", [])
        specs_by_category = result.get("specs_by_category", {})
        
        if not specs and not specs_by_category:
            return self.templates.get_template("no_technical_info").format(
                product_name=self.get_product_name(product_id)
            )
        
        # Om vi har kategorier, använd dem
        if specs_by_category:
            formatted_sections = [f"# Tekniska specifikationer för {self.get_product_name(product_id)}", ""]
            
            formatted_sections.append(f"**Artikelnummer:** {product_id}")
            formatted_sections.append("")
            
            # Sortera kategorier för att få viktiga först
            priority_categories = ["Dimensioner", "Mått", "Grundläggande", "Material", "Vikt"]
            categories = list(specs_by_category.keys())
            
            # Sortera så att prioriterade kategorier kommer först
            sorted_categories = sorted(categories, 
                                        key=lambda x: (
                                            0 if x in priority_categories else 
                                            priority_categories.index(x) if x in priority_categories else 
                                            999
                                        ))
            
            # Lägg till varje kategori
            for category in sorted_categories:
                category_specs = specs_by_category[category]
                
                # För nybörjare, visa bara viktiga kategorier och begränsad mängd specs
                if expertise_level == "beginner" and category not in priority_categories and len(category_specs) > 2:
                    category_specs = category_specs[:2]  # Bara visa de första två
                
                formatted_sections.append(f"## {category}")
                
                for spec in category_specs:
                    name = spec.get("name", "")
                    value = spec.get("raw_value", "")
                    unit = spec.get("unit", "")
                    
                    if name and value:
                        spec_line = f"- **{name}:** {value}"
                        if unit and unit not in value:
                            spec_line += f" {unit}"
                        formatted_sections.append(spec_line)
                
                formatted_sections.append("")  # Tomrad mellan kategorier
            
            # För nybörjare, lägg till förklarande text
            if expertise_level == "beginner":
                formatted_sections.insert(2, self.templates.get_template("technical_beginner_intro").format(
                    product_name=self.get_product_name(product_id)
                ))
                formatted_sections.insert(3, "")  # Tomrad
            
            return "\n".join(formatted_sections)
        
        # Fallback till enkel listning av specs
        formatted_sections = [f"# Tekniska specifikationer för {self.get_product_name(product_id)}", ""]
        formatted_sections.append(f"**Artikelnummer:** {product_id}")
        formatted_sections.append("")
        
        for spec in specs:
            name = spec.get("name", "")
            value = spec.get("raw_value", "")
            unit = spec.get("unit", "")
            
            if name and value:
                spec_line = f"- **{name}:** {value}"
                if unit and unit not in value:
                    spec_line += f" {unit}"
                formatted_sections.append(spec_line)
        
        return "\n".join(formatted_sections)
    
    def generate_compatibility_response(self, result: Dict[str, Any], product_id: str, 
                                        expertise_level: str) -> str:
        """
        Generera svar för kompatibilitetsfrågor med anpassad detaljnivå
        
        Args:
            result: Resultatdata
            product_id: Produktens ID
            expertise_level: Användarens expertisgrad
            
        Returns:
            Formaterad kompatibilitetsinformation
        """
        # Om resultatet har förformaterad text, använd den som bas
        if "formatted_text" in result:
            formatted_text = result["formatted_text"]
            
            # Experter får allt som det är
            if expertise_level == "expert":
                return formatted_text
            
            # För nybörjare och mellanliggande, lägg till förklarande text
            intro = self.templates.get_template("compatibility_intro").format(
                product_name=self.get_product_name(product_id)
            )
            
            # För nybörjare, förenkla texten något
            if expertise_level == "beginner":
                # Ersätt tekniska termer med enklare förklaringar
                formatted_text = self.simplify_technical_terms(formatted_text)
            
            return f"{intro}\n\n{formatted_text}"
        
        # Om ingen förformaterad text, generera från relationer
        relations = result.get("relations", [])
        relations_by_type = result.get("relations_by_type", {})
        
        if not relations and not relations_by_type:
            return self.templates.get_template("no_compatibility_info").format(
                product_name=self.get_product_name(product_id)
            )
        
        # Om vi har relationstyper, använd dem
        if relations_by_type:
            formatted_sections = [f"# Kompatibilitetsinformation för {self.get_product_name(product_id)}", ""]
            
            formatted_sections.append(f"**Artikelnummer:** {product_id}")
            formatted_sections.append("")
            
            # Definiera visningsnamn för relationstyper
            relation_display = {
                "direct": "Kompatibel med",
                "fits": "Passar till",
                "requires": "Kräver",
                "recommended": "Rekommenderas med",
                "designed_for": "Designad för",
                "accessory": "Tillbehör till",
                "replacement": "Ersätter",
                "replaced_by": "Ersätts av",
                "not_compatible": "Ej kompatibel med"
            }
            
            # Lägg till varje relationstyp
            for rel_type, relations in relations_by_type.items():
                display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
                formatted_sections.append(f"## {display_name}")
                
                for relation in relations:
                    related_product = relation.get("related_product", "")
                    numeric_ids = relation.get("numeric_ids", [])
                    
                    if related_product:
                        relation_text = f"- {related_product}"
                        if numeric_ids:
                            relation_text += f" (Art.nr: {numeric_ids[0]})"
                        formatted_sections.append(relation_text)
                
                formatted_sections.append("")  # Tomrad mellan kategorier
            
            # För nybörjare, lägg till förklarande text
            if expertise_level in ["beginner", "intermediate"]:
                formatted_sections.insert(2, self.templates.get_template("compatibility_intro").format(
                    product_name=self.get_product_name(product_id)
                ))
                formatted_sections.insert(3, "")  # Tomrad
            
            return "\n".join(formatted_sections)
        
        # Fallback till enkel listning av relationer
        formatted_sections = [f"# Kompatibilitetsinformation för {self.get_product_name(product_id)}", ""]
        formatted_sections.append(f"**Artikelnummer:** {product_id}")
        formatted_sections.append("")
        
        # Gruppera efter relationstyp
        grouped_relations = {}
        for relation in relations:
            rel_type = relation.get("relation_type", "other")
            if rel_type not in grouped_relations:
                grouped_relations[rel_type] = []
            grouped_relations[rel_type].append(relation)
        
        # Definiera visningsnamn för relationstyper
        relation_display = {
            "direct": "Kompatibel med",
            "fits": "Passar till",
            "requires": "Kräver",
            "recommended": "Rekommenderas med"
        }
        
        # Lägg till varje relationstyp
        for rel_type, rels in grouped_relations.items():
            display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
            formatted_sections.append(f"## {display_name}")
            
            for relation in rels:
                related_product = relation.get("related_product", "")
                if related_product:
                    formatted_sections.append(f"- {related_product}")
            
            formatted_sections.append("")  # Tomrad mellan kategorier
        
        return "\n".join(formatted_sections)
    
    def generate_summary_response(self, result: Dict[str, Any], product_id: str, 
                                    expertise_level: str) -> str:
        """
        Generera sammanfattningssvar med anpassad detaljnivå
        
        Args:
            result: Resultatdata
            product_id: Produktens ID
            expertise_level: Användarens expertisgrad
            
        Returns:
            Formaterad produktsammanfattning
        """
        # Om resultatet har förformaterad text, använd den
        if "formatted_text" in result:
            return result["formatted_text"]
        
        # Om vi har ett summary-objekt, formatera det
        summary = result.get("summary", {})
        
        if not summary:
            return self.templates.get_template("no_summary_info").format(
                product_name=self.get_product_name(product_id)
            )
        
        formatted_sections = []
        
        # Lägg till produktnamn och ID
        product_name = summary.get("product_name", self.get_product_name(product_id))
        formatted_sections.append(f"# {product_name}")
        formatted_sections.append("")
        formatted_sections.append(f"**Artikelnummer:** {product_id}")
        
        # Lägg till identifierare
        id_lines = []
        for id_type, values in summary.get("identifiers", {}).items():
            if values:
                id_lines.append(f"**{id_type}:** {', '.join(values)}")
        
        if id_lines:
            formatted_sections.extend(id_lines)
            formatted_sections.append("")  # Tomrad
        
        # Lägg till beskrivning
        if summary.get("description"):
            formatted_sections.append("## Beskrivning")
            formatted_sections.append(summary["description"])
            formatted_sections.append("")  # Tomrad
        
        # Lägg till viktiga specifikationer
        if summary.get("key_specifications"):
            formatted_sections.append("## Viktiga specifikationer")
            
            # Gruppera efter kategori för bättre struktur
            specs_by_category = {}
            for spec in summary["key_specifications"]:
                category = spec.get("category", "Övrigt")
                if category not in specs_by_category:
                    specs_by_category[category] = []
                specs_by_category[category].append(spec)
            
            # För experter och mellanliggande, visa kategoriserade specifikationer
            if expertise_level in ["expert", "intermediate"] and len(specs_by_category) > 1:
                for category, specs in specs_by_category.items():
                    formatted_sections.append(f"### {category}")
                    
                    for spec in specs:
                        name = spec.get("name", "")
                        value = spec.get("value", "")
                        unit = spec.get("unit", "")
                        if name and value:
                            spec_text = f"- **{name}:** {value}"
                            if unit and unit not in value:
                                spec_text += f" {unit}"
                            formatted_sections.append(spec_text)
                    
                    formatted_sections.append("")  # Tomrad mellan kategorier
            else:
                # För nybörjare, visa platt lista utan kategorier
                for spec in summary["key_specifications"]:
                    name = spec.get("name", "")
                    value = spec.get("value", "")
                    unit = spec.get("unit", "")
                    if name and value:
                        spec_text = f"- **{name}:** {value}"
                        if unit and unit not in value:
                            spec_text += f" {unit}"
                        formatted_sections.append(spec_text)
                
                formatted_sections.append("")  # Tomrad
        
        # Lägg till kompatibilitetsinformation
        if summary.get("key_compatibility"):
            formatted_sections.append("## Kompatibilitet")
            
            # Gruppera efter relationstyp
            compat_by_type = {}
            for relation in summary["key_compatibility"]:
                rel_type = relation.get("type", "other")
                if rel_type not in compat_by_type:
                    compat_by_type[rel_type] = []
                compat_by_type[rel_type].append(relation)
            
            # Definiera visningsnamn för relationstyper
            relation_display = {
                "direct": "Kompatibel med",
                "fits": "Passar till",
                "requires": "Kräver",
                "recommended": "Rekommenderas med",
                "designed_for": "Designad för",
                "accessory": "Tillbehör till"
            }
            
            # Experter får mer strukturerad information
            if expertise_level in ["expert", "intermediate"] and len(compat_by_type) > 1:
                for rel_type, relations in compat_by_type.items():
                    display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
                    formatted_sections.append(f"### {display_name}")
                    
                    for relation in relations:
                        related_product = relation.get("related_product", "")
                        if related_product:
                            compat_text = f"- {related_product}"
                            if relation.get("numeric_ids"):
                                compat_text += f" (Art.nr: {relation['numeric_ids'][0]})"
                            formatted_sections.append(compat_text)
                    
                    formatted_sections.append("")  # Tomrad mellan kategorier
            else:
                # För nybörjare, visa platt lista med beskrivande text
                for relation in summary["key_compatibility"]:
                    rel_type = relation.get("type", "other")
                    display_name = relation_display.get(rel_type, "")
                    related_product = relation.get("related_product", "")
                    
                    if related_product:
                        if display_name:
                            compat_text = f"- {display_name}: {related_product}"
                        else:
                            compat_text = f"- {related_product}"
                            
                        if relation.get("numeric_ids"):
                            compat_text += f" (Art.nr: {relation['numeric_ids'][0]})"
                            
                        formatted_sections.append(compat_text)
                
                formatted_sections.append("")  # Tomrad
        
        return "\n".join(formatted_sections)
    
    def generate_search_response(self, result: Dict[str, Any], query: str, 
                                expertise_level: str) -> str:
        """
        Generera svar för sökfrågor
        
        Args:
            result: Sökresultat
            query: Ursprunglig sökfråga
            expertise_level: Användarens expertisgrad
            
        Returns:
            Formaterad sökresultatlista
        """
        # Om resultatet har förformaterad text, använd den
        if "formatted_text" in result:
            return result["formatted_text"]
        
        # Hämta matchningar
        matches = result.get("matches", [])
        
        if not matches:
            return self.templates.get_template("no_search_results").format(
                query=query
            )
        
        # Formatera sökresultaten
        formatted_sections = [f"# Sökresultat för '{query}'", ""]
        
        # För experter, visa även matchningspoäng
        if expertise_level == "expert":
            formatted_sections.append("| Produkt | Artikelnummer | Matchningspoäng |")
            formatted_sections.append("|---------|---------------|-----------------|")
            
            for match in matches:
                name = match.get("name", "")
                product_id = match.get("product_id", "")
                score = match.get("score", 0)
                
                formatted_sections.append(f"| {name} | {product_id} | {score:.2f} |")
        else:
            # För vanliga användare, enklare lista
            for i, match in enumerate(matches, 1):
                name = match.get("name", "")
                product_id = match.get("product_id", "")
                
                formatted_sections.append(f"{i}. **{name}** (Art.nr: {product_id})")
        
        # Lägg till instruktioner om hur man får mer info
        formatted_sections.append("")
        formatted_sections.append("Använd kommandot `-s <artikelnr>` för att se mer information om en produkt.")
        
        return "\n".join(formatted_sections)
    
    def format_error_response(self, error_message: str) -> str:
        """
        Formatera ett felmeddelande
        
        Args:
            error_message: Felmeddelandet
            
        Returns:
            Formaterat felmeddelande
        """
        return self.templates.get_template("error").format(
            error=error_message
        )
    
    def fill_template(self, template: str, values: Dict[str, str]) -> str:
        """
        Fyll i en mall med värden
        
        Args:
            template: Mallen att använda
            values: Värden att fylla i
            
        Returns:
            Ifylld mall
        """
        try:
            return template.format(**values)
        except KeyError as e:
            logger.warning(f"Saknat värde i mall: {str(e)}")
            # Fallback - ersätt saknade värden med tomma strängar
            for key in str(e).strip("'"):
                if key not in values:
                    values[key] = ""
            return template.format(**values)
        except Exception as e:
            logger.error(f"Fel vid ifyllning av mall: {str(e)}")
            return template  # Returnera oförändrad mall vid fel
    
    def format_key_specifications(self, specs: List[Dict[str, Any]]) -> str:
        """
        Formatera nyckelspecifikationer
        
        Args:
            specs: Lista med specifikationer
            
        Returns:
            Formaterad text
        """
        if not specs:
            return ""
        
        formatted_lines = ["## Viktiga specifikationer", ""]
        
        for spec in specs:
            name = spec.get("name", "")
            value = spec.get("value", "")
            unit = spec.get("unit", "")
            
            if name and value:
                spec_text = f"- **{name}:** {value}"
                if unit and unit not in value:
                    spec_text += f" {unit}"
                formatted_lines.append(spec_text)
        
        return "\n".join(formatted_lines)
    
    def format_key_compatibility(self, compatibility: List[Dict[str, Any]]) -> str:
        """
        Formatera nyckelkompatibilitetsinformation
        
        Args:
            compatibility: Lista med kompatibilitetsrelationer
            
        Returns:
            Formaterad text
        """
        if not compatibility:
            return ""
        
        formatted_lines = ["## Kompatibilitet", ""]
        
        # Gruppera efter relationstyp
        grouped = {}
        for relation in compatibility:
            rel_type = relation.get("type", "other")
            if rel_type not in grouped:
                grouped[rel_type] = []
            grouped[rel_type].append(relation)
        
        # Definiera visningsnamn för relationstyper
        relation_display = {
            "direct": "Kompatibel med",
            "fits": "Passar till",
            "requires": "Kräver",
            "recommended": "Rekommenderas med",
            "designed_for": "Designad för",
            "accessory": "Tillbehör till"
        }
        
        # Formatera för varje relationstyp
        for rel_type, relations in grouped.items():
            display_name = relation_display.get(rel_type, rel_type.replace("_", " ").title())
            
            if len(grouped) > 1:  # Om fler än en typ, använd underrubriker
                formatted_lines.append(f"### {display_name}")
            
            for relation in relations:
                related_product = relation.get("related_product", "")
                numeric_ids = relation.get("numeric_ids", [])
                
                if related_product:
                    relation_text = f"- {related_product}"
                    if numeric_ids:
                        relation_text += f" (Art.nr: {numeric_ids[0]})"
                    formatted_lines.append(relation_text)
            
            formatted_lines.append("")  # Tomrad mellan kategorier
        
        return "\n".join(formatted_lines)
    
    def get_product_name(self, product_id: str) -> str:
        """
        Hämta produktnamn för ett produkt-ID
        
        Args:
            product_id: Produktens ID
            
        Returns:
            Produktnamn eller generisk text
        """
        # Detta skulle normalt använda någon form av produktdatabas
        # men här returnerar vi ett generiskt namn
        return f"Produkt {product_id}"
    
    def get_intent_display_name(self, intent: str) -> str:
        """
        Hämta visningsnamn för en intention
        
        Args:
            intent: Intentionskod
            
        Returns:
            Visningsnamn
        """
        intent_display = {
            "technical": "tekniska specifikationer",
            "compatibility": "kompatibilitetsinformation",
            "summary": "produktsammanfattning",
            "search": "produktsökning"
        }
        
        return intent_display.get(intent, intent)
    
    def infer_expertise_level(self, context: Dict[str, Any]) -> str:
        """
        Härleda användarens expertisgrad från kontext
        
        Args:
            context: Kontextinformation
            
        Returns:
            Expertisgrad (beginner/intermediate/expert)
        """
        # Om expertisgrad redan finns i kontexten, använd den
        if "expertise_level" in context:
            return context["expertise_level"]
        
        # Härleda från frågehistorik
        query_history = context.get("query_history", [])
        
        if not query_history:
            return "intermediate"  # Standardnivå för ny användare
        
        # Analysera tidigare frågor för att bedöma expertis
        technical_terms = [
            "specifikation", "dimensioner", "tolerans", "teknisk", "material",
            "effekt", "spänning", "kompatibilitet", "monteringsanvisning"
        ]
        
        # Räkna tekniska termer i historiken
        technical_count = 0
        for query in query_history:
            query_lower = query.lower()
            for term in technical_terms:
                if term in query_lower:
                    technical_count += 1
        
        # Bedöm nivå baserat på tekniska termer och historiklängd
        if technical_count >= 3 or len(query_history) >= 10:
            return "expert"
        elif technical_count >= 1 or len(query_history) >= 3:
            return "intermediate"
        else:
            return "beginner"
    
    def simplify_technical_terms(self, text: str) -> str:
        """
        Förenkla tekniska termer i text för nybörjaranvändare
        
        Args:
            text: Texten att förenkla
            
        Returns:
            Förenklad text
        """
        # Ersättningsordbok för tekniska termer
        replacements = {
            r'\b([Dd]imensioner)\b': r'mått',
            r'\b([Kk]ompatibilitet)\b': r'passar tillsammans med',
            r'\b([Ss]pecifikationer)\b': r'egenskaper',
            r'\b([Mm]ontering)\b': r'installation',
            r'\b([Tt]olerans)\b': r'tillåten avvikelse',
            r'\b([Ee]ffekt)\b': r'strömförbrukning'
        }
        
        # Utför ersättningar
        simplified_text = text
        for pattern, replacement in replacements.items():
            simplified_text = re.sub(pattern, replacement, simplified_text)
        
        return simplified_text
```

---

# ..\..\dialog\templates.py
## File: ..\..\dialog\templates.py

```py
# ..\..\dialog\templates.py
# nlp_bot_engine/dialog/templates.py

class ResponseTemplates:
    """
    Samling av svarsmallar för olika situationer och intentioner.
    """
    
    def __init__(self):
        """
        Initialisera mallsamlingen
        """
        self.templates = {
            # Generiska mallar
            "generic": "Jag sökte information om \"{query}\". Här är vad jag hittade.",
            
            "error": "Något gick fel: {error}",
            
            # Förtydligandemallar
            "generic_clarification": "Jag förstod inte riktigt din fråga \"{query}\". Kan du omformulera den eller vara mer specifik?",
            
            "product_clarification": "{question}\n\n{options}",
            
            "intent_clarification": "{question}\n\n{options}",
           
           # Mallar för låg konfidens
           "low_confidence_disclaimer": "Jag är inte helt säker, men jag tror att du frågar om {intent}.",
           
           "alternative_intents": "Du kanske också ville fråga om {alternatives}?",
           
           # Mallar för teknisk information
           "technical_beginner_intro": "Här är de viktigaste tekniska egenskaperna för {product_name} i ett förenklat format:",
           
           "no_technical_info": "Jag kunde tyvärr inte hitta någon teknisk information för {product_name}.",
           
           # Mallar för kompatibilitet
           "compatibility_intro": "Här är information om vilka produkter som {product_name} fungerar tillsammans med:",
           
           "no_compatibility_info": "Jag kunde tyvärr inte hitta någon kompatibilitetsinformation för {product_name}.",
           
           # Mallar för sammanfattningar
           "no_summary_info": "Jag kunde tyvärr inte hitta någon sammanfattande information för {product_name}.",
           
           # Mallar för sökning
           "no_search_results": "Jag kunde inte hitta några produkter som matchar din sökning '{query}'.",
           
           
           # Produktjämförelser
            "comparison_intro": "Här är en jämförelse mellan {product_name1} och {product_name2}:",
            "no_comparison_data": "Jag har inte tillräckligt med information för att jämföra dessa produkter.",

            # Felstavningar och korrigeringar
            "spelling_correction": "Jag antar att du menade \"{corrected_query}\" istället för \"{original_query}\".",

            # Dialoghantering
            "follow_up_question": "Angående {product_name}, {follow_up_response}",
            "multiple_products_question": "Du nämnde flera produkter. Vilken vill du veta mer om?",

            # Förslag
            "suggestion": "Du kanske också vill veta om {suggestion}?",
            "related_products_suggestion": "Liknande produkter du kanske är intresserad av:",

            # Hantering av produktserier
            "product_series_intro": "{series_name}-serien omfattar flera produkter med liknande egenskaper men olika {differentiator}.",
       }
   
    def get_template(self, template_key: str) -> str:
        """
        Hämta en mall baserat på nyckel
        
        Args:
            template_key: Mallens nyckel
            
        Returns:
            Malltext eller tom sträng om nyckeln inte finns
        """
        return self.templates.get(template_key, "")
    
    def add_template(self, template_key: str, template_text: str) -> None:
        """
        Lägg till eller uppdatera en mall
        
        Args:
            template_key: Mallens nyckel
            template_text: Mallens text
        """
        self.templates[template_key] = template_text
```

---

# ..\..\nlp\context_manager.py
## File: ..\..\nlp\context_manager.py

```py
# ..\..\nlp\context_manager.py
# nlp_bot_engine/nlp/context_manager.py

import logging
from typing import Dict, List, Any, Optional, Tuple

from ..core.config import BotConfig

logger = logging.getLogger(__name__)

class ContextManager:
    """
    Hanterar konversationskontext och referensupplösning.
    Spårar tidigare frågor, aktiva produkter och dialogstatus.
    """
    
    def __init__(self, config: BotConfig):
        """
        Initialisera kontexthanteraren
        
        Args:
            config: Konfigurationsobjekt
        """
        self.config = config
        
    def analyze_context(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analysera frågan i dess kontext för bättre förståelse
        
        Args:
            query: Användarens fråga
            context: Kontextinformation
            
        Returns:
            Utökad kontextanalys
        """
        # Standardisera kontextparameter
        if context is None:
            context = {}
        
        # Analysresultat
        analysis = {
            "query_type": "unknown",
            "references": [],
            "resolved_entities": {},
            "suggested_products": [],
            "context_products": []
        }
        
        # Kolla om det finns en aktiv produkt i kontexten
        active_product_id = context.get("active_product_id")
        if active_product_id:
            analysis["context_products"].append({
                "product_id": active_product_id,
                "relation": "active"
            })
        
        # Identifiera kontextberoendetyp
        context_type = self.identify_context_type(query, context)
        analysis["query_type"] = context_type
        
        # Lös referenser om det är en kontextberoende fråga
        if context_type in ["follow_up", "reference", "comparison"]:
            references = self.identify_references(query)
            analysis["references"] = references
            
            # Lös upp referenserna mot kontexten
            resolved = self.resolve_references(references, context)
            analysis["resolved_entities"] = resolved
        
        # Lägg till dialoghistorik
        if "query_history" in context:
            analysis["dialog_history"] = context["query_history"]
        
        # Lägg till tidigare intention om sådan finns
        if "previous_intent" in context:
            analysis["previous_intent"] = context["previous_intent"]
        
        return analysis
    
    def identify_context_type(self, query: str, context: Dict[str, Any]) -> str:
        """
        Identifiera typ av kontextberoende i frågan
        
        Args:
            query: Användarens fråga
            context: Kontextinformation
            
        Returns:
            Kontextberoendetyp
        """
        query_lower = query.lower()
        
        # Kontrollera för specifika referensord
        reference_terms = {
            "follow_up": ["mer", "fortsätt", "berätta mer", "och", "också"],
            "reference": ["den", "denna", "det", "dessa", "dom", "dom här", "den där", "detta"],
            "comparison": ["jämfört med", "kontra", "vs", "versus", "jämför", "skillnad", "skillnaden mellan"]
        }
        
        # Kolla om frågan innehåller referenstermer
        for context_type, terms in reference_terms.items():
            if any(term in query_lower for term in terms):
                return context_type
        
        # Kolla om det är en kort fråga utan specifik produkt (troligen uppföljning)
        if len(query_lower.split()) <= 3 and context.get("active_product_id"):
            return "follow_up"
        
        # Standardtyp om inget annat matchar
        return "independent"
    
    def identify_references(self, query: str) -> List[Dict[str, Any]]:
        """
        Identifiera referenser i texten (t.ex. "den", "denna", osv.)
        
        Args:
            query: Användarens fråga
            
        Returns:
            Lista med identifierade referenser
        """
        query_lower = query.lower()
        references = []
        
        # Definiera referenstyper och deras nyckelord
        reference_types = {
            "product": ["den", "denna", "den här", "produkten", "artikeln"],
            "property": ["det", "detta", "den egenskapen", "den funktionen"],
            "multiple": ["dessa", "de", "dom", "de här", "dom här", "produkterna"]
        }
        
        # Sök efter referenser i texten
        for ref_type, keywords in reference_types.items():
            for keyword in keywords:
                if keyword in query_lower:
                    # Hitta position i texten
                    start_pos = query_lower.find(keyword)
                    
                    references.append({
                        "type": ref_type,
                        "text": keyword,
                        "start": start_pos,
                        "end": start_pos + len(keyword)
                    })
        
        return references
    
    def resolve_references(self, references: List[Dict[str, Any]], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lös upp identifierade referenser mot kontexten
        
        Args:
            references: Lista med identifierade referenser
            context: Kontextinformation
            
        Returns:
            Dict med upplösta referenser
        """
        resolved = {}
        
        for ref in references:
            ref_type = ref["type"]
            
            if ref_type == "product" and context.get("active_product_id"):
                # Lös "den"/"denna" till aktiv produkt
                resolved[ref["text"]] = {
                    "type": "product",
                    "product_id": context["active_product_id"]
                }
                
            elif ref_type == "property" and context.get("last_mentioned_property"):
                # Lös "det"/"detta" till senast nämnda egenskap
                resolved[ref["text"]] = {
                    "type": "property",
                    "property": context["last_mentioned_property"]
                }
                
            elif ref_type == "multiple" and context.get("mentioned_products"):
                # Lös "dessa"/"de" till tidigare nämnda produkter
                resolved[ref["text"]] = {
                    "type": "products",
                    "product_ids": context["mentioned_products"]
                }
        
        return resolved
    
    def update_context(self, current_context: Dict[str, Any], new_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Uppdatera kontexten med ny information
        
        Args:
            current_context: Nuvarande kontextinformation
            new_info: Ny information att lägga till
            
        Returns:
            Uppdaterad kontextinformation
        """
        # Kopiera nuvarande kontext för att undvika att modifiera original
        updated_context = current_context.copy()
        
        # Uppdatera aktiv produkt om ny information finns
        if "product_id" in new_info:
            updated_context["active_product_id"] = new_info["product_id"]
            
            # Uppdatera listan över nämnda produkter
            mentioned_products = updated_context.get("mentioned_products", [])
            if new_info["product_id"] not in mentioned_products:
                mentioned_products.append(new_info["product_id"])
            updated_context["mentioned_products"] = mentioned_products
        
        # Uppdatera senast nämnda egenskap
        if "property" in new_info:
            updated_context["last_mentioned_property"] = new_info["property"]
        
        # Uppdatera senaste intention
        if "primary_intent" in new_info:
            updated_context["previous_intent"] = new_info["primary_intent"]
        
        # Uppdatera användarhistorik
        if "query" in new_info:
            query_history = updated_context.get("query_history", [])
            query_history.append(new_info["query"])
            
            # Begränsa historiken till senaste 10 frågor
            if len(query_history) > 10:
                query_history = query_history[-10:]
                
            updated_context["query_history"] = query_history
        
        return updated_context
    
    def extract_conversation_state(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extrahera aktuell konversationsstatus
        
        Args:
            context: Kontextinformation
            
        Returns:
            Dict med konversationsstatus
        """
        state = {
            "active_product": context.get("active_product_id"),
            "dialog_stage": "unknown",
            "mentioned_products": context.get("mentioned_products", []),
            "previous_intent": context.get("previous_intent"),
            "session_duration": context.get("session_duration", 0)
        }
        
        # Bestäm dialogstadium baserat på historik och förekomst av aktiv produkt
        if not context.get("query_history"):
            state["dialog_stage"] = "initial"
        elif context.get("active_product_id"):
            if state["previous_intent"] in ["technical", "compatibility"]:
                state["dialog_stage"] = "detailed_inquiry"
            else:
                state["dialog_stage"] = "product_exploration"
        else:
            state["dialog_stage"] = "search"
        
        return state
```

---

# ..\..\nlp\entity_extractor.py
## File: ..\..\nlp\entity_extractor.py

```py
# ..\..\nlp\entity_extractor.py
# nlp_bot_engine/nlp/entity_extractor.py

import re
import logging
from typing import Dict, List, Any, Optional, Tuple, Union

from ..core.config import BotConfig
from .processor import NLPProcessor

logger = logging.getLogger(__name__)

class EntityExtractor:
    """
    Extraherar entiteter från text, inklusive produkter, egenskaper och ID:n.
    Kombinerar mönsterigenkänning, NER och kontextförståelse.
    """
    
    def __init__(self, config: BotConfig, nlp_processor: NLPProcessor):
        """
        Initialisera entitetsextraktorn
        
        Args:
            config: Konfigurationsobjekt
            nlp_processor: NLP-processor för textanalys
        """
        self.config = config
        self.nlp_processor = nlp_processor
    
    def extract_entities(self, text: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Extrahera alla entiteter från texten
        
        Args:
            text: Texten att analysera
            context: Kontextinformation
            
        Returns:
            Lista med extraherade entiteter
        """
        # Initialisera kontextparameter
        context = context or {}
        
        # Samla entiteter från olika metoder
        entities = []
        
        # 1. Extrahera med spaCy NER om tillgänglig
        if self.nlp_processor.nlp:
            spacy_entities = self.extract_spacy_entities(text)
            entities.extend(spacy_entities)
        
        # 2. Extrahera med regelbundna uttryck (för att fånga produkt-ID, EAN, etc.)
        regex_entities = self.extract_regex_entities(text)
        entities.extend(regex_entities)
        
        # 3. Extrahera produktentiteter från produktnamn
        product_entities = self.extract_product_entities(text)
        entities.extend(product_entities)
        
        # 4. Extrahera relaterade entiteter från kontexten
        if context:
            context_entities = self.extract_context_entities(text, context)
            entities.extend(context_entities)
        
        # 5. Sammanfoga entiteter så att liknande entiteter slås ihop
        entities = self.merge_overlapping_entities(entities)
        
        # 6. Berika entiteter med produktreferenser och information
        entities = self.enrich_entities(entities, context)
        
        return entities
    
    def extract_spacy_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Extrahera entiteter med spaCy NER
        
        Args:
            text: Texten att analysera
            
        Returns:
            Lista med spaCy-entiteter
        """
        if not self.nlp_processor.nlp:
            return []
        
        doc = self.nlp_processor.nlp(text)
        entities = []
        
        for ent in doc.ents:
            entity = {
                "type": ent.label_,
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
                "confidence": 0.8,  # Standardkonfidens för spaCy NER
                "source": "spacy"
            }
            
            # Normalisera entitetstyper till våra standardtyper

            if ent.label_ in ["EAN"]:
                entity["type"] = "EAN"
            elif ent.label_ in ["PRODUCT", "WORK_OF_ART", "ORG"]:
                entity["type"] = "PRODUCT"
            elif ent.label_ in ["DIMENSION", "QUANTITY"]:
                entity["type"] = "DIMENSION"
            elif ent.label_ in ["COMPATIBILITY"]:
                entity["type"] = "COMPATIBILITY"
            
            entities.append(entity)
        
        return entities
    
    def extract_regex_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Extrahera entiteter med regelbundna uttryck
        
        Args:
            text: Texten att analysera
            
        Returns:
            Lista med regex-extraherade entiteter
        """
        entities = []
        
        # Artikelnummer-mönster
        article_patterns = [
            r'(?i)art(?:ikel)?\.?(?:nr|nummer)\.?\s*[:=]?\s*([A-Z0-9\-]{5,15})',
            r'(?<!\d)(\d{8})(?!\d)',  # Åttasiffrigt artikelnummer
        ]
        
        # EAN-mönster
        ean_patterns = [
            r'(?i)EAN(?:-13)?[:.\-]?\s*(\d{13})(?!\d)',
            r'(?<!\d)(\d{13})(?!\d)',  # Fristående 13-siffrigt nummer
            r'(?i)EAN(?:-8)?[:.\-]?\s*(\d{8})(?!\d)',
        ]
        
        # Dimensionsmönster
        dimension_patterns = [
            r'(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m|tum)',
        ]
        
        # Leta efter artikelnummer
        for pattern in article_patterns:
            for match in re.finditer(pattern, text):
                article_number = match.group(1)
                entities.append({
                    "type": "ARTICLE_NUMBER",
                    "text": article_number,
                    "start": match.start(1),
                    "end": match.end(1),
                    "confidence": 0.9,
                    "source": "regex"
                })
        
        # Leta efter EAN-koder
        for pattern in ean_patterns:
            for match in re.finditer(pattern, text):
                ean = match.group(1)
                # Validera EAN om möjligt
                if self.is_valid_ean(ean):
                    entities.append({
                        "type": "EAN",
                        "text": ean,
                        "start": match.start(1),
                        "end": match.end(1),
                        "confidence": 0.95,
                        "source": "regex"
                    })
        
        # Leta efter dimensioner
        for pattern in dimension_patterns:
            for match in re.finditer(pattern, text):
                dimension = match.group(0)  # Hela matchningen inkl. enhet
                entities.append({
                    "type": "DIMENSION",
                    "text": dimension,
                    "start": match.start(0),
                    "end": match.end(0),
                    "confidence": 0.85,
                    "source": "regex"
                })
        
        return entities
    
    def extract_product_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Extrahera produkter genom matchning mot produktnamnsindex
        
        Args:
            text: Texten att analysera
            
        Returns:
            Lista med extraherade produkter
        """
        entities = []
        text_lower = text.lower()
        
        # Få produktnamnsmappning från nlp_processor
        name_to_id_map = getattr(self.nlp_processor, 'name_to_id_map', {})
        
        if not name_to_id_map and hasattr(self.nlp_processor, 'data_manager'):
            # Försök att få produktnamn från datahanteraren om de finns där
            name_to_id_map = getattr(self.nlp_processor.data_manager, 'name_to_id_map', {})
        
        # Sök efter produktnamn i texten
        for name, product_id in name_to_id_map.items():
            if name in text_lower:
                # Hitta startpositionen (kan finnas på flera ställen)
                start_pos = text_lower.find(name)
                
                # Medan vi hittar fler förekomster
                while start_pos != -1:
                    entities.append({
                        "type": "PRODUCT",
                        "text": text[start_pos:start_pos+len(name)],  # Använd originalkapitalisering
                        "start": start_pos,
                        "end": start_pos + len(name),
                        "confidence": 0.9,
                        "source": "product_index",
                        "product_id": product_id
                    })
                    
                    # Sök efter nästa förekomst
                    start_pos = text_lower.find(name, start_pos + 1)
        
        return entities
    
    def extract_context_entities(self, text: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extrahera entiteter baserat på kontext
        
        Args:
            text: Texten att analysera
            context: Kontextinformation
            
        Returns:
            Lista med kontextbaserade entiteter
        """
        entities = []
        
        # Om aktiv produkt finns i kontexten
        active_product_id = context.get("active_product_id")
        if active_product_id:
            # Kolla om texten innehåller kontext-refererande ord som "den", "denna", etc.
            context_refs = ["den", "denna", "det", "produkten", "artikeln"]
            text_lower = text.lower().split()
            
            for ref in context_refs:
                if ref in text_lower:
                    # Hämta produktnamn om möjligt
                    product_name = self.get_product_name(active_product_id)
                    
                    entities.append({
                        "type": "PRODUCT",
                        "text": product_name or f"Produkt {active_product_id}",
                        "start": -1,  # Implicit referens, ingen position i texten
                        "end": -1,
                        "confidence": 0.8,
                        "source": "context",
                        "product_id": active_product_id,
                        "is_contextual_reference": True
                    })
                    break  # En referens räcker
        
        return entities
    
    def merge_overlapping_entities(self, entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Sammanfoga överlappande entiteter
        
        Args:
            entities: Lista med entiteter
            
        Returns:
            Lista med sammanfogade entiteter
        """
        if not entities:
            return []
        
        # Sortera efter startposition och sedan efter längd (längre först vid samma position)
        sorted_entities = sorted(entities, key=lambda e: (e.get("start", -1), -len(e.get("text", ""))))
        
        merged = []
        current = sorted_entities[0]
        
        for entity in sorted_entities[1:]:
            current_end = current.get("end", -1)
            next_start = entity.get("start", -1)
            
            # Om de överlappar
            if current_end >= next_start and next_start >= 0 and current_end >= 0:
                # Behåll den med högre konfidens eller den större om lika
                if entity.get("confidence", 0) > current.get("confidence", 0):
                    current = entity
            else:
                merged.append(current)
                current = entity
        
        # Lägg till den sista
        merged.append(current)
        
        return merged
    
    def enrich_entities(self, entities: List[Dict[str, Any]], context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Berika entiteter med ytterligare information
        
        Args:
            entities: Lista med entiteter
            context: Kontextinformation
            
        Returns:
            Lista med berikade entiteter
        """
        enriched = []
        
        for entity in entities:
            # Kopiera entiteten för att undvika att modifiera originalet
            enriched_entity = entity.copy()
            
            # Berika olika entitetstyper
            if entity["type"] == "PRODUCT":
                # Se om vi redan har product_id
                if "product_id" not in entity:
                    # Försök att hitta produkt-ID baserat på namn
                    product_id = self.find_product_id_by_name(entity["text"])
                    if product_id:
                        enriched_entity["product_id"] = product_id
            
            elif entity["type"] == "ARTICLE_NUMBER":
                # Validera och hitta produkt-ID
                article_number = entity["text"]
                product_id = self.find_product_id_by_article_number(article_number)
                if product_id:
                    enriched_entity["product_id"] = product_id
                    enriched_entity["type"] = "PRODUCT"  # Konvertera till produktentitet
            
            elif entity["type"] == "EAN":
                # Validera och hitta produkt-ID
                ean = entity["text"]
                product_id = self.find_product_id_by_ean(ean)
                if product_id:
                    enriched_entity["product_id"] = product_id
                    enriched_entity["type"] = "PRODUCT"  # Konvertera till produktentitet
            
            # Lägg till berikad version
            enriched.append(enriched_entity)
        
        return enriched
    
    def is_valid_ean(self, ean: str) -> bool:
        """
        Validera en EAN-kod med checksumma
        
        Args:
            ean: EAN-koden att validera
            
        Returns:
            True om giltig, annars False
        """
        if not ean.isdigit():
            return False
        
        # EAN-8, EAN-13, UPC (12 digits), or GTIN-14
        if len(ean) not in [8, 12, 13, 14]:
            return False
        
        # Checksumma-beräkning
        total = 0
        for i, digit in enumerate(reversed(ean[:-1])):
            multiplier = 3 if i % 2 == 0 else 1
            total += int(digit) * multiplier
            
        check_digit = (10 - (total % 10)) % 10
        
        return check_digit == int(ean[-1])
    
    def get_product_name(self, product_id: str) -> Optional[str]:
        """
        Hämta produktnamn för ett givet produkt-ID
        
        Args:
            product_id: Produktens ID
            
        Returns:
            Produktnamn eller None om det inte hittas
        """
        # Försök att få tillgång till produkt-index eller datahanterare
        data_manager = getattr(self.nlp_processor, 'data_manager', None)
        
        if data_manager:
            return data_manager.get_product_name(product_id)
        
        return None
    
    def find_product_id_by_name(self, name: str) -> Optional[str]:
        """
        Hitta produkt-ID baserat på namn
        
        Args:
            name: Produktnamnet
            
        Returns:
            Produkt-ID eller None om det inte hittas
        """
        name_lower = name.lower()
        
        # Få produktnamnsmappning
        name_to_id_map = getattr(self.nlp_processor, 'name_to_id_map', {})
        
        if not name_to_id_map and hasattr(self.nlp_processor, 'data_manager'):
            name_to_id_map = getattr(self.nlp_processor.data_manager, 'name_to_id_map', {})
        
        # Exakt matchning
        if name_lower in name_to_id_map:
            return name_to_id_map[name_lower]
        
        # Alternativt, försök med fuzzy matching
        best_match = None
        best_score = 0
        
        for product_name, product_id in name_to_id_map.items():
            # Beräkna likhet
            similarity = self.calculate_name_similarity(name_lower, product_name)
            
            if similarity > best_score and similarity > 0.8:  # Minst 80% match
                best_score = similarity
                best_match = product_id
        
        return best_match
    
    def find_product_id_by_article_number(self, article_number: str) -> Optional[str]:
        """
        Hitta produkt-ID baserat på artikelnummer
        
        Args:
            article_number: Artikelnumret
            
        Returns:
            Produkt-ID eller None om det inte hittas
        """
        # Försök att få tillgång till artikelnummer-index
        data_manager = getattr(self.nlp_processor, 'data_manager', None)
        
        if data_manager and hasattr(data_manager, 'indices'):
            article_index = data_manager.indices.get("article_numbers", {})
            
            if article_number in article_index:
                # Artikelnummerindex kan ha flera produkter per nummer
                products = article_index[article_number]
                if products and isinstance(products, list) and isinstance(products[0], dict):
                    return products[0].get("product_id")
        
        return None
    
    def find_product_id_by_ean(self, ean: str) -> Optional[str]:
        """
        Hitta produkt-ID baserat på EAN
        
        Args:
            ean: EAN-kod
            
        Returns:
            Produkt-ID eller None om det inte hittas
        """
        # Försök att få tillgång till EAN-index
        data_manager = getattr(self.nlp_processor, 'data_manager', None)
        
        if data_manager and hasattr(data_manager, 'indices'):
            ean_index = data_manager.indices.get("ean_numbers", {})
            
            if ean in ean_index:
                # EAN-index kan ha flera produkter per EAN
                products = ean_index[ean]
                if products and isinstance(products, list) and isinstance(products[0], dict):
                    return products[0].get("product_id")
        
        return None
    
    def calculate_name_similarity(self, name1: str, name2: str) -> float:
        """
        Beräkna likhet mellan två produktnamn
        
        Args:
            name1: Första namnet
            name2: Andra namnet
            
        Returns:
            Likhetspoäng mellan 0 och 1
        """
        # Enkel tokenisering
        tokens1 = set(name1.lower().split())
        tokens2 = set(name2.lower().split())
        
        # Jaccard-likhet
        if not tokens1 or not tokens2:
            return 0
        
        intersection = len(tokens1.intersection(tokens2))
        union = len(tokens1.union(tokens2))
        
        return intersection / union
```

---

# ..\..\nlp\intent_analyzer.py
## File: ..\..\nlp\intent_analyzer.py

```py
# ..\..\nlp\intent_analyzer.py
# nlp_bot_engine/nlp/intent_analyzer.py

import logging
from typing import Dict, List, Any, Optional, Tuple

from ..core.config import BotConfig
from .processor import NLPProcessor

logger = logging.getLogger(__name__)

class IntentAnalyzer:
    """
    Analyserar användarfrågor för att identifiera intention.
    Kombinerar nyckelordsmatchning, kontextanalys och semantisk analys.
    """
    
    def __init__(self, config: BotConfig, nlp_processor: NLPProcessor):
        """
        Initialisera intentionsanalysator
        
        Args:
            config: Konfigurationsobjekt
            nlp_processor: NLP-processor för textanalys
        """
        self.config = config
        self.nlp_processor = nlp_processor
        
        # Fördefinierade intentionsprototyper för semantisk matchning
        self.intent_prototypes = {
            "technical": [
                "Vad är de tekniska specifikationerna för denna produkt?",
                "Vilka mått har produkten?",
                "Hur mycket väger produkten?",
                "Vilket material är produkten tillverkad av?",
                "Vad är spänningen för produkten?"
            ],
            "compatibility": [
                "Är denna produkt kompatibel med andra produkter?",
                "Passar produkten till min existerande installation?",
                "Vilka andra produkter fungerar med denna?",
                "Kan jag använda denna med produkt X?",
                "Vilka trycken passar denna produkt?"
            ],
            "summary": [
                "Berätta om denna produkt",
                "Vad är detta för produkt?",
                "Ge mig en översikt över produkten",
                "Vilken information finns om produkten?",
                "Vad används denna produkt till?"
            ],
            "search": [
                "Jag letar efter en produkt som...",
                "Hitta produkter som liknar...",
                "Sök efter produkter som...",
                "Finns det några produkter för...",
                "Jag behöver en produkt som kan..."
            ]
        }
        
        # Generera embeddings för intentionsprototyper om möjligt
        self.intent_embeddings = {}
        
        if self.nlp_processor.embedding_model:
            for intent, examples in self.intent_prototypes.items():
                # Använd genomsnitt av alla exempel
                embeddings = []
                for example in examples:
                    embedding = self.nlp_processor.get_embeddings(example)
                    if embedding:
                        embeddings.append(embedding)
                
                if embeddings:
                    import numpy as np
                    # Beräkna genomsnitt av alla embeddings
                    self.intent_embeddings[intent] = np.mean(embeddings, axis=0).tolist()
    
    def analyze_intent(self, text: str, entities: List[Dict[str, Any]], 
                      context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analysera användartexten för att identifiera huvudsaklig intention
        
        Args:
            text: Användartexten
            entities: Extraherade entiteter
            context: Kontextinformation
            
        Returns:
            Dict med intentionsanalys
        """
        # 1. Nyckelordsbaserad intentionsidentifiering
        keyword_intents = self.nlp_processor.detect_intent_keywords(text)
        
        # 2. Semantisk intentionsidentifiering (om embeddings finns)
        semantic_intents = self.detect_semantic_intent(text)
        
        # 3. Entitetsbaserad intentionsidentifiering
        entity_intents = self.detect_entity_based_intent(entities)
        
        # 4. Kontextbaserad intentionsidentifiering
        context_intents = self.detect_context_based_intent(context)
        
        # 5. Kombinera alla metoder med viktning
        combined_intents = self.combine_intent_scores(
            keyword_intents, semantic_intents, entity_intents, context_intents
        )
        
        # 6. Identifiera primär intention med konfidens
        primary_intent, confidence = self.determine_primary_intent(combined_intents)
        
        # 7. Sortera intentioner efter poäng
        sorted_intents = [
            {"intent": intent, "score": score}
            for intent, score in sorted(combined_intents.items(), key=lambda x: x[1], reverse=True)
        ]
        
        return {
            "intents": sorted_intents,
            "primary_intent": primary_intent,
            "confidence": confidence,
            "keyword_based": keyword_intents,
            "semantic_based": semantic_intents,
            "entity_based": entity_intents,
            "context_based": context_intents
        }
    
    def detect_semantic_intent(self, text: str) -> Dict[str, float]:
        """
        Detektera intention baserat på semantisk likhet
        
        Args:
            text: Texten att analysera
            
        Returns:
            Dict med intentioner och deras poäng
        """
        # Om vi inte har embeddings, returnera tomma poäng
        if not self.intent_embeddings:
            return {intent: 0.0 for intent in self.intent_prototypes}
        
        # Skapa embedding för texten
        text_embedding = self.nlp_processor.get_embeddings(text)
        
        if not text_embedding:
            return {intent: 0.0 for intent in self.intent_prototypes}
        
        # Beräkna similarity med varje intentionsprototyp
        intent_scores = {}
        
        import numpy as np
        text_vec = np.array(text_embedding)
        
        for intent, prototype_vec in self.intent_embeddings.items():
            # Beräkna cosine similarity
            proto_vec = np.array(prototype_vec)
            
            dot_product = np.dot(text_vec, proto_vec)
            text_norm = np.linalg.norm(text_vec)
            proto_norm = np.linalg.norm(proto_vec)
            
            if text_norm == 0 or proto_norm == 0:
                similarity = 0.0
            else:
                similarity = dot_product / (text_norm * proto_norm)
            
            # Normalisera till [0,1]
            similarity = max(0.0, min(1.0, (similarity + 1) / 2))
            
            intent_scores[intent] = similarity
        
        return intent_scores
    
    def detect_entity_based_intent(self, entities: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Detektera intention baserat på extraherade entiteter
        
        Args:
            entities: Lista med extraherade entiteter
            
        Returns:
            Dict med intentioner och deras poäng
        """
        intent_scores = {
            "technical": 0.0,
            "compatibility": 0.0,
            "summary": 0.0,
            "search": 0.0
        }
        
        # Sammanställ entitetstyper
        entity_types = [entity["type"] for entity in entities]
        entity_types_count = {etype: entity_types.count(etype) for etype in set(entity_types)}
        
        # Öka poäng baserat på entitetstyper
        if "DIMENSION" in entity_types_count:
            intent_scores["technical"] += 0.6 * min(entity_types_count["DIMENSION"], 3) / 3
        
        if "COMPATIBILITY" in entity_types_count:
            intent_scores["compatibility"] += 0.8
        
        if "PRODUCT" in entity_types_count:
            # Om många produkter nämns, troligen en sökning
            if entity_types_count["PRODUCT"] > 1:
                intent_scores["search"] += 0.5
            else:
                # Annars troligen en produktsummering eller teknisk info
                intent_scores["summary"] += 0.4
                intent_scores["technical"] += 0.3
        
        # Om det finns flera produkter och kompatibilitetstermer, troligen kompatibilitetsfråga
        if entity_types_count.get("PRODUCT", 0) > 1 and "COMPATIBILITY" in entity_types_count:
            intent_scores["compatibility"] += 0.3
        
        # Om inga specifika entiteter hittades, anta summering
        if not entity_types:
            intent_scores["summary"] += 0.2
        
        return intent_scores
    
    def detect_context_based_intent(self, context: Dict[str, Any]) -> Dict[str, float]:
        """
        Detektera intention baserat på konversationskontext
        
        Args:
            context: Kontextinformation
            
        Returns:
            Dict med intentioner och deras poäng
        """
        intent_scores = {
            "technical": 0.0,
            "compatibility": 0.0,
            "summary": 0.0,
            "search": 0.0
        }
        
        # Analysera tidigare meddelanden/kontext
        query_history = context.get("query_history", [])
        
        if query_history:
            # Titta på tidigare intentioner i konversationen
            if context.get("previous_intent") == "summary":
                # Om förra var summary, troligt att nästa är mer specifik
                intent_scores["technical"] += 0.2
                intent_scores["compatibility"] += 0.2
            
            elif context.get("previous_intent") == "technical":
                # Om förra var teknisk, troligt att fortsätta med tekniska frågor
                intent_scores["technical"] += 0.3
            
            elif context.get("previous_intent") == "compatibility":
                # Om förra var kompabilitet, troligt att fortsätta med kompatibilitet
                intent_scores["compatibility"] += 0.3
            
            # Kolla om användaren just sökt och nu frågar om en produkt
            if context.get("previous_intent") == "search" and context.get("active_product_id"):
                intent_scores["summary"] += 0.4
        
        # Om ingen historik finns, anta summering
        else:
            intent_scores["summary"] += 0.1
        
        return intent_scores
    
    def combine_intent_scores(self, keyword_intents: Dict[str, float], 
                             semantic_intents: Dict[str, float],
                             entity_intents: Dict[str, float],
                             context_intents: Dict[str, float]) -> Dict[str, float]:
        """
        Kombinera intentionspoäng från olika metoder med vikter
        
        Args:
            keyword_intents: Intentionspoäng från nyckelord
            semantic_intents: Intentionspoäng från semantisk analys
            entity_intents: Intentionspoäng från entiteter
            context_intents: Intentionspoäng från kontext
            
        Returns:
            Dict med kombinerade intentionspoäng
        """
        # Vikter för olika metoder
        method_weights = {
            "keyword": 0.35,
            "semantic": 0.30,
            "entity": 0.25,
            "context": 0.10
        }
        
        combined_scores = {}
        
        # Kombinera poäng för varje intention
        for intent in keyword_intents.keys():
            combined_scores[intent] = (
                keyword_intents.get(intent, 0.0) * method_weights["keyword"] +
                semantic_intents.get(intent, 0.0) * method_weights["semantic"] +
                entity_intents.get(intent, 0.0) * method_weights["entity"] +
                context_intents.get(intent, 0.0) * method_weights["context"]
            )
        
        return combined_scores
    
    def determine_primary_intent(self, intent_scores: Dict[str, float]) -> Tuple[str, float]:
        """
        Identifiera primär intention och dess konfidens
        
        Args:
            intent_scores: Dict med intentionspoäng
            
        Returns:
            Tuppel med primär intention och konfidenspoäng
        """
        if not intent_scores:
            return "summary", 0.1
        
        # Hitta intentionen med högst poäng
        primary_intent = max(intent_scores.items(), key=lambda x: x[1])
        intent_name, highest_score = primary_intent
        
        # Sortera alla poäng i fallande ordning
        sorted_scores = sorted(intent_scores.values(), reverse=True)
        
        # Beräkna konfidens baserat på skillnad från runner-up
        confidence = highest_score
        
        # Om det finns minst två intentioner, se på differensen
        if len(sorted_scores) > 1:
            confidence_margin = highest_score - sorted_scores[1]
            
            # Justera konfidensen baserat på marginal till närmaste konkurrent
            if confidence_margin < 0.1:
                # Liten marginal - minska konfidensen
                confidence = highest_score * 0.8
            elif confidence_margin > 0.3:
                # Stor marginal - öka konfidensen något
                confidence = min(1.0, highest_score * 1.1)
        
        return intent_name, confidence
```

---

# ..\..\nlp\processor.py
## File: ..\..\nlp\processor.py

```py
# ..\..\nlp\processor.py
# nlp_bot_engine/nlp/processor.py

import re
import logging
import unicodedata
from typing import Dict, List, Any, Optional, Tuple, Union
import importlib.util

from ..core.config import BotConfig

logger = logging.getLogger(__name__)

class NLPProcessor:
    """
    Huvudprocessor för NLP-funktionalitet.
    Ansvarar för tokenisering, lemmatisering, och grundläggande textbearbetning.
    Fungerar som gränssnitt mot underliggande NLP-bibliotek.
    """
    
    def __init__(self, config: BotConfig):
        """
        Initialisera NLP-processorn
        
        Args:
            config: Konfigurationsobjekt
        """
        self.config = config
        self.nlp = None
        self.embedding_model = None
        
        # Ladda spaCy-modell om tillgänglig
        if config.use_nlp:
            self.load_spacy()
            self.load_embedding_model()
    
    def load_spacy(self) -> bool:
        """
        Ladda spaCy-modellen
        
        Returns:
            True om laddningen lyckades, annars False
        """
        try:
            # Kolla om spaCy är installerat
            if importlib.util.find_spec("spacy") is None:
                logger.warning("spaCy är inte installerat. Vissa NLP-funktioner kommer att vara begränsade.")
                return False
            
            import spacy
            self.nlp = spacy.load(self.config.spacy_model)
            logger.info(f"Laddade spaCy-modell: {self.config.spacy_model}")
            self.add_custom_components()
            return True
            
        except Exception as e:
            logger.error(f"Kunde inte ladda spaCy-modell: {str(e)}")
            return False
    
    def load_embedding_model(self) -> bool:
        """
        Ladda modell för embeddings (vektorrepresentationer)
        
        Returns:
            True om laddningen lyckades, annars False
        """
        try:
            # Kolla om transformers är installerat
            if importlib.util.find_spec("transformers") is None:
                logger.warning("transformers är inte installerat. Semantisk sökning kommer att vara begränsad.")
                return False
            
            from transformers import AutoTokenizer, AutoModel
            import torch
            
            # Ladda tokenizer och modell
            tokenizer = AutoTokenizer.from_pretrained(self.config.embeddings_model)
            model = AutoModel.from_pretrained(self.config.embeddings_model)
            
            # Spara som attribut
            self.embedding_tokenizer = tokenizer
            self.embedding_model = model
            
            logger.info(f"Laddade embedding-modell: {self.config.embeddings_model}")
            return True
            
        except Exception as e:
            logger.error(f"Kunde inte ladda embedding-modell: {str(e)}")
            self.embedding_tokenizer = None
            self.embedding_model = None
            return False
    
    def add_custom_components(self) -> None:
        """
        Lägg till anpassade komponenter till spaCy-pipelinen
        """
        if not self.nlp:
            return
        
        try:
            # Kontrollera om entity ruler redan finns
            if not self.nlp.has_pipe("entity_ruler"):
                # Skapa entity ruler med factory-metoden
                ruler = self.nlp.add_pipe("entity_ruler", before="ner")
                
                # Lägg till mönster för produktentiteter
                patterns = [
                    # EAN-mönster
                    {"label": "EAN", "pattern": [{"SHAPE": "dddddddddddd"}]},  # 12-siffrig (UPC)
                    {"label": "EAN", "pattern": [{"SHAPE": "ddddddddddddd"}]},  # 13-siffrig (EAN-13)
                    
                    # Artikelnummermönster
                    {"label": "PRODUCT", "pattern": [
                        {"LOWER": {"IN": ["artikelnr", "art.nr", "artnr", "artikel", "art", "artikelnummer"]}}, 
                        {"IS_PUNCT": True, "OP": "?"}, 
                        {"TEXT": {"REGEX": "[A-Z0-9\\-]{4,15}"}}
                    ]},
                    
                    # Produktmodellmönster
                    {"label": "PRODUCT", "pattern": [
                        {"LOWER": {"IN": ["modell", "model"]}},
                        {"IS_PUNCT": True, "OP": "?"},
                        {"TEXT": {"REGEX": "[A-Z0-9\\-]{2,10}"}}
                    ]},
                    
                    # Dimensionsmönster
                    {"label": "DIMENSION", "pattern": [
                        {"TEXT": {"REGEX": "\\d+(?:[.,]\\d+)?"}}, 
                        {"LOWER": {"IN": ["mm", "cm", "m", "tum", "millimeter", "centimeter", "meter"]}}
                    ]},
                    
                    # Kompatibilitetsmönster
                    {"label": "COMPATIBILITY", "pattern": [
                        {"LOWER": {"IN": ["kompatibel", "passar", "fungerar"]}},
                        {"LOWER": {"IN": ["med", "till", "för", "tillsammans"]}},
                        {"POS": "NOUN"}
                    ]}
                ]
                
                ruler.add_patterns(patterns)
                logger.info("Lade till anpassade entitetsigenkänningskomponenter")
        
        except Exception as e:
            logger.error(f"Fel vid tillägg av anpassade komponenter: {str(e)}")
    
    def preprocess(self, text: str) -> str:
        """
        Förbehandla text innan NLP-analys
        
        Args:
            text: Texten att förbehandla
            
        Returns:
            Förbehandlad text
        """
        # Standardisera whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Normalisera unicode-tecken
        text = unicodedata.normalize('NFKD', text)
        
        # Standardisera punktuation (t.ex. ersätt dubbla streck med enkla)
        text = re.sub(r'--', '-', text)
        text = re.sub(r'\.\.+', '...', text)
        
        # Standardisera citat
        text = re.sub(r'[""„]', '"', text)
        text = re.sub(r'[''`]', "'", text)
        
        return text
    
    def tokenize(self, text: str) -> List[Dict[str, Any]]:
        """
        Tokenisera text i ord och meningar
        
        Args:
            text: Texten att tokenisera
            
        Returns:
            Lista med tokens och deras attribut
        """
        if not self.nlp:
            # Enkel tokenisering om spaCy inte är tillgänglig
            return [{"text": token} for token in text.split()]
        
        doc = self.nlp(text)
        
        # Extrahera token-information
        tokens = []
        for token in doc:
            tokens.append({
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "is_stop": token.is_stop,
                "i": token.i,  # Index inom dokumentet
                "start_char": token.idx,  # Startposition i texten
                "end_char": token.idx + len(token.text)  # Slutposition i texten
            })
        
        return tokens
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Utför fullständig språkanalys på texten
        
        Args:
            text: Texten att analysera
            
        Returns:
            Dict med analysresultat
        """
        if not self.nlp:
            logger.warning("spaCy inte tillgänglig, kan inte utföra fullständig analys")
            return {
                "tokens": self.tokenize(text),
                "entities": [],
                "sentences": [text]
            }
        
        # Preprocessa och analysera
        preprocessed_text = self.preprocess(text)
        doc = self.nlp(preprocessed_text)
        
        # Extrahera entiteter
        entities = []
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "start_char": ent.start_char,
                "end_char": ent.end_char,
                "start_token": ent.start,
                "end_token": ent.end
            })
        
        # Extrahera meningar
        sentences = []
        for sent in doc.sents:
            sentences.append(sent.text)
        
        # Extrahera substantiv och andra viktiga termer
        key_terms = []
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN", "ADJ"] and not token.is_stop:
                key_terms.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "pos": token.pos_
                })
        
        return {
            "tokens": self.tokenize(preprocessed_text),
            "entities": entities,
            "sentences": sentences,
            "key_terms": key_terms
        }
    
    def extract_key_terms(self, text: str) -> List[str]:
        """
        Extrahera nyckeltermer från texten (substantiv, egennamn, etc.)
        
        Args:
            text: Texten att analysera
            
        Returns:
            Lista med nyckeltermer
        """
        if not self.nlp:
            # Enkel extrahering baserat på ordlängd och frekvens
            words = text.lower().split()
            # Filtrera bort korta ord och vanliga stoppord
            stopwords = {"och", "eller", "men", "om", "så", "att", "en", "ett", "den", "det", "de", "i", "på", "med", "för", "till"}
            key_terms = [word for word in words if len(word) > 3 and word not in stopwords]
            return list(set(key_terms))  # Ta bort dubletter
        
        doc = self.nlp(text)
        key_terms = []
        
        for token in doc:
            # Inkludera substantiv, egennamn, adjektiv och siffror
            if (token.pos_ in ["NOUN", "PROPN", "ADJ", "NUM"] and not token.is_stop) or token.ent_type_:
                key_terms.append(token.lemma_)
        
        return list(set(key_terms))  # Ta bort dubletter
    
    def get_embeddings(self, text: str) -> Optional[List[float]]:
        """
        Skapa vektorrepresentation (embedding) för en text
        
        Args:
            text: Texten att skapa embedding för
            
        Returns:
            Vektor som representerar texten eller None om det inte går
        """
        if not self.embedding_model or not self.embedding_tokenizer:
            logger.warning("Embedding-modell inte tillgänglig, kan inte generera vektorrepresentation")
            return None
        
        try:
            import torch
            
            # Tokenisera texten
            inputs = self.embedding_tokenizer(
                text, 
                return_tensors="pt", 
                padding=True, 
                truncation=True, 
                max_length=512
            )
            
            # Generera embeddings
            with torch.no_grad():
                outputs = self.embedding_model(**inputs)
            
            # Använd genomsnitt av sista lagrets hidden states
            embeddings = outputs.last_hidden_state.mean(dim=1)
            
            # Konvertera till lista för enklare serialisering
            return embeddings[0].tolist()
            
        except Exception as e:
            logger.error(f"Fel vid generering av embeddings: {str(e)}")
            return None
    
    def semantic_similarity(self, text1: str, text2: str) -> Optional[float]:
        """
        Beräkna semantisk likhet mellan två texter
        
        Args:
            text1: Första texten
            text2: Andra texten
            
        Returns:
            Likhetsvärde mellan 0 och 1, eller None vid fel
        """
        emb1 = self.get_embeddings(text1)
        emb2 = self.get_embeddings(text2)
        
        if emb1 is None or emb2 is None:
            return None
        
        try:
            import numpy as np
            
            # Konvertera till numpy-arrays
            vec1 = np.array(emb1)
            vec2 = np.array(emb2)
            
            # Beräkna cosine similarity
            dot_product = np.dot(vec1, vec2)
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            
            if norm1 == 0 or norm2 == 0:
                return 0.0
                
            return dot_product / (norm1 * norm2)
            
        except Exception as e:
            logger.error(f"Fel vid beräkning av semantisk likhet: {str(e)}")
            return None
    
    def detect_intent_keywords(self, text: str) -> Dict[str, float]:
        """
        Detektera intention baserat på nyckelord
        
        Args:
            text: Texten att analysera
            
        Returns:
            Dict med intentionstyper och deras sannolikhet
        """
        text_lower = text.lower()
        
        # Intentionsmönster med nyckelord
        intent_patterns = {
            "technical": [
                "teknisk", "specifikation", "mått", "dimension", "vikt", "material",
                "effekt", "spänning", "ström", "hur ser", "hur stor", "hur tung"
            ],
            "compatibility": [
                "passar", "kompatibel", "fungerar med", "kan användas med", "passar till",
                "monteringsstolpe", "trycke", "tillsammans med", "går att använda"
            ],
            "summary": [
                "berätta om", "vad är", "information om", "beskriv", "sammanfatta", 
                "översikt", "produktfakta", "vad betyder", "vad innebär"
            ],
            "search": [
                "hitta", "sök", "leta", "finns det", "har ni", "jag letar efter",
                "jag behöver en", "alternativ till", "liknande"
            ]
        }
        
        # Beräkna matchningspoäng för varje intention
        intent_scores = {}
        
        for intent, keywords in intent_patterns.items():
            score = sum(1.0 for keyword in keywords if keyword in text_lower)
            # Normalisera baserat på antal nyckelord
            normalized_score = score / len(keywords) if score > 0 else 0.0
            intent_scores[intent] = normalized_score
        
        # Om inga träffar, sätt summary som default med låg poäng
        if all(score == 0.0 for score in intent_scores.values()):
            intent_scores["summary"] = 0.1
        
        return intent_scores
```

---

