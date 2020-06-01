from FileManager import FileManager
from PyPDF2 import PdfFileWriter, PdfFileReader


class Extraction(FileManager):
    # def __init__(self, read_name=None, write_name=None):
    #     super().__init__(read_name, write_name)
    #     self.description = 'Extraction to New File'

    def add_description(self):
        self.description = 'Extraction to New File'

    def extract_pdf(self, start, stop):
        start -= 1
        reader = PdfFileReader(str(self.read_dir))
        writer = PdfFileWriter()

        for page in reader.pages[start:stop:1]:
            writer.addPage(page)

        with self.write_dir.open(mode='wb') as output_file:
            writer.write(output_file)

    def implement(self):
        start = int(input('Inclusively start from page '))
        stop = int(input('Inclusively stop at page '))
        self.extract_pdf(start, stop)


if __name__ == '__main__':
    new_extract = Extraction('olympiad-number-theory', 'extract')
    # new_extract.extract_pdf(4, 8)
    print(new_extract.description)
