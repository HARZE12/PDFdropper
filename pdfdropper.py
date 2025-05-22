#!/usr/bin/env python3
import argparse
from core import Pdf
from linkinject import LinkInject

def run():
    parser = argparse.ArgumentParser(
        prog='pdfdropper-link',
        description='Full-page PDF link injector'
    )
    parser.add_argument('-f',  required=True, help='Input PDF path')
    parser.add_argument('-o',  required=True, help='Output PDF path')
    parser.add_argument('-url', required=True, help='URL to inject')
    args = parser.parse_args()

    pdf = Pdf(args.f)
    injector = LinkInject(args.url)
    injector.exploit(pdf)
    pdf.store(args.o)
    print(f"[+] Wrote link-injected PDF → {args.o}")

if __name__ == "__main__":
    run()
