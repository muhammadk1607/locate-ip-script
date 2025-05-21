# Locale IP Script

This script is designed to fetch the IP address of a given domain and determine its geographical
location using the `ipinfo.io` API. It can be useful for various purposes,
uch as network diagnostics, geolocation services, or simply checking the IP address of a website.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

By default the script looks for a file called `input.csv` in the current directory.
You can specify a different input file using the `-i` or `--input` option.
The output will be saved to a file called `output.csv` in the same directory.
You can specify a different output file using the `-o` or `--output` option.

```bash
python main.py -i input.csv -o output.csv
```

## Input File Format

The input file should be a CSV file with a column named `ip`.

## Output File Format

The output will be the same as the input file, with an additional column named `location`.
