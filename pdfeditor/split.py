from pdfeditor.file_manager import FileManager
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from pathlib import Path
import copy


class Split(FileManager):
    def __init__(self, read_name=None, write_name=None, write_folder=None):
        super().__init__(read_name, write_name)
        self.write_folder = write_folder
        # self.description = 'Split All Pages into Small Files'

    @property
    def write_folder(self):
        return self._write_folder

    @write_folder.setter
    def write_folder(self, value):
        p = Path()
        self._write_folder = p.home() / 'Documents' / 'Python' / 'Python Projects' / 'PdfEditor' / 'output' / (str(value))

    @property
    def write_dir(self):
        return self._write_dir

    @write_dir.setter
    def write_dir(self, value):
        self._write_dir = value

    def add_description(self):
        self.description = 'Split All Pages into Small Files'

    def create_folder(self):
        if not os.path.exists(str(self.write_folder)):
            os.mkdir(str(self.write_folder))

    def split_pdf(self):
        reader = PdfFileReader(str(self.read_dir))
        # in this case self.write_dir is the pdf name
        raw = str(self.write_folder / (str(self.write_dir) + '.pdf'))
        new_dir = list(os.path.splitext(raw))
        number = 1

        for page in reader.pages:
            writer = PdfFileWriter()
            writer.addPage(page)
            edit_dir = copy.deepcopy(new_dir)
            edit_dir.insert(1, '-page-' + str(number))
            processed = "".join(edit_dir)
            with open(processed, mode='wb') as output_file:
                writer.write(output_file)

            number += 1

    def implement(self):
        self.write_folder = str(input('Folder name: '))
        self.create_folder()
        self.split_pdf()


if __name__ == '__main__':
    pdf = Split('olympiad-number-theory', 'split_pdf', 'splits')
    # pdf.create_folder()
    # pdf.split_pdf()
    print(pdf.description)
