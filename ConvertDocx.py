from FileManager import FileManager
from PyPDF2 import PdfFileReader
from docx import Document
from pathlib import Path


total_pages = 0


class ConvertDocx(FileManager):
    @property
    def write_dir(self):
        return self._write_dir

    @write_dir.setter
    def write_dir(self, value):
        p = Path()
        self._write_dir = p.home() / 'Documents' / 'Python' / 'Python Projects' / 'PdfEditor' / 'Pdf' / (str(value) + '.docx')

    def add_description(self):
        self.description = 'Convert PDF to Docs'

    def get_total_pages(self):
        global total_pages
        pdf_reader = PdfFileReader(str(self.read_dir))
        total_pages = pdf_reader.getNumPages()

    def convert_docx(self, page_index=0, document=None):
        if document is None:
            document = Document()

        pdf_reader = PdfFileReader(str(self.read_dir))
        page_object = pdf_reader.getPage(page_index)
        content = page_object.extractText()
        document.add_paragraph(str(content))
        document.add_page_break()

        if page_index < total_pages-1:
            return self.convert_docx(page_index+1, document)
        else:
            return document.save(self.write_dir)

    def implement(self):
        self.get_total_pages()
        self.convert_docx()


if __name__ == '__main__':
    new_docx = ConvertDocx('extract', 'extract')
    print(new_docx.description)
    new_docx.implement()
