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
    "extraction_timestamp": "20250305_221242",
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
  "extraction_timestamp": "20250305_221242"
}
```

---

# ..\..\data\extracted_data\reports\extraction_quality_20250305_221242.json
## File: ..\..\data\extracted_data\reports\extraction_quality_20250305_221242.json

```json
# ..\..\data\extracted_data\reports\extraction_quality_20250305_221242.json
{
  "timestamp": "20250305_221242",
  "overall_coverage": {
    "products_with_identifiers_pct": 36.36363636363637,
    "products_with_specs_pct": 100.0,
    "products_with_compat_pct": 90.9090909090909
  },
  "extraction_methods": {
    "identifiers": {
      "regex": 51
    },
    "specifications": {
      "nlp_phrase_matcher": 57,
      "nlp_entity": 28
    },
    "compatibility": {
      "regex": 21,
      "nlp_matcher": 6
    }
  },
  "confidence_stats": {
    "identifiers": {
      "high": 2,
      "medium": 49,
      "low": 0
    },
    "specifications": {
      "high": 0,
      "medium": 85,
      "low": 0
    },
    "compatibility": {
      "high": 0,
      "medium": 27,
      "low": 0
    }
  },
  "missing_data": [
    {
      "product_id": "50464764",
      "product_name": "UPS Battery Box 24 V FLX M",
      "missing": [
        "identifiers"
      ]
    },
    {
      "product_id": "50152629",
      "product_name": "10 output module POWER SUPPLIES - MADE IN SWEDEN Om kortet",
      "missing": [
        "identifiers"
      ]
    },
    {
      "product_id": "50155387",
      "product_name": "10 output module POWER SUPPLIES - MADE IN SWEDEN Om kortet",
      "missing": [
        "identifiers"
      ]
    },
    {
      "product_id": "50152628",
      "product_name": "Produkt 50152628",
      "missing": [
        "identifiers",
        "compatibility"
      ]
    },
    {
      "product_id": "50132277",
      "product_name": "USERMANUAL",
      "missing": [
        "identifiers"
      ]
    },
    {
      "product_id": "50461470",
      "product_name": "**USERMANUAL** Powder extinguishers",
      "missing": [
        "identifiers"
      ]
    }
  ],
  "low_quality_products": [
    {
      "product_id": "50152628",
      "product_name": "Produkt 50152628",
      "item_count": 2,
      "avg_confidence": 0.85
    }
  ]
}
```

---

# ..\..\data\extracted_data\reports\extraction_report_20250305_221242.md
## File: ..\..\data\extracted_data\reports\extraction_report_20250305_221242.md

```md
# ..\..\data\extracted_data\reports\extraction_report_20250305_221242.md
# Product Data Extraction Report

**Generated:** 2025-03-05 22:12:48

## Summary

- **Total files processed:** 22 of 22
- **Products extracted:** 22
- **Extraction duration:** 6.0 seconds

## Data Coverage

| Data Type | Products | Total Extracted | Percentage |
|-----------|----------|-----------------|------------|
| Identifiers | 8 | 102 | 36.4% |
| Specifications | 22 | 184 | 100.0% |
| Compatibility | 20 | 56 | 90.9% |

## Sample Products

### Produkt 50025313 (50025313)

• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269

**Identifiers:**

- EAN-13: 7320896000544
- EAN-8: 43131495
- ARTICLE_NUMBER: 1693269

**Technical Specifications:**

- kg: 6 GE
- Längd: 540.000
- Höjd: 380.000
- Bredd: 240.000
- kg: 26.05000

**Compatibility:**

- Fits: PE6GEB, PE6TEA PE6TJ

• *ARTICLE INFORMATION:** Art

### UPS Battery Box 24 V FLX M (50464764)

| 1. Om UPS batteribox 3 | |
|-------------------------------------------------------------|--|
| 1.1. Tillverkarens support 3 | |
| 1.2. Produktens livslängd, miljöpåverkan och återvinning 3 | |
| 2. Denna batteribox passar till följande UPS:er 4 | |
| 3. Batterier - placering och inkoppling 4 | |
| 3.1. Placering av batterier 4 | |
| 3.2. Inkoppling batteribox med UPS 5 | |
| 4. Tekniska data UPS 6 | |
| 5. Tekniska data kapsling 6 | |
| 5.1. Kapsling - Tekniska Data -UPS Battery box 24V FL...

**Technical Specifications:**

- Height: 224 mm mm
- Height: 438 mm mm
- Height: 212 mm mm
- Dimension: 197x165x170 mm mm
- Mått: 224 mm
- ...and 5 more

**Compatibility:**

- Compatibility: UPS:ER


| UPS | Artikelnummer |
- Compatibility: rensa tidigare batterikapacitet
- Fits: följande UPS:er 4 | |
| 3
- Fits: följande UPS:er \[4\]](#page-3-0) UPS:er denna batteribox passar till
- Fits: FÖLJANDE UPS:ER


| UPS | Artikelnummer |
|---------------------------------|----------------|
| SIN 600W FLX L | FL01U0021FP006 |
| SIN 1100W FLX L | FL01U0031FP011 |
| SIN 1500W FLX L | FL01U0031FP015 |
| TEL-1200W-STS-SIN2* | 5144 |
| *Säljs ej direkt av Milleteknik | |

# 3
- ...and 1 more

### V/P löser dina problem med spänningsfall (50107532)

Alarmtech har utvecklat nya strömförsörjningsenheter med unika egenskaper som löser många problem i en anläggning. **Några fördelar med VIP strömförsörjning:**

**Identifiers:**

- ARTICLE_NUMBER: 5240068
- ARTICLE_NUMBER: 5240067
- ARTICLE_NUMBER: 5240001
- ARTICLE_NUMBER: 5240002
- ARTICLE_NUMBER: 5213168
- ...and 11 more

**Technical Specifications:**

- Dimension: 325x276x90 mm mm
- Dimension: 345x325x130 mm mm
- Dimension: 400x425x200 mm mm
- Dimension: 300x230x100mm mm
- Dimension: 35 mm mm
- ...and 10 more

**Compatibility:**

- Fits: följande PSV-modeller |
|---------|-------------|---------|-----------------------------------|
| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |
| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |
| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |
| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |

## Spänningsfall i ledningsnätet?


![](_page_3_Picture_1
- Requires: inte ändras
## Behövs mer ström?


![](_page_3_Picture_6

### V/P löser dina problem med spänningsfall (50107533)

Alarmtech har utvecklat nya strömförsörjningsenheter med unika egenskaper som löser många problem i en anläggning. **Några fördelar med VIP strömförsörjning:**

**Identifiers:**

- ARTICLE_NUMBER: 5240068
- ARTICLE_NUMBER: 5240067
- ARTICLE_NUMBER: 5240001
- ARTICLE_NUMBER: 5240002
- ARTICLE_NUMBER: 5213168
- ...and 11 more

**Technical Specifications:**

- Dimension: 325x276x90 mm mm
- Dimension: 345x325x130 mm mm
- Dimension: 400x425x200 mm mm
- Dimension: 300x230x100mm mm
- Dimension: 35 mm mm
- ...and 10 more

**Compatibility:**

- Fits: följande PSV-modeller |
|---------|-------------|---------|-----------------------------------|
| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |
| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |
| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |
| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |

## Spänningsfall i ledningsnätet?


![](_page_3_Picture_1
- Requires: inte ändras
## Behövs mer ström?


![](_page_3_Picture_6

### 10 output module POWER SUPPLIES - MADE IN SWEDEN Om kortet (50152629)

10 output module (i tabellen nedan 10 OUT) är en avsäkringsmodul med sju prioriterade (=alltid spänning) utgångar och tre oprioriterade utgångar. Kontrollera vid beställning att kortet passar till den batteribackup kortet skall installeras i.

**Technical Specifications:**

- Dimension: 55 mm mm
- Mått: 120 x

**Compatibility:**

- Compatibility: innan montering sker
- Fits: den batteribackup kortet skall installeras i
- Fits: enheten innan montering sker


## Errors and Issues

- **Errors:** 0
- **Warnings:** 0


## Next Steps

1. **Review extracted data** for quality and completeness
2. **Analyze compatibility relations** to find patterns
3. **Enhance the extraction model** based on quality reports
4. **Integrate the data** with other systems

*Report generated by Unified Product Data Extractor 20250305_221242*

```

---

# ..\..\data\extracted_data\reports\extraction_stats_20250305_221242.json
## File: ..\..\data\extracted_data\reports\extraction_stats_20250305_221242.json

```json
# ..\..\data\extracted_data\reports\extraction_stats_20250305_221242.json
{
  "total_files": 22,
  "processed_files": 22,
  "extracted_products": 22,
  "products_with_identifiers": 8,
  "products_with_specifications": 22,
  "products_with_compatibility": 20,
  "total_identifiers": 102,
  "total_specifications": 184,
  "total_compatibility": 56,
  "errors": 0,
  "warnings": 0,
  "start_time": "2025-03-05T22:12:42.006051",
  "end_time": "2025-03-05T22:12:48.015498",
  "duration_seconds": 6.009447
}
```

---

# ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
## File: ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json

```json
# ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
{
    "product_id": "50025313",
    "command": "-c",
    "timestamp": "2025-03-05T22:12:48.039840",
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
    "timestamp": "2025-03-05T22:12:48.039840",
    "product_name": "Produkt 50025313",
    "summary_data": {
        "product_id": "50025313",
        "generated_at": "20250305_221242",
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
    "timestamp": "2025-03-05T22:12:48.039840",
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
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240067": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240001": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240002": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213168": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213169": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240041": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240042": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213170": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5213171": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5255012": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5255013": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240000": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240064": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240065": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
      "id_type": "ARTICLE_NUMBER"
    }
  ],
  "5240069": [
    {
      "product_id": "50107532",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50107533",
      "id_type": "ARTICLE_NUMBER"
    },
    {
      "product_id": "50108133",
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
  ],
  "följande PSV-modeller |\n|---------|-------------|---------|-----------------------------------|\n| FG20721 | 12V/7,2 Ah | 5230060 | PSV 2415-7 |\n| FG21202 | 12V/12 Ah | 5230061 | Alla PSV 24XX-12 |\n| FG21805 | 12V18 Ah | 5230062 | Alla PSV 12XX-18 |\n| FG24207 | 12V/42 Ah | 5230063 | Alla PSV 24XX-40 |\n\n## Spänningsfall i ledningsnätet?\n\n\n![](_page_3_Picture_1": [
    {
      "related_product": "50107532",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50107533",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50108133",
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
  "50152629": [
    {
      "related_product": "innan montering sker",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "den batteribackup kortet skall installeras i",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "enheten innan montering sker",
      "relation_type": "fits",
      "numeric_ids": []
    }
  ],
  "den batteribackup kortet skall installeras i": [
    {
      "related_product": "50152629",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50155387",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "enheten innan montering sker": [
    {
      "related_product": "50152629",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50155387",
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
  "50155387": [
    {
      "related_product": "innan montering sker",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "den batteribackup kortet skall installeras i",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "enheten innan montering sker",
      "relation_type": "fits",
      "numeric_ids": []
    }
  ],
  "50132277": [
    {
      "related_product": "",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "ditt bruksområde enligt informationen på brandsläckarens etikett",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "specialutrustning",
      "relation_type": "requires",
      "numeric_ids": []
    }
  ],
  "ditt bruksområde enligt informationen på brandsläckarens etikett": [
    {
      "related_product": "50132277",
      "relation_type": "compatible_with",
      "numeric_ids": []
    },
    {
      "related_product": "50461470",
      "relation_type": "compatible_with",
      "numeric_ids": []
    }
  ],
  "50461470": [
    {
      "related_product": "",
      "relation_type": "compatibility",
      "numeric_ids": []
    },
    {
      "related_product": "ditt bruksområde enligt informationen på brandsläckarens etikett",
      "relation_type": "fits",
      "numeric_ids": []
    },
    {
      "related_product": "specialutrustning",
      "relation_type": "requires",
      "numeric_ids": []
    },
    {
      "related_product": "special equipment and training, Contact an authorized service centre",
      "relation_type": "requires",
      "numeric_ids": []
    },
    {
      "related_product": "that the original seal is intact and that the product has not been opened, used, refilled or gone through service that has resulted in physical intervention of the product",
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
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "2",
        "unit": "",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Slokkeren skal inneholde en spesifisert mengde med CO2 angitt i kg.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "5",
        "unit": "TGX",
        "normalized_value": 5.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "For modell K2 = 2 kg, for modell K5TGX = 5 kg.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "220",
        "unit": "Bar",
        "normalized_value": 220.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Vekt: 6,4 kg",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "vikt",
        "raw_value": "2",
        "unit": "som",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Apparatens vikt frånräknat apparatens tomvikt motsvarar mängden CO2 som är i apparaten.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "6,4",
        "unit": "kg",
        "normalized_value": 6.4,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "34B Vikt: 6,4 kg",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "15",
        "unit": "kg",
        "normalized_value": 15.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Vikt: 15 kg",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "KG",
        "raw_value": "2",
        "unit": "HR",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*TEKNISKE SPESIFIKASJONER:**\n\n\n#### **2 KG PE2HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE2HR-A **Type:** 2 kg ABC pulver, trykkladet **Brannklasse:** ABC **Effektklasse:** 13A 89B C **Vekt:** 3,6 kg **Arbeidstrykk:** 15 Bar **Drivgass:** Nitrogen N₂ **Slokkemiddel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "15",
        "unit": "Bar",
        "normalized_value": 15.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*TEKNISKE SPESIFIKASJONER:**\n\n\n#### **2 KG PE2HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE2HR-A **Type:** 2 kg ABC pulver, trykkladet **Brannklasse:** ABC **Effektklasse:** 13A 89B C **Vekt:** 3,6 kg **Arbeidstrykk:** 15 Bar **Drivgass:** Nitrogen N₂ **Slokkemiddel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "KG",
        "raw_value": "6",
        "unit": "HR",
        "normalized_value": 6.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Standard **Godkjenninger:** CE **Temperaturområde:** -30 °C til +60 °C\n\n#### **6 KG PE6HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE6HR-A **Type:** 6 kg ABC pulver, trykkladet **Brannklasse:** ABC **Effektklasse:** 55A 233B C **Vekt:** 9,2 kg **Arbeidstrykk:** 15 Bar **Drivgass:** Nitrogen N₂ **Slokkemiddel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "3,6",
        "unit": "kg",
        "normalized_value": 3.6,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "PE2HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE2HR-A **Typ:** 2 kg ABC pulver, tryckladdad. **Brandklass:** ABC **Effektklass:** 13A 89B C **Vikt:** 3,6 kg **Arbetstryck:** 15",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "9,2",
        "unit": "kg",
        "normalized_value": 9.2,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "**Brandklass:** ABC **Effektklass:** 55A 233B C **Vikt:** 9,2 kg **Arbetstryck:** 15 Bar **Drivgas:** Nitrogen gas N₂ **Släckmedel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "3,5",
        "unit": "kg",
        "normalized_value": 3.5,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "*Modell:** Housegard PE2HR-B **Typ:** 2 kg ABC pulver, tryckladdad. **Brandklass:** ABC **Effektklass:** 13A 89B C **Vikt:** 3,5 kg **Arbetstryck:** 15 Bar **Drivgas:** Nitrogen gas N₂ **Släckmedel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "Vikt",
        "raw_value": "8,6",
        "unit": "kg",
        "normalized_value": 8.6,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "**Brandklass:** ABC **Effektklass:** 55A 233B C **Vikt:** 8,6 kg **Arbetstryck:** 15 Bar **Drivgas:** Nitrogen gas N₂ **Släckmedel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "13",
        "unit": "A",
        "normalized_value": 13.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "PE2HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE2HR-A **Typ:** 2 kg ABC-Pulver, Druckladung **Brandschutzklasse:** ABC **Löschvermögen-Klasse:** 13A 89B C **Gewicht:** 3,6 kg **Druck:** 15 Bar **Treibgas:** Nitrogen N₂ **Löschmittel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "WEIGHT",
        "name": "kg",
        "raw_value": "55",
        "unit": "A",
        "normalized_value": 55.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Standard **Zulassungen:** CE **Temperaturbereich:** -30 °C bis +60 °C\n\n#### **6 KG PE6HR-A BLACK, WHITE**\n\n\n• *Modell:** Housegard PE6HR-A **Typ:** 6 kg ABC-Pulver, Druckladung **Brandschutzklasse:** ABC **Löschvermögen-Klasse:** 55A 233B C **Gewicht:** 9,2 kg **Druck:** 15 Bar **Treibgas:** Nitrogen N₂ **Löschmittel:** SUN ABC",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50461470"
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
      "product_id": "50152629",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "55 mm",
        "unit": "mm",
        "normalized_value": 55.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 120 x 55 mm | | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50152629"
      }
    },
    {
      "product_id": "50152629",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Mått",
        "raw_value": "120",
        "unit": "x",
        "normalized_value": 120.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 120 x 55 mm | | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50152629"
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
      "product_id": "50155387",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "55 mm",
        "unit": "mm",
        "normalized_value": 55.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 120 x 55 mm | | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50155387"
      }
    },
    {
      "product_id": "50155387",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Mått",
        "raw_value": "120",
        "unit": "x",
        "normalized_value": 120.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 120 x 55 mm | | | |\n|",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50155387"
      }
    },
    {
      "product_id": "50152628",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "37 mm",
        "unit": "mm",
        "normalized_value": 37.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 85 x 37 mm.",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50152628"
      }
    },
    {
      "product_id": "50152628",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Mått",
        "raw_value": "85",
        "unit": "x",
        "normalized_value": 85.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Mått | 85 x 37 mm.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50152628"
      }
    },
    {
      "product_id": "50132277",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "1 meter",
        "unit": "meter",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Ved slokking av branner i elektriske anlegg, sørg for en sikkerhetsavstand på minimum 1 meter.\n\n#### FORPAKNINGEN INNEHOLDER:\n\n\n• » 1 stk brannslokker\n\n• » 1 stk veggfeste\n\n• » 1 stk slange (modell K5TGX)\n\n• » 1 stk pakning til slange.",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50132277"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "1 meter",
        "unit": "meter",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Gå ikke for nære, men hold en sikkerhetsavstand på minimum 1 meter.",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50461470"
      }
    },
    {
      "product_id": "50461470",
      "spec": {
        "category": "DIMENSIONS",
        "name": "Dimension",
        "raw_value": "1 Meter",
        "unit": "Meter",
        "normalized_value": 1.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Sicherheitsabstand von mindestens 1 Meter.",
        "source_location": "",
        "extracted_method": "nlp_entity",
        "product_id": "50461470"
      }
    }
  ],
  "ELECTRICAL": [
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
    }
  ],
  "MATERIAL": [
    {
      "product_id": "50132277",
      "spec": {
        "category": "MATERIAL",
        "name": "material",
        "raw_value": "2",
        "unit": "ger",
        "normalized_value": 2.0,
        "confidence": 0.85,
        "importance": "normal",
        "source_text": "Din nya Housegard brandsläckare innehåller koldioxid som är avsedd för släckning av bränder i olika material såsom brandfarliga vätskor och kemikalier.",
        "source_location": "",
        "extracted_method": "nlp_phrase_matcher",
        "product_id": "50132277"
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
  "snro": [
    "50025313"
  ],
  "page": [
    "50025313",
    "50464764"
  ],
  "1200": [
    "50025313"
  ],
  "fordonsha": [
    "50025313"
  ],
  "passar": [
    "50025313",
    "50464764",
    "50152629",
    "50155387",
    "50152628"
  ],
  "bredd": [
    "50025313"
  ],
  "05000": [
    "50025313"
  ],
  "weight": [
    "50025313"
  ],
  "850": [
    "50025313"
  ],
  "ngd": [
    "50025313",
    "50464764"
  ],
  "produkt": [
    "50025313",
    "50152628"
  ],
  "440": [
    "50025313"
  ],
  "jpeg": [
    "50025313",
    "50464764",
    "50107532",
    "50107533",
    "50108133",
    "50152628",
    "50132277",
    "50461470"
  ],
  "kina": [
    "50025313"
  ],
  "pe6tea": [
    "50025313"
  ],
  "pe6tj": [
    "50025313"
  ],
  "7320896000544": [
    "50025313"
  ],
  "exkrt": [
    "50025313"
  ],
  "pe6geb": [
    "50025313"
  ],
  "1693269": [
    "50025313"
  ],
  "30000": [
    "50025313"
  ],
  "pulversla": [
    "50025313"
  ],
  "tillverkningsland": [
    "50025313"
  ],
  "net": [
    "50025313"
  ],
  "housegard": [
    "50025313",
    "50132277",
    "50461470"
  ],
  "_page_0_picture_1": [
    "50025313",
    "50152628",
    "50461470"
  ],
  "540": [
    "50025313"
  ],
  "160": [
    "50025313"
  ],
  "600054": [
    "50025313"
  ],
  "ean": [
    "50025313"
  ],
  "technical": [
    "50025313"
  ],
  "volym": [
    "50025313"
  ],
  "8424908080": [
    "50025313"
  ],
  "_page_0_picture_6": [
    "50025313"
  ],
  "statistiskt": [
    "50025313"
  ],
  "50025313": [
    "50025313"
  ],
  "ckare": [
    "50025313"
  ],
  "6209317": [
    "50025313"
  ],
  "kod": [
    "50025313"
  ],
  "800": [
    "50025313"
  ],
  "120": [
    "50025313"
  ],
  "peb6ge": [
    "50025313"
  ],
  "240": [
    "50025313"
  ],
  "43131495": [
    "50025313"
  ],
  "_page_0_picture_3": [
    "50025313",
    "50132277",
    "50461470"
  ],
  "nobb": [
    "50025313"
  ],
  "nummer": [
    "50025313"
  ],
  "pall": [
    "50025313"
  ],
  "000": [
    "50025313"
  ],
  "llare": [
    "50025313"
  ],
  "specifikation": [
    "50025313"
  ],
  "art": [
    "50025313"
  ],
  "article": [
    "50025313"
  ],
  "60000": [
    "50025313"
  ],
  "bruttovikt": [
    "50025313"
  ],
  "information": [
    "50025313",
    "50132277",
    "50461470"
  ],
  "_page_0_picture_8": [
    "50025313"
  ],
  "packaging": [
    "50025313"
  ],
  "380": [
    "50025313"
  ],
  "332": [
    "50025313"
  ],
  "till": [
    "50025313",
    "50464764",
    "50152629",
    "50155387",
    "50152628"
  ],
  "6411723": [
    "50025313"
  ],
  "_page_0_picture_0": [
    "50464764",
    "50107532",
    "50107533",
    "50108133",
    "50132277"
  ],
  "miljo": [
    "50464764"
  ],
  "battery": [
    "50464764"
  ],
  "inkoppling": [
    "50464764",
    "50152629",
    "50155387",
    "50152628"
  ],
  "box": [
    "50464764"
  ],
  "tva": [
    "50464764"
  ],
  "2023": [
    "50464764"
  ],
  "llsfo": [
    "50464764"
  ],
  "tekniska": [
    "50464764"
  ],
  "verkan": [
    "50464764"
  ],
  "kopplas": [
    "50464764"
  ],
  "batteribox": [
    "50464764"
  ],
  "underha": [
    "50464764"
  ],
  "edenna": [
    "50464764"
  ],
  "tervinning": [
    "50464764"
  ],
  "24v": [
    "50464764",
    "50152629",
    "50155387",
    "50152628"
  ],
  "230": [
    "50464764"
  ],
  "produktens": [
    "50464764"
  ],
  "kan": [
    "50464764",
    "50107532",
    "50107533",
    "50108133",
    "50132277",
    "50461470"
  ],
  "agm": [
    "50464764"
  ],
  "ljande": [
    "50464764"
  ],
  "flx": [
    "50464764",
    "50152629",
    "50155387"
  ],
  "batteri": [
    "50464764"
  ],
  "350": [
    "50464764"
  ],
  "och": [
    "50464764",
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387",
    "50152628"
  ],
  "data": [
    "50464764"
  ],
  "med": [
    "50464764",
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387",
    "50152628"
  ],
  "placering": [
    "50464764"
  ],
  "rteckning": [
    "50464764"
  ],
  "batteria": [
    "50464764"
  ],
  "denna": [
    "50464764",
    "50152628"
  ],
  "publiceringsdatum": [
    "50464764"
  ],
  "livsla": [
    "50464764"
  ],
  "batteriboxen": [
    "50464764"
  ],
  "ups": [
    "50464764"
  ],
  "tillverkarens": [
    "50464764"
  ],
  "batterier": [
    "50464764"
  ],
  "batteribyte": [
    "50464764"
  ],
  "gjord": [
    "50464764"
  ],
  "kapsling": [
    "50464764"
  ],
  "support": [
    "50464764"
  ],
  "inga": [
    "50464764",
    "50152629",
    "50155387",
    "50152628"
  ],
  "inneha": [
    "50464764"
  ],
  "enligt": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "dvs": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "vip": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "utvecklat": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "har": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "antal": [
    "50107532",
    "50107533",
    "50108133",
    "50152628"
  ],
  "psv": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "nningsfall": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "unika": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "att": [
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387"
  ],
  "50131": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "batteriladdning": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "dina": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "stro": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "som": [
    "50107532",
    "50107533",
    "50108133",
    "50132277",
    "50461470"
  ],
  "rkstro": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "buss": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "rjningsagg": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ggningen": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "kra": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "uto": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "valfritt": [
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387",
    "50152628"
  ],
  "enkelt": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "oberoende": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "anva": [
    "50107532",
    "50107533",
    "50108133",
    "50152628"
  ],
  "kning": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "rso": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "utan": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "synkronisering": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "voltage": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "rdelar": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ter": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "_page_1_picture_0": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "nning": [
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387"
  ],
  "alarmtech": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "parallel": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ndas": [
    "50107532",
    "50107533",
    "50108133",
    "50152628"
  ],
  "rjningsaggregat": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "funktion": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "parallellkopplas": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "parallell": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "kompensera": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "nya": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "enheter": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "system": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "oavsett": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ledningar": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "mmen": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "spa": [
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387",
    "50152628"
  ],
  "nga": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "grad": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "samma": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "egenskaper": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "gra": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ggning": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "samtliga": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "kallar": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "_page_0_picture_2": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "problem": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "utvecklad": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "alla": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "class": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "tilla": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "rjningsenheter": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "mfo": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "rjning": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "anla": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "beho": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "extra": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "ser": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "mer": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "speciell": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "vid": [
    "50107532",
    "50107533",
    "50152629",
    "50108133",
    "50155387"
  ],
  "jligo": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "felsa": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "bygga": [
    "50107532",
    "50107533",
    "50108133"
  ],
  "batteribackup": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "koppla": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "prioriterade": [
    "50152629",
    "50155387"
  ],
  "batteriback": [
    "50152629",
    "50155387"
  ],
  "alltid": [
    "50152629",
    "50155387"
  ],
  "oprioriterade": [
    "50152629",
    "50155387"
  ],
  "pro1": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "utga": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "llning": [
    "50152629",
    "50155387"
  ],
  "nedan": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "kortets": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "varianto": [
    "50152629",
    "50155387"
  ],
  "10a": [
    "50152629",
    "50155387"
  ],
  "pla": [
    "50152629",
    "50155387"
  ],
  "supplies": [
    "50152629",
    "50155387"
  ],
  "kretskort": [
    "50152629",
    "50155387"
  ],
  "tabellen": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "besta": [
    "50152629",
    "50155387"
  ],
  "skall": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "monteras": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "ngar": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "kontrollera": [
    "50152629",
    "50155387"
  ],
  "ttning": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "installeras": [
    "50152629",
    "50155387"
  ],
  "versikt": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "pro2": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "den": [
    "50152629",
    "50155387",
    "50152628",
    "50132277",
    "50461470"
  ],
  "fra": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "pro3": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "made": [
    "50152629",
    "50155387"
  ],
  "avsa": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "lastutga": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "power": [
    "50152629",
    "50155387"
  ],
  "module": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "sju": [
    "50152629",
    "50155387"
  ],
  "nningslo": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "batteribackupens": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "vilka": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "out": [
    "50152629",
    "50155387"
  ],
  "larm": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "ngsa": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "kringsmodul": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "iga": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "vara": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "styrning": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "tre": [
    "50152629",
    "50155387",
    "50461470"
  ],
  "output": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "driftsa": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "last": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "fast": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "batteribackuper": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "kortet": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "matning": [
    "50152629",
    "50155387",
    "50152628"
  ],
  "sweden": [
    "50152629",
    "50155387"
  ],
  "beskriver": [
    "50152628"
  ],
  "eller": [
    "50152628"
  ],
  "helt": [
    "50152628"
  ],
  "fungerar": [
    "50152628"
  ],
  "adapter": [
    "50152628"
  ],
  "manual": [
    "50152628",
    "50132277",
    "50461470"
  ],
  "korten": [
    "50152628"
  ],
  "tts": [
    "50152628"
  ],
  "vinkel": [
    "50152628"
  ],
  "innan": [
    "50152628"
  ],
  "50152628": [
    "50152628"
  ],
  "ju1": [
    "50152628"
  ],
  "byglad": [
    "50152628"
  ],
  "pro": [
    "50152628"
  ],
  "fem": [
    "50152628"
  ],
  "inte": [
    "50152628"
  ],
  "upp": [
    "50152628"
  ],
  "neo3": [
    "50152628"
  ],
  "kort": [
    "50152628"
  ],
  "krade": [
    "50152628"
  ],
  "din": [
    "50132277",
    "50461470"
  ],
  "spar": [
    "50132277",
    "50461470"
  ],
  "ren": [
    "50132277"
  ],
  "elektriske": [
    "50132277",
    "50461470"
  ],
  "ogsa": [
    "50132277",
    "50461470"
  ],
  "sørg": [
    "50132277"
  ],
  "sikkerhetsavstand": [
    "50132277"
  ],
  "veggfeste": [
    "50132277",
    "50461470"
  ],
  "denne": [
    "50132277",
    "50461470"
  ],
  "co2": [
    "50132277"
  ],
  "restprodukter": [
    "50132277"
  ],
  "brannslokkeren": [
    "50132277",
    "50461470"
  ],
  "slokker": [
    "50132277"
  ],
  "benyttes": [
    "50132277",
    "50461470"
  ],
  "_page_2_figure_1": [
    "50132277"
  ],
  "hele": [
    "50132277",
    "50461470"
  ],
  "ohje": [
    "50132277",
    "50461470"
  ],
  "com": [
    "50132277",
    "50461470"
  ],
  "til": [
    "50132277",
    "50461470"
  ],
  "rekke": [
    "50132277",
    "50461470"
  ],
  "anlegg": [
    "50132277",
    "50461470"
  ],
  "k5tgx": [
    "50132277"
  ],
  "framtidig": [
    "50132277",
    "50461470"
  ],
  "1000": [
    "50132277",
    "50461470"
  ],
  "viktig": [
    "50132277",
    "50461470"
  ],
  "uten": [
    "50132277"
  ],
  "kjemikalier": [
    "50132277",
    "50461470"
  ],
  "brugsvejledning": [
    "50132277",
    "50461470"
  ],
  "utilisation": [
    "50132277",
    "50461470"
  ],
  "ver": [
    "50132277",
    "50461470"
  ],
  "meter": [
    "50132277"
  ],
  "volt": [
    "50132277",
    "50461470"
  ],
  "161207": [
    "50132277"
  ],
  "forpakningen": [
    "50132277",
    "50461470"
  ],
  "ytto": [
    "50132277",
    "50461470"
  ],
  "for": [
    "50132277",
    "50461470"
  ],
  "_page_1_picture_2": [
    "50132277"
  ],
  "visit": [
    "50132277",
    "50461470"
  ],
  "før": [
    "50132277",
    "50461470"
  ],
  "produktet": [
    "50132277",
    "50461470"
  ],
  "ildsfarlige": [
    "50132277",
    "50461470"
  ],
  "manuel": [
    "50132277",
    "50461470"
  ],
  "gir": [
    "50132277"
  ],
  "installerer": [
    "50132277",
    "50461470"
  ],
  "bruk": [
    "50132277",
    "50461470"
  ],
  "inntil": [
    "50132277",
    "50461470"
  ],
  "brannslokker": [
    "50132277",
    "50461470"
  ],
  "usermanual": [
    "50132277",
    "50461470"
  ],
  "bruksanvisning": [
    "50132277",
    "50461470"
  ],
  "user": [
    "50132277",
    "50461470"
  ],
  "more": [
    "50132277",
    "50461470"
  ],
  "nøye": [
    "50132277",
    "50461470"
  ],
  "slokking": [
    "50132277",
    "50461470"
  ],
  "stk": [
    "50132277"
  ],
  "nye": [
    "50132277",
    "50461470"
  ],
  "minimum": [
    "50132277"
  ],
  "les": [
    "50132277",
    "50461470"
  ],
  "egnet": [
    "50132277",
    "50461470"
  ],
  "inneholder": [
    "50132277",
    "50461470"
  ],
  "forurensende": [
    "50132277"
  ],
  "extinguishers": [
    "50132277",
    "50461470"
  ],
  "www": [
    "50132277",
    "50461470"
  ],
  "materialer": [
    "50132277",
    "50461470"
  ],
  "branner": [
    "50132277",
    "50461470"
  ],
  "væsker": [
    "50132277",
    "50461470"
  ],
  "ved": [
    "50132277",
    "50461470"
  ],
  "fiberstoffer": [
    "50461470"
  ],
  "papir": [
    "50461470"
  ],
  "dansk": [
    "50461470"
  ],
  "egenkontroll": [
    "50461470"
  ],
  "slange": [
    "50461470"
  ],
  "pulver": [
    "50461470"
  ],
  "felt": [
    "50461470"
  ],
  "manometer": [
    "50461470"
  ],
  "gjelder": [
    "50461470"
  ],
  "grønt": [
    "50461470"
  ],
  "ikke": [
    "50461470"
  ],
  "gebrauchsanweisung": [
    "50461470"
  ],
  "montert": [
    "50461470"
  ],
  "plombe": [
    "50461470"
  ],
  "utpakking": [
    "50461470"
  ],
  "abc": [
    "50461470"
  ],
  "210705": [
    "50461470"
  ],
  "sta": [
    "50461470"
  ],
  "powder": [
    "50461470"
  ],
  "sikringsplinten": [
    "50461470"
  ],
  "_page_0_picture_4": [
    "50461470"
  ],
  "pilen": [
    "50461470"
  ],
  "kontroller": [
    "50461470"
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
{"product_id": "50025313", "generated_at": "20250305_221242", "product_name": "Produkt 50025313", "description": "• *ARTICLE INFORMATION:** Art.no: 600054 EAN: 7320896000544 E-nummer: 1693269", "key_specifications": [{"category": "WEIGHT", "name": "kg", "value": "6", "unit": "GE"}, {"category": "WEIGHT", "name": "kg", "value": "26.05000", "unit": ""}, {"category": "DIMENSIONS", "name": "Längd", "value": "540.000", "unit": ""}, {"category": "DIMENSIONS", "name": "Höjd", "value": "380.000", "unit": ""}], "key_compatibility": [{"type": "fits", "related_product": "PE6GEB, PE6TEA PE6TJ\n\n• *ARTICLE INFORMATION:** Art", "has_product_id": false, "numeric_ids": []}], "identifiers": {"EAN-13": ["7320896000544"], "EAN-8": ["43131495"], "ARTICLE_NUMBER": ["1693269"]}}

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

