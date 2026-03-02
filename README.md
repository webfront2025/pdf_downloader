# PDF Downloader Project

## Dansk Version

### Projektbeskrivelse
Dette projekt er en simpel PDF-downloader, som henter PDF-filer fra URL’er og gemmer dem lokalt.  
Programmet understøtter parallel downloading ved brug af ThreadPoolExecutor og håndterer fejl som timeout og ugyldige links.

Projektet indeholder også automatiske tests skrevet med unittest.

---

### Funktioner

- Downloader PDF-filer fra angivne URL’er
- Understøtter flere downloads samtidig (multithreading)
- Timeout-håndtering
- Statushåndtering (Success, Failed osv.)
- Automatisk oprettelse af output-mappe


---

### Teknologier

- Python 3
- requests
- concurrent.futures (ThreadPoolExecutor)
- pathlib

---

### Installation

1. Klon projektet
2. Installer dependencies:

```bash
pip install -r requirements.txt
pip install openpyxl pandas requests


python main.py

---
---
---

## English Version

### Project Description
This project is a simple PDF downloader that fetches PDF files from given URLs and saves them locally.  
The program supports parallel downloading using ThreadPoolExecutor and handles errors such as timeouts and invalid links.

The project also includes automated unit tests written with unittest.

---

### Features

- Download PDF files from URLs
- Parallel downloads (multithreading)
- Timeout handling
- Download status management (Success, Failed, etc.)
- Automatic output directory creation
- Unit testing with unittest
- Test discovery via `python -m unittest discover`

---

### Technologies Used

- Python 3
- requests
- unittest
- concurrent.futures (ThreadPoolExecutor)
- pathlib

---

### Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install requests
```

---

### Running Tests

To run all tests:

```bash
python -m unittest discover -s tests
```

Example output:

```
Ran 4 tests in 32.005s
OK
```

---

## About the downloads_test Folder

During testing, a temporary folder named:

```
downloads_test
```

is created.

This folder is only used during test execution.  
If the tests clean up properly (using tearDown), the folder is automatically deleted afterward.

That is why you usually only see the `__pycache__` folder and not `downloads_test`.

---

## Project Status

The project currently includes:

- Working PDF downloader
- Multithreading support
- Excel column validation
- Unit tests
- Test discovery setup






















# PDF Downloader

## Dansk

## Projekt Oversigt

Dette projekt downloader PDF-rapporter fra en liste af URLs i en Excel-fil.  
Nu kan projektet:

- Hente alle rapporter i Excel-filen (ikke kun 10).  
- Bruge en fallback-URL hvis den primære URL fejler.  
- Gemme resultaterne både som CSV og Excel (.xlsx).

## Funktioner

Læser rapporter fra Excel-filen (GRI_2017_2020(1).xlsx).

Downloader PDF-filer til en specificeret output-mappe.

Prøver fallback-URL, hvis primær-URL fejler.

Springer filer over, som allerede er downloadet.

Eksporterer en Markdown-stil CSV, xlsx med kolonner: company, url, status, message, file_path.

## Brug
# Kør programmet
python main.py


## English

## Project Overview 
This project is a Python tool to download PDF reports from a list of URLs provided in an Excel file.  
It now supports:

- Downloading **all reports** in the Excel file, not limited to 10 files.  
- Using a **fallback URL** if the primary URL fails.  
- Exporting the results into both **CSV** and **Excel (.xlsx)** files.  

### Features

- Reads reports from an Excel file (GRI_2017_2020(1).xlsx).
- Downloads PDF files to a specified output folder.
- Tries fallback URLs if the primary URL fails.
- Skips files that are already downloaded.
- Exports a Markdown-style CSV, xlsx with columns:   company, url, status, message, file_path.
- Supports limiting downloads with `max_download` and concurrency with `max_workers`.

### Usage

# Run the program
1. Make sure dependencies are installed:

```bash
pip install -r requirements.txt
pip install openpyxl pandas requests


python main.py