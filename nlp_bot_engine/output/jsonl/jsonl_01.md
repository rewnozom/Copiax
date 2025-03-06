# Project Details

# Table of Contents
- [..\data\extracted_data\products\50025313\50025313_compatibility.jsonl](#-data-extracted_data-products-50025313-50025313_compatibilityjsonl)
- [..\data\extracted_data\products\50025313\50025313_data.json](#-data-extracted_data-products-50025313-50025313_datajson)
- [..\data\extracted_data\products\50025313\50025313_identifiers.jsonl](#-data-extracted_data-products-50025313-50025313_identifiersjsonl)
- [..\data\extracted_data\products\50025313\50025313_specifications.jsonl](#-data-extracted_data-products-50025313-50025313_specificationsjsonl)
- [..\data\extracted_data\products\50025313\50025313_summary.json](#-data-extracted_data-products-50025313-50025313_summaryjson)
- [..\data\extracted_data\reports\extraction_quality_20250305_221242.json](#-data-extracted_data-reports-extraction_quality_20250305_221242json)
- [..\data\extracted_data\reports\extraction_report_20250305_221242.md](#-data-extracted_data-reports-extraction_report_20250305_221242md)
- [..\data\extracted_data\reports\extraction_stats_20250305_221242.json](#-data-extracted_data-reports-extraction_stats_20250305_221242json)
- [..\data\integrated_data\bot_responses\50025313\compatibility_response.json](#-data-integrated_data-bot_responses-50025313-compatibility_responsejson)
- [..\data\integrated_data\bot_responses\50025313\summary_response.json](#-data-integrated_data-bot_responses-50025313-summary_responsejson)
- [..\data\integrated_data\bot_responses\50025313\technical_response.json](#-data-integrated_data-bot_responses-50025313-technical_responsejson)
- [..\data\integrated_data\indices\article_numbers.json](#-data-integrated_data-indices-article_numbersjson)
- [..\data\integrated_data\indices\compatibility_map.json](#-data-integrated_data-indices-compatibility_mapjson)
- [..\data\integrated_data\indices\ean_numbers.json](#-data-integrated_data-indices-ean_numbersjson)
- [..\data\integrated_data\indices\technical_specs_index.json](#-data-integrated_data-indices-technical_specs_indexjson)
- [..\data\integrated_data\indices\text_search_index.json](#-data-integrated_data-indices-text_search_indexjson)
- [..\data\integrated_data\products\50025313\article_info.jsonl](#-data-integrated_data-products-50025313-article_infojsonl)
- [..\data\integrated_data\products\50025313\compatibility.jsonl](#-data-integrated_data-products-50025313-compatibilityjsonl)
- [..\data\integrated_data\products\50025313\full_info.md](#-data-integrated_data-products-50025313-full_infomd)
- [..\data\integrated_data\products\50025313\summary.jsonl](#-data-integrated_data-products-50025313-summaryjsonl)
- [..\data\integrated_data\products\50025313\technical_specs.jsonl](#-data-integrated_data-products-50025313-technical_specsjsonl)


# ..\..\data\extracted_data\products\50025313\50025313_compatibility.jsonl
## File: ..\..\data\extracted_data\products\50025313\50025313_compatibility.jsonl

```jsonl
# ..\..\data\extracted_data\products\50025313\50025313_compatibility.jsonl
{"relation_type": "fits", "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art", "numeric_ids": [], "context": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare", "confidence": 0.8, "source_text": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare", "source_location": "", "extracted_method": "regex"}

```

---

# ..\..\data\extracted_data\products\50025313\50025313_data.json
## File: ..\..\data\extracted_data\products\50025313\50025313_data.json

```json
# ..\..\data\extracted_data\products\50025313\50025313_data.json
{
  "product_id": "50025313",
  "file_path": "test_docs\\50025313_pro\\50025313_pro.md",
  "filename": "50025313_pro.md",
  "product_name": "Produkt 50025313",
  "product_description": "• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269",
  "identifiers": [
    {
      "type": "EAN-13",
      "value": "7320896000544",
      "confidence": 0.9,
      "source_text": "onshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB",
      "source_location": "",
      "extracted_method": "regex",
      "is_valid": true,
      "validation_message": ""
    },
    {
      "type": "EAN-8",
      "value": "43131495",
      "confidence": 0.9,
      "source_text": "--------------|------------|--| | Statistiskt nummer | 8424908080 | | | E-nummer | 1693269 | | | EL-nr | 6209317 | | | Snro | 6411723 | | | Nobb-nr | 43131495 | | ## **Packaging information** | | EXKRT | PALL | ST | |--------------------|----------|-----------|---------------| | EAN kod | | | 73208960005",
      "source_location": "",
      "extracted_method": "regex",
      "is_valid": true,
      "validation_message": ""
    },
    {
      "type": "ARTICLE_NUMBER",
      "value": "1693269",
      "confidence": 0.85,
      "source_text": "g pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ## **Technic",
      "source_location": "",
      "extracted_method": "regex",
      "is_valid": true,
      "validation_message": ""
    }
  ],
  "specifications": [
    {
      "category": "WEIGHT",
      "name": "kg",
      "raw_value": "6",
      "unit": "GE",
      "normalized_value": 6.0,
      "confidence": 0.85,
      "importance": "normal",
      "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!",
      "source_location": "",
      "extracted_method": "nlp_phrase_matcher"
    },
    {
      "category": "DIMENSIONS",
      "name": "Längd",
      "raw_value": "540.000",
      "unit": "",
      "normalized_value": 540.0,
      "confidence": 0.85,
      "importance": "normal",
      "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
      "source_location": "",
      "extracted_method": "nlp_phrase_matcher"
    },
    {
      "category": "DIMENSIONS",
      "name": "Höjd",
      "raw_value": "380.000",
      "unit": "",
      "normalized_value": 380.0,
      "confidence": 0.85,
      "importance": "normal",
      "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
      "source_location": "",
      "extracted_method": "nlp_phrase_matcher"
    },
    {
      "category": "DIMENSIONS",
      "name": "Bredd",
      "raw_value": "240.000",
      "unit": "",
      "normalized_value": 240.0,
      "confidence": 0.85,
      "importance": "normal",
      "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
      "source_location": "",
      "extracted_method": "nlp_phrase_matcher"
    },
    {
      "category": "WEIGHT",
      "name": "kg",
      "raw_value": "26.05000",
      "unit": "",
      "normalized_value": 26.05,
      "confidence": 0.85,
      "importance": "normal",
      "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|",
      "source_location": "",
      "extracted_method": "nlp_phrase_matcher"
    }
  ],
  "compatibility": [
    {
      "relation_type": "fits",
      "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art",
      "numeric_ids": [],
      "context": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare",
      "confidence": 0.8,
      "source_text": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare",
      "source_location": "",
      "extracted_method": "regex"
    }
  ],
  "content_sample": "![](_page_0_Picture_1.jpeg)\n\n## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n![](_page_0_Picture_3.jpeg)\n\nPassar till PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269\n\n![](_page_0_Picture_6.jpeg)\n\n![](_page_0_Picture_8.jpeg)\n\n• *Page 1/2**\n\n## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n## **Technical specifikation**\n\n\n| Tillverkningsland | Kina | |\n|--------------------|------------|--|\n| Statistiskt nummer | 8424908080 | |\n| E-nummer | 1693269 | |\n| EL-nr | 6209317 | |\n| Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n| Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.000",
  "metadata": {
    "extraction_timestamp": "20250305_235339",
    "sections": [
      "full_content",
      "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE",
      "Technical specifikation",
      "Packaging information"
    ],
    "extraction_methods": {
      "nlp_available": true,
      "identifier_methods": {
        "regex": 3
      },
      "specification_methods": {
        "nlp_phrase_matcher": 5
      },
      "compatibility_methods": {
        "regex": 1
      }
    }
  }
}
```

---

# ..\..\data\extracted_data\products\50025313\50025313_identifiers.jsonl
## File: ..\..\data\extracted_data\products\50025313\50025313_identifiers.jsonl

```jsonl
# ..\..\data\extracted_data\products\50025313\50025313_identifiers.jsonl
{"type": "EAN-13", "value": "7320896000544", "confidence": 0.9, "source_text": "onshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": ""}
{"type": "EAN-8", "value": "43131495", "confidence": 0.9, "source_text": "--------------|------------|--| | Statistiskt nummer | 8424908080 | | | E-nummer | 1693269 | | | EL-nr | 6209317 | | | Snro | 6411723 | | | Nobb-nr | 43131495 | | ## **Packaging information** | | EXKRT | PALL | ST | |--------------------|----------|-----------|---------------| | EAN kod | | | 73208960005", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": ""}
{"type": "ARTICLE_NUMBER", "value": "1693269", "confidence": 0.85, "source_text": "g pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ## **Technic", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": ""}

```

---

# ..\..\data\extracted_data\products\50025313\50025313_specifications.jsonl
## File: ..\..\data\extracted_data\products\50025313\50025313_specifications.jsonl

```jsonl
# ..\..\data\extracted_data\products\50025313\50025313_specifications.jsonl
{"category": "WEIGHT", "name": "kg", "raw_value": "6", "unit": "GE", "normalized_value": 6.0, "confidence": 0.85, "importance": "normal", "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!", "source_location": "", "extracted_method": "nlp_phrase_matcher"}
{"category": "DIMENSIONS", "name": "Längd", "raw_value": "540.000", "unit": "", "normalized_value": 540.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher"}
{"category": "DIMENSIONS", "name": "Höjd", "raw_value": "380.000", "unit": "", "normalized_value": 380.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher"}
{"category": "DIMENSIONS", "name": "Bredd", "raw_value": "240.000", "unit": "", "normalized_value": 240.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher"}
{"category": "WEIGHT", "name": "kg", "raw_value": "26.05000", "unit": "", "normalized_value": 26.05, "confidence": 0.85, "importance": "normal", "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher"}

```

---

# ..\..\data\extracted_data\products\50025313\50025313_summary.json
## File: ..\..\data\extracted_data\products\50025313\50025313_summary.json

```json
# ..\..\data\extracted_data\products\50025313\50025313_summary.json
{
  "product_id": "50025313",
  "product_name": "Produkt 50025313",
  "description": "• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269",
  "file_path": "test_docs\\50025313_pro\\50025313_pro.md",
  "identifier_count": 3,
  "specification_count": 5,
  "compatibility_count": 1,
  "extraction_timestamp": "20250305_235339"
}
```

---

# File: ..\..\data\extracted_data\reports\extraction_quality_20250305_221242.json

**Binary file cannot be displayed.**

---

# File: ..\..\data\extracted_data\reports\extraction_report_20250305_221242.md

**Binary file cannot be displayed.**

---

# File: ..\..\data\extracted_data\reports\extraction_stats_20250305_221242.json

**Binary file cannot be displayed.**

---

# ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
## File: ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json

```json
# ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
{
    "product_id": "50025313",
    "command": "-c",
    "timestamp": "2025-03-05T23:53:41.377738",
    "product_name": "Produkt 50025313",
    "has_compatibility_info": true,
    "compatibility_groups": {
        "Passar till": [
            {
                "relation_type": "fits",
                "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art",
                "numeric_ids": [],
                "context": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare",
                "confidence": 0.8,
                "source_text": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare",
                "source_location": "",
                "extracted_method": "regex"
            }
        ]
    },
    "related_products": [
        {
            "related_product_id": null,
            "relation_type": "fits",
            "name": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art",
            "numeric_ids": [],
            "notes": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare"
        }
    ],
    "markdown_response": "# Kompatibilitetsinformation för Produkt 50025313\n\n**Artikelnummer:** 50025313\n**EAN:** 7320896000544, 43131495\n\n## Passar till\n\n- PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art\n"
}
```

---

# ..\..\data\integrated_data\bot_responses\50025313\summary_response.json
## File: ..\..\data\integrated_data\bot_responses\50025313\summary_response.json

```json
# ..\..\data\integrated_data\bot_responses\50025313\summary_response.json
{
    "product_id": "50025313",
    "command": "-s",
    "timestamp": "2025-03-05T23:53:41.377738",
    "product_name": "Produkt 50025313",
    "summary_data": {
        "product_id": "50025313",
        "generated_at": "20250305_235339",
        "product_name": "Produkt 50025313",
        "description": "• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269",
        "key_specifications": [
            {
                "category": "WEIGHT",
                "name": "kg",
                "value": "6",
                "unit": "GE"
            },
            {
                "category": "WEIGHT",
                "name": "kg",
                "value": "26.05000",
                "unit": ""
            },
            {
                "category": "DIMENSIONS",
                "name": "Längd",
                "value": "540.000",
                "unit": ""
            },
            {
                "category": "DIMENSIONS",
                "name": "Höjd",
                "value": "380.000",
                "unit": ""
            }
        ],
        "key_compatibility": [
            {
                "type": "fits",
                "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art",
                "has_product_id": false,
                "numeric_ids": []
            }
        ],
        "identifiers": {
            "EAN-13": [
                "7320896000544"
            ],
            "EAN-8": [
                "43131495"
            ],
            "ARTICLE_NUMBER": [
                "1693269"
            ]
        }
    },
    "markdown_response": "# Produkt 50025313\n\n**Artikelnummer:** 50025313\n**EAN-13:** 7320896000544\n**EAN-8:** 43131495\n**ARTICLE_NUMBER:** 1693269\n\n• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269\n\n## Tekniska specifikationer\n\n- **kg:** 6 GE\n- **kg:** 26.05000\n- **Längd:** 540.000\n- **Höjd:** 380.000\n\n## Kompatibilitet\n\n### Passar till\n\n- PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art\n"
}
```

---

# ..\..\data\integrated_data\bot_responses\50025313\technical_response.json
## File: ..\..\data\integrated_data\bot_responses\50025313\technical_response.json

```json
# ..\..\data\integrated_data\bot_responses\50025313\technical_response.json
{
    "product_id": "50025313",
    "command": "-t",
    "timestamp": "2025-03-05T23:53:41.377738",
    "product_name": "Produkt 50025313",
    "has_technical_info": true,
    "technical_categories": {
        "WEIGHT": [
            {
                "category": "WEIGHT",
                "name": "kg",
                "raw_value": "6",
                "unit": "GE",
                "normalized_value": 6.0,
                "confidence": 0.85,
                "importance": "normal",
                "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!",
                "source_location": "",
                "extracted_method": "nlp_phrase_matcher"
            },
            {
                "category": "WEIGHT",
                "name": "kg",
                "raw_value": "26.05000",
                "unit": "",
                "normalized_value": 26.05,
                "confidence": 0.85,
                "importance": "normal",
                "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|",
                "source_location": "",
                "extracted_method": "nlp_phrase_matcher"
            }
        ],
        "DIMENSIONS": [
            {
                "category": "DIMENSIONS",
                "name": "Längd",
                "raw_value": "540.000",
                "unit": "",
                "normalized_value": 540.0,
                "confidence": 0.85,
                "importance": "normal",
                "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
                "source_location": "",
                "extracted_method": "nlp_phrase_matcher"
            },
            {
                "category": "DIMENSIONS",
                "name": "Höjd",
                "raw_value": "380.000",
                "unit": "",
                "normalized_value": 380.0,
                "confidence": 0.85,
                "importance": "normal",
                "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
                "source_location": "",
                "extracted_method": "nlp_phrase_matcher"
            },
            {
                "category": "DIMENSIONS",
                "name": "Bredd",
                "raw_value": "240.000",
                "unit": "",
                "normalized_value": 240.0,
                "confidence": 0.85,
                "importance": "normal",
                "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
                "source_location": "",
                "extracted_method": "nlp_phrase_matcher"
            }
        ]
    },
    "all_specifications": [
        {
            "category": "WEIGHT",
            "name": "kg",
            "raw_value": "6",
            "unit": "GE",
            "normalized_value": 6.0,
            "confidence": 0.85,
            "importance": "normal",
            "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!",
            "source_location": "",
            "extracted_method": "nlp_phrase_matcher"
        },
        {
            "category": "DIMENSIONS",
            "name": "Längd",
            "raw_value": "540.000",
            "unit": "",
            "normalized_value": 540.0,
            "confidence": 0.85,
            "importance": "normal",
            "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
            "source_location": "",
            "extracted_method": "nlp_phrase_matcher"
        },
        {
            "category": "DIMENSIONS",
            "name": "Höjd",
            "raw_value": "380.000",
            "unit": "",
            "normalized_value": 380.0,
            "confidence": 0.85,
            "importance": "normal",
            "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
            "source_location": "",
            "extracted_method": "nlp_phrase_matcher"
        },
        {
            "category": "DIMENSIONS",
            "name": "Bredd",
            "raw_value": "240.000",
            "unit": "",
            "normalized_value": 240.0,
            "confidence": 0.85,
            "importance": "normal",
            "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
            "source_location": "",
            "extracted_method": "nlp_phrase_matcher"
        },
        {
            "category": "WEIGHT",
            "name": "kg",
            "raw_value": "26.05000",
            "unit": "",
            "normalized_value": 26.05,
            "confidence": 0.85,
            "importance": "normal",
            "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|",
            "source_location": "",
            "extracted_method": "nlp_phrase_matcher"
        }
    ],
    "markdown_response": "# Tekniska specifikationer för Produkt 50025313\n\n**Artikelnummer:** 50025313\n**EAN:** 7320896000544, 43131495\n\n## WEIGHT\n\n- **kg:** 6 GE\n- **kg:** 26.05000\n\n## DIMENSIONS\n\n- **Längd:** 540.000\n- **Höjd:** 380.000\n- **Bredd:** 240.000\n"
}
```

---

# ..\..\data\integrated_data\indices\article_numbers.json
## File: ..\..\data\integrated_data\indices\article_numbers.json

```json
# ..\..\data\integrated_data\indices\article_numbers.json
{
  "1693269": [
    {
      "product_id": "50025313",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240068": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240067": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240001": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240002": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213168": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213169": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240041": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240042": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213170": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213171": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5255012": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5255013": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240000": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240064": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240065": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240069": [
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    }
  ]
}
```

---

# ..\..\data\integrated_data\indices\compatibility_map.json
## File: ..\..\data\integrated_data\indices\compatibility_map.json

```json
# ..\..\data\integrated_data\indices\compatibility_map.json
{
  "50025313": [
    {
      "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art",
      "relation_type": "fits",
      "numeric_ids": []
    }
  ],
  "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art": [
    {
      "related_product": "50025313",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "50464764": [
    {
      "related_product": "UPS:ER\n\n\n| UPS | Artikelnummer |",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "rensa tidigare batterikapacitet",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "följande UPS:er 4 | |\n| 3",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "följande UPS:er \\[4\\]](#page-3-0) UPS:er denna batteribox passar till",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "FÖLJANDE UPS:ER\n\n\n| UPS | Artikelnummer |\n|---------------------------------|----------------|\n| SIN 600W FLX L | FL01U0021FP006 |\n| SIN 1100W FLX L | FL01U0031FP011 |\n| SIN 1500W FLX L | FL01U0031FP015 |\n| TEL-1200W-STS-SIN2* | 5144 |\n| *Säljs ej direkt av Milleteknik | |\n\n# 3",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "enheten rensa tidigare batterikapacitet",
      "relation_type": "requires",
      "numeric_ids": []
    }
  ],
  "följande UPS:er 4 | |\n| 3": [
    {
      "related_product": "50464764",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "följande UPS:er \\[4\\]](#page-3-0) UPS:er denna batteribox passar till": [
    {
      "related_product": "50464764",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "FÖLJANDE UPS:ER\n\n\n| UPS | Artikelnummer |\n|---------------------------------|----------------|\n| SIN 600W FLX L | FL01U0021FP006 |\n| SIN 1100W FLX L | FL01U0031FP011 |\n| SIN 1500W FLX L | FL01U0031FP015 |\n| TEL-1200W-STS-SIN2* | 5144 |\n| *Säljs ej direkt av Milleteknik | |\n\n# 3": [
    {
      "related_product": "50464764",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "50108133": [
    {
      "related_product": "följande PSV-modeller |\n|---------|-------------|---------|-----------------------------------|\n| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |\n| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |\n| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |\n| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |\n\n## Spänningsfall i ledningsnätet?\n\n\n![](_page_3_Picture_1",
      "relation_type": "fits",
      "numeric_ids": [
        "20721",
        "5230060",
        "21202",
        "5230061",
        "21805",
        "5230062",
        "24207",
        "5230063"
      ]
    },
    {
      "related_product": "inte ändras\n## Behövs mer ström?\n\n\n![](_page_3_Picture_6",
      "relation_type": "requires",
      "numeric_ids": []
    }
  ],
  "följande PSV-modeller |\n|---------|-------------|---------|-----------------------------------|\n| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |\n| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |\n| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |\n| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |\n\n## Spänningsfall i ledningsnätet?\n\n\n![](_page_3_Picture_1": [
    {
      "related_product": "50108133",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50107533",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50107532",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "50107533": [
    {
      "related_product": "följande PSV-modeller |\n|---------|-------------|---------|-----------------------------------|\n| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |\n| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |\n| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |\n| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |\n\n## Spänningsfall i ledningsnätet?\n\n\n![](_page_3_Picture_1",
      "relation_type": "fits",
      "numeric_ids": [
        "20721",
        "5230060",
        "21202",
        "5230061",
        "21805",
        "5230062",
        "24207",
        "5230063"
      ]
    },
    {
      "related_product": "inte ändras\n## Behövs mer ström?\n\n\n![](_page_3_Picture_6",
      "relation_type": "requires",
      "numeric_ids": []
    }
  ],
  "50107532": [
    {
      "related_product": "följande PSV-modeller |\n|---------|-------------|---------|-----------------------------------|\n| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |\n| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |\n| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |\n| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |\n\n## Spänningsfall i ledningsnätet?\n\n\n![](_page_3_Picture_1",
      "relation_type": "fits",
      "numeric_ids": [
        "20721",
        "5230060",
        "21202",
        "5230061",
        "21805",
        "5230062",
        "24207",
        "5230063"
      ]
    },
    {
      "related_product": "inte ändras\n## Behövs mer ström?\n\n\n![](_page_3_Picture_6",
      "relation_type": "requires",
      "numeric_ids": []
    }
  ]
}
```

---

# ..\..\data\integrated_data\indices\ean_numbers.json
## File: ..\..\data\integrated_data\indices\ean_numbers.json

```json
# ..\..\data\integrated_data\indices\ean_numbers.json
{
  "7320896000544": [
    {
      "product_id": "50025313",
      "id_type": "EAN-13"
    }
  ],
  "43131495": [
    {
      "product_id": "50025313",
      "id_type": "EAN-8"
    }
  ]
}
```

---

# ..\..\data\integrated_data\indices\technical_specs_index.json
## File: ..\..\data\integrated_data\indices\technical_specs_index.json

```json
# ..\..\data\integrated_data\indices\technical_specs_index.json
{
  "WEIGHT": [
    {
      "product_id": "50025313",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "6",
        "unit": "GE",
        "normalized_value": 6.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50025313"
      }
    },
    {
      "product_id": "50025313",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "26.05000",
        "unit": "",
        "normalized_value": 26.05,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50025313"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "113",
        "unit": "",
        "normalized_value": 113.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Vikt per<br>styck |",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    }
  ],
  "DIMENSIONS": [
    {
      "product_id": "50025313",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Längd",
        "raw_value": "540.000",
        "unit": "",
        "normalized_value": 540.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50025313"
      }
    },
    {
      "product_id": "50025313",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Höjd",
        "raw_value": "380.000",
        "unit": "",
        "normalized_value": 380.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50025313"
      }
    },
    {
      "product_id": "50025313",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Bredd",
        "raw_value": "240.000",
        "unit": "",
        "normalized_value": 240.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50025313"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Height",
        "raw_value": "224 mm",
        "unit": "mm",
        "normalized_value": 224.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Height",
        "raw_value": "438 mm",
        "unit": "mm",
        "normalized_value": 438.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Height",
        "raw_value": "212 mm",
        "unit": "mm",
        "normalized_value": 212.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "197x165x170 mm",
        "unit": "mm",
        "normalized_value": 197.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Fabrikat |\n|----------------|----------|----------------------------------------------|--------------|----------------------------|-------------------|----------|\n| MT113-12V45-01 | 5230546 | UPLUS 12V 45Ah<br>10+ Design life<br>batteri | M6 Bult | 197x165x170 mm | 14,5 kg | UPLUS |\n\n•",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Mått",
        "raw_value": "224",
        "unit": "mm",
        "normalized_value": 224.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått |",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Höjd",
        "raw_value": "224",
        "unit": "mm",
        "normalized_value": 224.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "bredd",
        "raw_value": "438",
        "unit": "mm",
        "normalized_value": 438.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "djup",
        "raw_value": "212",
        "unit": "mm",
        "normalized_value": 212.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd: 224 mm, bredd 438 mm, djup 212 mm | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50464764",
      "spec": {
        "category": "DIMENSIONS",
        "name": "djup",
        "raw_value": "113",
        "unit": "",
        "normalized_value": 113.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Höjd, bredd,<br>djup |",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50464764"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "325x276x90 mm",
        "unit": "mm",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "345x325x130 mm",
        "unit": "mm",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "400x425x200 mm",
        "unit": "mm",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "300x230x100mm",
        "unit": "mm",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "35 mm",
        "unit": "mm",
        "normalized_value": 35.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "[](_page_2_Picture_7.jpeg)\n\n• *Enhet med 40Ah batterier**\n\n#### **Kundstyrd design av strömförsörjningsutrustning**\n\n\nEfter kundens önskemål gör vi också strömförsörjningsenheter som har plats för kundens egen utrustning på 35 mm DIN-rail.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "210x120x70mm",
        "unit": "mm",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "325",
        "unit": "x",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "345",
        "unit": "x",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "400",
        "unit": "x",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "300",
        "unit": "x",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "122",
        "unit": "",
        "normalized_value": 122.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Model | Beskrivning | Storlek<br>(BxHxD mm) |\n|------------|-----------------------------|-----------------------|\n| Box",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "210",
        "unit": "x",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "325x276x90 mm",
        "unit": "mm",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "345x325x130 mm",
        "unit": "mm",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "400x425x200 mm",
        "unit": "mm",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "300x230x100mm",
        "unit": "mm",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "35 mm",
        "unit": "mm",
        "normalized_value": 35.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "[](_page_2_Picture_7.jpeg)\n\n• *Enhet med 40Ah batterier**\n\n#### **Kundstyrd design av strömförsörjningsutrustning**\n\n\nEfter kundens önskemål gör vi också strömförsörjningsenheter som har plats för kundens egen utrustning på 35 mm DIN-rail.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "210x120x70mm",
        "unit": "mm",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "325",
        "unit": "x",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "345",
        "unit": "x",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "400",
        "unit": "x",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "300",
        "unit": "x",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "122",
        "unit": "",
        "normalized_value": 122.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Model | Beskrivning | Storlek<br>(BxHxD mm) |\n|------------|-----------------------------|-----------------------|\n| Box",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "210",
        "unit": "x",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "325x276x90 mm",
        "unit": "mm",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "345x325x130 mm",
        "unit": "mm",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "400x425x200 mm",
        "unit": "mm",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "300x230x100mm",
        "unit": "mm",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "35 mm",
        "unit": "mm",
        "normalized_value": 35.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "[](_page_2_Picture_7.jpeg)\n\n• *Enhet med 40Ah batterier**\n\n#### **Kundstyrd design av strömförsörjningsutrustning**\n\n\nEfter kundens önskemål gör vi också strömförsörjningsenheter som har plats för kundens egen utrustning på 35 mm DIN-rail.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "210x120x70mm",
        "unit": "mm",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "325",
        "unit": "x",
        "normalized_value": 325.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 325x276x90 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "345",
        "unit": "x",
        "normalized_value": 345.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 345x325x130 mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "400",
        "unit": "x",
        "normalized_value": 400.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 400x425x200 mm",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "300",
        "unit": "x",
        "normalized_value": 300.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 300x230x100mm\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "122",
        "unit": "",
        "normalized_value": 122.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Model | Beskrivning | Storlek<br>(BxHxD mm) |\n|------------|-----------------------------|-----------------------|\n| Box",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Storlek",
        "raw_value": "210",
        "unit": "x",
        "normalized_value": 210.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Storlek (BxHxD) 210x120x70mm.\n\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    }
  ],
  "ELECTRICAL": [
    {
      "product_id": "50108133",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "2",
        "unit": "st",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt med plats för 2 st.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "1",
        "unit": "st",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 12 Volt med plats för 1st 18Ah batteri**\n\n\nUtspänning 13,8V i vit metallåda med plats för 1st blyackumulator 12V/18Ah.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50108133",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "27,6",
        "unit": "V",
        "normalized_value": 27.6,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt**\n\nUtspänning 27,6 V i vit metallåda\n\nStorlek (BxHxD)",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50108133"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "2",
        "unit": "st",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt med plats för 2 st.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "1",
        "unit": "st",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 12 Volt med plats för 1st 18Ah batteri**\n\n\nUtspänning 13,8V i vit metallåda med plats för 1st blyackumulator 12V/18Ah.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107533",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "27,6",
        "unit": "V",
        "normalized_value": 27.6,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt**\n\nUtspänning 27,6 V i vit metallåda\n\nStorlek (BxHxD)",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107533"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "2",
        "unit": "st",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt med plats för 2 st.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "1",
        "unit": "st",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 12 Volt med plats för 1st 18Ah batteri**\n\n\nUtspänning 13,8V i vit metallåda med plats för 1st blyackumulator 12V/18Ah.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    },
    {
      "product_id": "50107532",
      "spec": {
        "category": "ELECTRICAL",
        "name": "Volt",
        "raw_value": "27,6",
        "unit": "V",
        "normalized_value": 27.6,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Enheter för 24 Volt**\n\nUtspänning 27,6 V i vit metallåda\n\nStorlek (BxHxD)",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50107532"
      }
    }
  ]
}
```

---

# ..\..\data\integrated_data\indices\text_search_index.json
## File: ..\..\data\integrated_data\indices\text_search_index.json

```json
# ..\..\data\integrated_data\indices\text_search_index.json
{
  "page": [
    "50025313",
    "50464764"
  ],
  "passar": [
    "50025313",
    "50464764"
  ],
  "exkrt": [
    "50025313"
  ],
  "pe6tea": [
    "50025313"
  ],
  "net": [
    "50025313"
  ],
  "produkt": [
    "50025313"
  ],
  "332": [
    "50025313"
  ],
  "specifikation": [
    "50025313"
  ],
  "statistiskt": [
    "50025313"
  ],
  "540": [
    "50025313"
  ],
  "05000": [
    "50025313"
  ],
  "ean": [
    "50025313"
  ],
  "tillverkningsland": [
    "50025313"
  ],
  "article": [
    "50025313"
  ],
  "1693269": [
    "50025313"
  ],
  "kina": [
    "50025313"
  ],
  "6411723": [
    "50025313"
  ],
  "8424908080": [
    "50025313"
  ],
  "art": [
    "50025313"
  ],
  "jpeg": [
    "50025313",
    "50464764",
    "50108133",
    "50107533",
    "50107532"
  ],
  "43131495": [
    "50025313"
  ],
  "1200": [
    "50025313"
  ],
  "housegard": [
    "50025313"
  ],
  "50025313": [
    "50025313"
  ],
  "volym": [
    "50025313"
  ],
  "fordonsha": [
    "50025313"
  ],
  "technical": [
    "50025313"
  ],
  "pall": [
    "50025313"
  ],
  "800": [
    "50025313"
  ],
  "bruttovikt": [
    "50025313"
  ],
  "nobb": [
    "50025313"
  ],
  "60000": [
    "50025313"
  ],
  "ckare": [
    "50025313"
  ],
  "peb6ge": [
    "50025313"
  ],
  "ngd": [
    "50025313",
    "50464764"
  ],
  "240": [
    "50025313"
  ],
  "000": [
    "50025313"
  ],
  "7320896000544": [
    "50025313"
  ],
  "30000": [
    "50025313"
  ],
  "120": [
    "50025313"
  ],
  "llare": [
    "50025313"
  ],
  "snro": [
    "50025313"
  ],
  "160": [
    "50025313"
  ],
  "kod": [
    "50025313"
  ],
  "pulversla": [
    "50025313"
  ],
  "380": [
    "50025313"
  ],
  "_page_0_picture_3": [
    "50025313"
  ],
  "pe6tj": [
    "50025313"
  ],
  "850": [
    "50025313"
  ],
  "600054": [
    "50025313"
  ],
  "pe6geb": [
    "50025313"
  ],
  "information": [
    "50025313"
  ],
  "weight": [
    "50025313"
  ],
  "_page_0_picture_6": [
    "50025313"
  ],
  "_page_0_picture_8": [
    "50025313"
  ],
  "bredd": [
    "50025313"
  ],
  "_page_0_picture_1": [
    "50025313"
  ],
  "till": [
    "50025313",
    "50464764"
  ],
  "440": [
    "50025313"
  ],
  "packaging": [
    "50025313"
  ],
  "nummer": [
    "50025313"
  ],
  "6209317": [
    "50025313"
  ],
  "batteriboxen": [
    "50464764"
  ],
  "inkoppling": [
    "50464764"
  ],
  "kan": [
    "50464764",
    "50108133",
    "50107533",
    "50107532"
  ],
  "underha": [
    "50464764"
  ],
  "batteri": [
    "50464764"
  ],
  "med": [
    "50464764",
    "50108133",
    "50107533",
    "50107532"
  ],
  "gjord": [
    "50464764"
  ],
  "350": [
    "50464764"
  ],
  "tva": [
    "50464764"
  ],
  "box": [
    "50464764"
  ],
  "battery": [
    "50464764"
  ],
  "support": [
    "50464764"
  ],
  "tillverkarens": [
    "50464764"
  ],
  "och": [
    "50464764",
    "50108133",
    "50107533",
    "50107532"
  ],
  "flx": [
    "50464764"
  ],
  "placering": [
    "50464764"
  ],
  "24v": [
    "50464764"
  ],
  "denna": [
    "50464764"
  ],
  "kopplas": [
    "50464764"
  ],
  "data": [
    "50464764"
  ],
  "kapsling": [
    "50464764"
  ],
  "llsfo": [
    "50464764"
  ],
  "inneha": [
    "50464764"
  ],
  "inga": [
    "50464764"
  ],
  "_page_0_picture_0": [
    "50464764",
    "50108133",
    "50107533",
    "50107532"
  ],
  "publiceringsdatum": [
    "50464764"
  ],
  "edenna": [
    "50464764"
  ],
  "agm": [
    "50464764"
  ],
  "batteribyte": [
    "50464764"
  ],
  "verkan": [
    "50464764"
  ],
  "2023": [
    "50464764"
  ],
  "batteribox": [
    "50464764"
  ],
  "tekniska": [
    "50464764"
  ],
  "tervinning": [
    "50464764"
  ],
  "batterier": [
    "50464764"
  ],
  "livsla": [
    "50464764"
  ],
  "rteckning": [
    "50464764"
  ],
  "produktens": [
    "50464764"
  ],
  "batteria": [
    "50464764"
  ],
  "ljande": [
    "50464764"
  ],
  "230": [
    "50464764"
  ],
  "ups": [
    "50464764"
  ],
  "miljo": [
    "50464764"
  ],
  "oberoende": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "class": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "enligt": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rjningsaggregat": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "vid": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ter": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "speciell": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "stro": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ndas": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rjning": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rso": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "enheter": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "parallel": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "_page_1_picture_0": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "dvs": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "psv": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "egenskaper": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "parallell": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "voltage": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ledningar": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ggningen": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "gra": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "mmen": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "spa": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "tilla": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rkstro": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "synkronisering": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "kra": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "system": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ser": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "som": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rjningsenheter": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "kompensera": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "funktion": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "kallar": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "alla": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "har": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "ggning": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "alarmtech": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "nningsfall": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "parallellkopplas": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "nning": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "unika": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "oavsett": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "grad": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "50131": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "kning": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "samma": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "beho": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "uto": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "felsa": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "anla": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "problem": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "nga": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "anva": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "dina": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "enkelt": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "samtliga": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "nya": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "att": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "extra": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "mfo": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "valfritt": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "utvecklad": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "utvecklat": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "antal": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "_page_0_picture_2": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "mer": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rdelar": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "bygga": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "buss": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "rjningsagg": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "jligo": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "utan": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "batteriladdning": [
    "50108133",
    "50107533",
    "50107532"
  ],
  "vip": [
    "50108133",
    "50107533",
    "50107532"
  ]
}
```

---

# ..\..\data\integrated_data\products\50025313\article_info.jsonl
## File: ..\..\data\integrated_data\products\50025313\article_info.jsonl

```jsonl
# ..\..\data\integrated_data\products\50025313\article_info.jsonl
{"type": "EAN-13", "value": "7320896000544", "confidence": 0.9, "source_text": "onshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": "", "product_id": "50025313"}
{"type": "EAN-8", "value": "43131495", "confidence": 0.9, "source_text": "--------------|------------|--| | Statistiskt nummer | 8424908080 | | | E-nummer | 1693269 | | | EL-nr | 6209317 | | | Snro | 6411723 | | | Nobb-nr | 43131495 | | ## **Packaging information** | | EXKRT | PALL | ST | |--------------------|----------|-----------|---------------| | EAN kod | | | 73208960005", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": "", "product_id": "50025313"}
{"type": "ARTICLE_NUMBER", "value": "1693269", "confidence": 0.85, "source_text": "g pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ## **Technic", "source_location": "", "extracted_method": "regex", "is_valid": true, "validation_message": "", "product_id": "50025313"}

```

---

# ..\..\data\integrated_data\products\50025313\compatibility.jsonl
## File: ..\..\data\integrated_data\products\50025313\compatibility.jsonl

```jsonl
# ..\..\data\integrated_data\products\50025313\compatibility.jsonl
{"relation_type": "fits", "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art", "numeric_ids": [], "context": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare", "confidence": 0.8, "source_text": "![](_page_0_Picture_1.jpeg) ## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE ![](_page_0_Picture_3.jpeg) Passar till PE6GEB, PE6TEA PE6TJ • *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269 ![](_page_0_Picture_6.jpeg) ![](_page_0_Picture_8.jpeg) • *Page 1/2** ## Housegard fordonshållare", "source_location": "", "extracted_method": "regex", "product_id": "50025313"}

```

---

# ..\..\data\integrated_data\products\50025313\full_info.md
## File: ..\..\data\integrated_data\products\50025313\full_info.md

```md
# ..\..\data\integrated_data\products\50025313\full_info.md
![](_page_0_Picture_1.jpeg)

## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE

![](_page_0_Picture_3.jpeg)

Passar till PE6GEB, PE6TEA PE6TJ

**ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269

![](_page_0_Picture_6.jpeg)

![](_page_0_Picture_8.jpeg)

**Page 1/2**

## Housegard fordonshållare till 6 kg pulversläckare, PEB6GE

## **Technical specifikation**

| Tillverkningsland  | Kina       |  |
|--------------------|------------|--|
| Statistiskt nummer | 8424908080 |  |
| E-nummer           | 1693269    |  |
| EL-nr              | 6209317    |  |
| Snro               | 6411723    |  |
| Nobb-nr            | 43131495   |  |

## **Packaging information**

|                    | EXKRT    | PALL      | ST            |
|--------------------|----------|-----------|---------------|
| EAN kod            |          |           | 7320896000544 |
| Längd (mm)         | 540.000  | 1200.000  | 440.000       |
| Höjd (mm)          | 380.000  | 850.000   | 160.000       |
| Bredd (mm)         | 240.000  | 800.000   | 120.000       |
| Bruttovikt (kg)    | 26.05000 | 332.60000 | 1.30000       |
| Net Weight (kg)    | 26.05000 |           | 1.30000       |
| Volym              | 0.00000  | 0.00000   | 0.00246       |
| Net Volume         | 0.00000  |           | 0.00000       |
| Number LAV         |          | 3         |               |
| Nr of units on LAV |          | 4         |               |
| Antal ST           | 20       | 240       | 1             |

![](_page_1_Picture_7.jpeg)

**Page 2/2**
```

---

# ..\..\data\integrated_data\products\50025313\summary.jsonl
## File: ..\..\data\integrated_data\products\50025313\summary.jsonl

```jsonl
# ..\..\data\integrated_data\products\50025313\summary.jsonl
{"product_id": "50025313", "generated_at": "20250305_235339", "product_name": "Produkt 50025313", "description": "• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269", "key_specifications": [{"category": "WEIGHT", "name": "kg", "value": "6", "unit": "GE"}, {"category": "WEIGHT", "name": "kg", "value": "26.05000", "unit": ""}, {"category": "DIMENSIONS", "name": "Längd", "value": "540.000", "unit": ""}, {"category": "DIMENSIONS", "name": "Höjd", "value": "380.000", "unit": ""}], "key_compatibility": [{"type": "fits", "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art", "has_product_id": false, "numeric_ids": []}], "identifiers": {"EAN-13": ["7320896000544"], "EAN-8": ["43131495"], "ARTICLE_NUMBER": ["1693269"]}}

```

---

# ..\..\data\integrated_data\products\50025313\technical_specs.jsonl
## File: ..\..\data\integrated_data\products\50025313\technical_specs.jsonl

```jsonl
# ..\..\data\integrated_data\products\50025313\technical_specs.jsonl
{"category": "WEIGHT", "name": "kg", "raw_value": "6", "unit": "GE", "normalized_value": 6.0, "confidence": 0.85, "importance": "normal", "source_text": "Housegard fordonshållare till 6 kg pulversläckare, PEB6GE\n\n\n!", "source_location": "", "extracted_method": "nlp_phrase_matcher", "product_id": "50025313"}
{"category": "DIMENSIONS", "name": "Längd", "raw_value": "540.000", "unit": "", "normalized_value": 540.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher", "product_id": "50025313"}
{"category": "DIMENSIONS", "name": "Höjd", "raw_value": "380.000", "unit": "", "normalized_value": 380.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher", "product_id": "50025313"}
{"category": "DIMENSIONS", "name": "Bredd", "raw_value": "240.000", "unit": "", "normalized_value": 240.0, "confidence": 0.85, "importance": "normal", "source_text": "Snro | 6411723 | |\n| Nobb-nr | 43131495 | |\n\n## **Packaging information**\n\n\n| | EXKRT | PALL | ST |\n|--------------------|----------|-----------|---------------|\n| EAN kod | | | 7320896000544 |\n| Längd (mm) | 540.000 | 1200.000 | 440.000 |\n| Höjd (mm) | 380.000 | 850.000 | 160.000 |\n| Bredd (mm) | 240.000 | 800.000 | 120.000 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher", "product_id": "50025313"}
{"category": "WEIGHT", "name": "kg", "raw_value": "26.05000", "unit": "", "normalized_value": 26.05, "confidence": 0.85, "importance": "normal", "source_text": "Bruttovikt (kg) | 26.05000 | 332.60000 | 1.30000 |\n| Net Weight (kg) | 26.05000 | | 1.30000 |\n| Volym | 0.00000 | 0.00000 | 0.00246 |\n|", "source_location": "", "extracted_method": "nlp_phrase_matcher", "product_id": "50025313"}

```

---

