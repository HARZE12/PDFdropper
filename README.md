![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/yourusername/pdfdropper/python-app.yml?branch=main)

# Universal PDF Dropper: Full-Page Link Injection for Modern Browsers

*For educational purposes only.* 🔒

Inject a full-page, invisible link into any PDF so that clicking anywhere in the document opens your chosen URL—no Acrobat-only JavaScript required.

## 🚀 Features
- Full-Page Injection
- Cross-Viewer Support
- Pure Python (pypdf)
- CLI Tool

## 📋 Prerequisites
- Python 3.6+
- venv or virtualenv
- Base PDF (`original.pdf`)

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/pdfdropper.git
cd pdfdropper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp /path/to/your.pdf original.pdf
