from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, NameObject

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
