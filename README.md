# QR Generator

## Overview
Tiny Python script to generate a PNG QR code into `sample_output/`.  

## Requirements
- Python **3.12** (works on 3.10+)
- `pip`
- Dependencies listed in `requirements.txt`

## Setup & Run
```bash
# Clone and enter
git clone https://github.com/sghimire2025/MSCS-633-Assignment2-QR-Code-Generator
cd MSCS-633-Assignment2-QR-Code-Generator

# Create & activate venv
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

# Install deps
pip install -U pip wheel
pip install -r requirements.txt

# Generate QR
python qr_generator.py
# Output: sample_output/qr_bioxsystems.png
```

## Project Structure
```
repo-root/
├─ sample_output/          
├─ .gitignore              
├─ qr_generator.py         
├─ README.md               
└─ requirements.txt        
```
