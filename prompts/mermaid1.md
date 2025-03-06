
Jag ska skapa en detaljerad mermaid-diagram som visualiserar hur modulerna i "./prompts/" fungerar och är kopplade till varandra. Baserat på den kod du delat kan jag konstruera ett omfattande diagram som visar klassrelationer, arv, funktionsanrop och dataflöde.




```mermaid
classDiagram
    %% Huvudklasser
    class PromptTemplate {
        +String template
        +String name
        +String description
        +String version
        +List~String~ tags
        +DateTime creation_time
        +DateTime last_modified
        +int usage_count
        +List usage_history
        +float success_rate
        +int average_latency_ms
        +_validate_template()
        +format(**kwargs)
        +add_example(example)
        +add_context(context)
        +with_instruction(instruction)
        +update_success_rate(success)
        +update_latency(latency_ms)
        +to_dict()
        +to_yaml()
        +save(directory)
        +from_dict(data)
        +from_yaml(yaml_str)
        +load(file_path)
    }

    class ExtractionPrompt {
        +Dict schema
        +String extraction_type
        +Dict required_fields
        +String improved_instructions
        +String error_prevention
        +_extract_required_fields(schema)
        +with_improved_instructions()
        +with_error_prevention()
        +with_examples(examples)
        +for_model(model_name)
    }

    class ValidationPrompt {
        +List~String~ validation_rules
        +with_specific_schema(schema)
        +with_error_detection()
    }

    class CorrectionPrompt {
        +Dict error_types
        +for_errors(specific_errors)
        +with_guidance(guidance_text)
        +with_exemplar_correction(original, corrected, explanation)
    }

    class PromptLoader {
        +load_prompt_from_file(file_path, logger)
        +load_prompts_from_directory(directory, recursive, logger)
        +create_specialized_prompt_from_yaml(file_path, logger)
        +load_default_prompts(logger)
        +save_prompt_to_file(prompt, directory, override, logger)
    }

    class PromptManager {
        +Dict~String, PromptTemplate~ prompts
        +Dict~String, List~ by_tag
        +Dict~String, List~ by_type
        +llm_client
        +bool use_cache
        +Path cache_dir
        +Dict response_cache
        +int cache_hits
        +int cache_misses
        +int max_cache_size
        +set_llm_client(llm_client)
        +register_with_workflow(workflow_manager)
        +dynamic_optimize(extraction_type, sample_texts)
        +setup_caching(cache_dir, max_cache_size)
        +_load_cache()
        +get_cached_response(prompt)
        +cache_response(prompt, response)
        +get_cache_stats()
        +_load_existing_prompts()
        +add_prompt(prompt)
        +_get_prompt_type(prompt)
        +get_prompt(name)
        +get_prompts_by_tag(tag)
        +get_prompts_by_type(prompt_type)
        +save_prompt(prompt)
        +save_all()
        +delete_prompt(name)
        +update_usage_statistics(name, success, latency_ms)
        +get_best_prompt(tags, min_success_rate)
        +create_variant(base_name, variant_suffix, modifications)
        +list_prompts(filter_tag)
        +compare_prompt_versions(base_name)
        +optimize_prompt(name)
        +merge_prompts(primary_name, secondary_name, merged_name)
        +visualize_prompt_performance(visualizer)
        +export_statistics(file_path)
        +export_to_markdown(file_path)
        +get_similar_prompts(name, max_count)
    }

    %% Moduler
    class prompt_utils {
        +enhance_prompt_with_examples(prompt_template, examples)
        +create_specialized_prompt(base_prompt, focus_area, additional_instructions)
        +fix_json_format(json_text)
        +extract_schema_from_json(json_example)
        +extract_json_from_text(text)
        +improve_prompt_based_on_feedback(prompt_template, feedback)
        +create_conditional_prompt(base_prompt, condition_text, alternate_instruction)
    }

    class __init__ {
        +__version__
        +__author__
        +__all__
    }

    %% YAML-filer
    class default_yaml {
        Schema och mall för extraktion
    }
    
    class error_yaml {
        Schema och mall för korrigering
    }
    
    class validation_yaml {
        Schema och mall för validering
    }
    
    class default_validation_yaml {
        Standardmall för validering
    }

    %% Arvsrelationer
    PromptTemplate <|-- ExtractionPrompt
    PromptTemplate <|-- ValidationPrompt
    PromptTemplate <|-- CorrectionPrompt

    %% Associationer
    PromptManager --> PromptTemplate : hanterar
    PromptManager --> PromptLoader : använder
    PromptLoader --> PromptTemplate : skapar
    PromptLoader --> ExtractionPrompt : skapar
    PromptLoader --> ValidationPrompt : skapar
    PromptLoader --> CorrectionPrompt : skapar
    
    %% Användarrelationer mellan moduler
    prompt_utils --> PromptTemplate : manipulerar
    prompt_utils --> ExtractionPrompt : manipulerar
    prompt_utils --> ValidationPrompt : manipulerar
    prompt_utils --> CorrectionPrompt : manipulerar
    
    %% Filrelationer
    PromptLoader --> default_yaml : laddar
    PromptLoader --> error_yaml : laddar
    PromptLoader --> validation_yaml : laddar
    PromptLoader --> default_validation_yaml : laddar
    
    %% __init__ relation
    __init__ --> PromptTemplate : exporterar
    __init__ --> ExtractionPrompt : exporterar
    __init__ --> ValidationPrompt : exporterar
    __init__ --> CorrectionPrompt : exporterar
    __init__ --> PromptLoader : exporterar
    __init__ --> PromptManager : exporterar
    __init__ --> prompt_utils : exporterar funktioner

    %% Externa integrationer
    class LLMClient {
        +get_completion(prompt)
        +response_parser
    }
    
    class WorkflowManager {
        +prompt_manager
        +processor
    }
    
    class Visualizer {
        +display_table(headers, rows, title)
        +display_markdown(markdown)
    }
    
    PromptManager --> LLMClient : använder
    PromptManager --> Visualizer : använder
    WorkflowManager --> PromptManager : integrerar med

```





För att göra diagrammet ännu tydligare, låt mig skapa en kompletterande diagram som fokuserar på dataflödet och processerna i systemet:

```mermaid
flowchart TD
    %% Huvudprocesser
    subgraph PromptManagement [Prompthantering]
        Load[Ladda Promptmallar]
        Create[Skapa Promptmallar]
        Modify[Modifiera Promptmallar]
        Use[Använda Promptmallar]
        Cache[Cacha Promptsvar]
        Optimize[Optimera Promptar]
        Export[Exportera Statistik]
    end

    %% Datakällor
    subgraph Storage [Lagring]
        YAML[YAML-filer]
        DefaultTemplates[Fördefinierade Mallar]
        CacheStorage[Cache-lagring]
    end

    %% Externa komponenter
    subgraph External [Externa System]
        LLM[LLM-klient]
        Workflow[Arbetsflödeshanterare]
        Logger[Logger]
        Vis[Visualizer]
    end

    %% Prompt-typer
    subgraph PromptTypes [Prompt-typer]
        Basic[Bas PromptTemplate]
        Extract[ExtractionPrompt]
        Validate[ValidationPrompt]
        Correct[CorrectionPrompt]
    end
    
    %% Utils
    subgraph Utils [Hjälpfunktioner]
        EnhanceExamples[enhance_prompt_with_examples]
        CreateSpecialized[create_specialized_prompt]
        FixJSON[fix_json_format]
        ExtractSchema[extract_schema_from_json]
        ExtractJSON[extract_json_from_text]
        ImproveFeedback[improve_prompt_based_on_feedback]
        CreateConditional[create_conditional_prompt]
    end

    %% Processer och dataflöden för laddning
    YAML --> Load
    DefaultTemplates --> Load
    Load --> Create
    
    %% Skapande och modifiering av mallar
    Create --> Basic
    Create --> Extract
    Create --> Validate
    Create --> Correct
    Basic --> Modify
    Extract --> Modify
    Validate --> Modify
    Correct --> Modify
    
    %% Användning av mallar
    Basic --> Use
    Extract --> Use
    Validate --> Use
    Correct --> Use
    Use --> Cache
    Cache --> CacheStorage
    CacheStorage --> Cache
    
    %% Optimering
    Use --> Optimize
    Optimize --> Basic
    Optimize --> Extract
    Optimize --> Validate
    Optimize --> Correct
    
    %% Statistik och export
    Use --> Export
    Export --> YAML
    
    %% Externa integrationer
    LLM <--> Use
    Workflow <--> Use
    Logger --> Load
    Logger --> Use
    Logger --> Optimize
    Vis <--> Export
    
    %% Utils kopplingar
    EnhanceExamples --> Modify
    CreateSpecialized --> Modify
    FixJSON --> Use
    ExtractSchema --> Create
    ExtractJSON --> Use
    ImproveFeedback --> Optimize
    CreateConditional --> Modify

    %% Huvud dataflöden och processer
    subgraph MainFlow [Huvudflöde]
        direction LR
        Init[Initialisering] --> LoadPromptsFlow[Ladda Promptar]
        LoadPromptsFlow --> ConfigureFlow[Konfigurera Manager]
        ConfigureFlow --> UsePromptFlow[Använda Prompt]
        UsePromptFlow --> OptimizeFlow[Optimera Prompt]
        OptimizeFlow --> ExportFlow[Exportera Statistik]
    end
    
    %% Detaljerade processer
    subgraph DetailedFlow [Detaljerat flöde för en prompt]
        direction TB
        LoadTemplate[Ladda mall] --> FormatPrompt[Formatera prompt]
        FormatPrompt --> SendToLLM[Skicka till LLM]
        SendToLLM --> ValidateResponse[Validera svar]
        ValidateResponse --> CorrectErrors[Korrigera fel om nödvändigt]
        CorrectErrors --> UpdateStats[Uppdatera statistik]
    end

    MainFlow -.-> PromptManagement
    DetailedFlow -.-> Use

```













