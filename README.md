# AutoPi OpenAPI Explorer

A Python-based OpenAPI parser and endpoint explorer built from the public AutoPi OpenAPI specification.

## Disclaimer

This project uses the public AutoPi OpenAPI specification endpoint for educational and portfolio purposes only.
No private telemetry or unauthorized API access is used.

## Features

- Download OpenAPI JSON specification
- Parse API endpoint paths
- Extract supported HTTP methods
- Export endpoints to Markdown
- Export endpoints to CSV

## Tech Stack

- Python
- Requests
- JSON parsing
- CSV export
- Markdown generation

## Example Output

```bash
Total endpoint summaries: 387
```

## Generated Files

- outputs/endpoints.md
- outputs/endpoints.csv


## Tree

```text
autopi-openapi-explorer/
│
├── src/
│   ├── api_client.py
│   ├── parser.py
│   ├── exporters.py
│   └── cli.py
│
├── outputs/
│   ├── endpoints.md
│   └── endpoints.csv
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Purpose

This project was built as a backend/API portfolio project focused on:

- API understanding
- OpenAPI processing
- backend workflows
- data extraction
- automation pipelines


## How to run

```bash
pip install -r requirements.txt
python main.py
```