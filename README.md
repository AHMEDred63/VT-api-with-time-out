# VirusTotal Hash Uploader

This Python script is designed to upload hash values to VirusTotal in batches. It respects the VirusTotal API rate limits by introducing a delay between batches, preventing any quota overages.

## Features
- Uploads hash values from a CSV file.
- Handles API rate limits by adding delays.
- Provides clear output for each batch uploaded.

## Usage
1. Prepare a CSV file with one hash per line.
2. Replace `YOUR_API_KEY` in the script with your VirusTotal API key.
3. Run the script.

## Requirements
- Python 3.x
- `requests` library

## License
This project is open-source.

