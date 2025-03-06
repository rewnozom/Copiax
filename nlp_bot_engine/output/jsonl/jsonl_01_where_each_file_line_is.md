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

## File: ..\..\data\integrated_data\bot_responses\50025313\compatibility_response.json
Line = 244, Starts = 246, Ends = 284

## File: ..\..\data\integrated_data\bot_responses\50025313\summary_response.json
Line = 284, Starts = 286, Ends = 351

## File: ..\..\data\integrated_data\bot_responses\50025313\technical_response.json
Line = 351, Starts = 353, Ends = 496

## File: ..\..\data\integrated_data\indices\article_numbers.json
Line = 496, Starts = 498, Ends = 737

## File: ..\..\data\integrated_data\indices\compatibility_map.json
Line = 737, Starts = 739, Ends = 895

## File: ..\..\data\integrated_data\indices\ean_numbers.json
Line = 895, Starts = 897, Ends = 918

## File: ..\..\data\integrated_data\indices\technical_specs_index.json
Line = 918, Starts = 920, Ends = 1895

## File: ..\..\data\integrated_data\indices\text_search_index.json
Line = 1895, Starts = 1897, Ends = 2621

## File: ..\..\data\integrated_data\products\50025313\article_info.jsonl
Line = 2621, Starts = 2623, Ends = 2634

## File: ..\..\data\integrated_data\products\50025313\compatibility.jsonl
Line = 2634, Starts = 2636, Ends = 2645

## File: ..\..\data\integrated_data\products\50025313\full_info.md
Line = 2645, Starts = 2647, Ends = 2701

## File: ..\..\data\integrated_data\products\50025313\summary.jsonl
Line = 2701, Starts = 2703, Ends = 2712

## File: ..\..\data\integrated_data\products\50025313\technical_specs.jsonl
Line = 2712, Starts = 2714, Ends = 2727

