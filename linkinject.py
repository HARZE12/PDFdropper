#!/usr/bin/env python3
import argparse
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DictionaryObject, NameObject, TextStringObject,
    ArrayObject, NumberObject
)

class Pdf:
    def __init__(self, path: str, password: str = None):
        reader = PdfReader(path, password=password)
        self.writer = PdfWriter()
        for page in reader.pages:
            self.writer.add_page(page)

    @property
    def pages(self):
        return self.writer.pages

    def add_object(self, obj):
        return self.writer._add_object(obj)

    def add_annotation(self, page, annot_ref):
        annots = page.get("/Annots")
        if annots is None:
            page[NameObject("/Annots")] = ArrayObject([annot_ref])
        else:
            annots.append(annot_ref)

    def store(self, output_path: str):
        with open(output_path, "wb") as out_f:
            self.writer.write(out_f)

class LinkInject:
    def __init__(self, url: str):
        self.url = url

    def exploit(self, pdf):
        for page in pdf.pages:
            rect = page.mediabox
            annot = DictionaryObject({
                NameObject("/Type"): NameObject("/Annot"),
                NameObject("/Subtype"): NameObject("/Link"),
                NameObject("/Rect"): rect,
                NameObject("/Border"): ArrayObject([
                    NumberObject(0), NumberObject(0), NumberObject(0)
                ]),
                NameObject("/A"): DictionaryObject({
                    NameObject("/S"): NameObject("/URI"),
                    NameObject("/URI"): TextStringObject(self.url),
                }),
            })
            annot_ref = pdf.add_object(annot)
            pdf.add_annotation(page, annot_ref)

def main():
    parser = argparse.ArgumentParser(
        prog='linkinject',
        description='Full-page PDF link injector'
    )
    parser.add_argument('-f', required=True, help='Input PDF path')
    parser.add_argument('-o', required=True, help='Output PDF path')
    parser.add_argument('-url', required=True, help='URL to inject')
    args = parser.parse_args()

    pdf = Pdf(args.f)
    injector = LinkInject(args.url)
    injector.exploit(pdf)
    pdf.store(args.o)
    print(f"[+] Wrote link-injected PDF → {args.o}")

if __name__ == "__main__":
    main()
