## Where each File line for each ## File: ..\filename: 

## To extract code blocks from this markdown file, use the following Python script:

```python
def extract_code_blocks(file_path, instructions):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for instruction in instructions:
        file_name = instruction['file']
        start_line = instruction['start_line'] - 1
        end_line = instruction['end_line']
        code = ''.join(lines[start_line:end_line])
        print(f"## Extracted Code from {file_name}")
        print(code)
        print("#" * 80)

# Example instructions
instructions = [
    {'file': '../example.py', 'start_line': 1, 'end_line': 10},
]

file_path = '{generated_file_name}'
extract_code_blocks(file_path, instructions)
```

## File: ..\..\data\extracted_data\products\50025313\50025313_compatibility.jsonl
Line = 27, Starts = 29, Ends = 38

## File: ..\..\data\extracted_data\products\50025313\50025313_data.json
Line = 38, Starts = 40, Ends = 182

## File: ..\..\data\extracted_data\products\50025313\50025313_identifiers.jsonl
Line = 182, Starts = 184, Ends = 195

## File: ..\..\data\extracted_data\products\50025313\50025313_specifications.jsonl
Line = 195, Starts = 197, Ends = 210

## File: ..\..\data\extracted_data\products\50025313\50025313_summary.json
Line = 210, Starts = 212, Ends = 229

## File: ..\..\data\extracted_data\reports\extraction_quality_20250305_221242.json
Line = 229, Starts = 231, Ends = 329

## File: ..\..\data\extracted_data\reports\extraction_report_20250305_221242.md
Line = 329, Starts = 331, Ends = 542

## File: ..\..\data\extracted_data\reports\extraction_stats_20250305_221242.json
Line = 542, Starts = 544, Ends = 567

## File: ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
Line = 567, Starts = 569, Ends = 607

## File: ..\..\data\integrated_data\bot_responses\50025313\summary_response.json
Line = 607, Starts = 609, Ends = 674

## File: ..\..\data\integrated_data\bot_responses\50025313\technical_response.json
Line = 674, Starts = 676, Ends = 819

## File: ..\..\data\integrated_data\indices\article_numbers.json
Line = 819, Starts = 821, Ends = 1060

## File: ..\..\data\integrated_data\indices\compatibility_map.json
Line = 1060, Starts = 1062, Ends = 1332

## File: ..\..\data\integrated_data\indices\ean_numbers.json
Line = 1332, Starts = 1334, Ends = 1355

## File: ..\..\data\integrated_data\indices\technical_specs_index.json
Line = 1355, Starts = 1357, Ends = 2734

## File: ..\..\data\integrated_data\indices\text_search_index.json
Line = 2734, Starts = 2736, Ends = 4149

## File: ..\..\data\integrated_data\products\50025313\article_info.jsonl
Line = 4149, Starts = 4151, Ends = 4162

## File: ..\..\data\integrated_data\products\50025313\compatibility.jsonl
Line = 4162, Starts = 4164, Ends = 4173

## File: ..\..\data\integrated_data\products\50025313\full_info.md
Line = 4173, Starts = 4175, Ends = 4229

## File: ..\..\data\integrated_data\products\50025313\summary.jsonl
Line = 4229, Starts = 4231, Ends = 4240

## File: ..\..\data\integrated_data\products\50025313\technical_specs.jsonl
Line = 4240, Starts = 4242, Ends = 4255

