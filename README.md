

# Universal PDF Dropper: Full-Page Link Injection for Modern Browsers

*For educational purposes only.* 🔒

Inject a full-page, invisible link into any PDF so that clicking anywhere in the document opens your chosen URL—no Acrobat-only JavaScript required.

## 🚀 Features
- **Full-Page Injection**: Invisible `/URI` annotation across the entire page.
- **Cross-Viewer Support**: Compatible with Chrome, Firefox, Preview, Acrobat, etc.
- **Pure Python**: Uses `pypdf`, no JS or Acrobat plugins.
- **CLI**: Quick one-liner to craft your dropper.

## 📋 Prerequisites
- Python 3.6+
- `venv` or `virtualenv`
- A safe base PDF (`original.pdf`)

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/pdfdropper.git
cd pdfdropper
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate.ps1
pip install -r requirements.txt
cp /path/to/your.pdf original.pdf
