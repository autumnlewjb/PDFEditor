from FileManager import FileManager
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from pathlib import Path


class Split(FileManager):
    def __init__(self, read_name, write_name, write_folder):
        super().__init__(read_name, write_name)
        self.write_folder = write_folder

    @property
    def write_folder(self):
        return self._write_folder

    @write_folder.setter
    def write_folder(self, value):
        p = Path()
        self._write_folder = p.home() / 'Documents' / 'Python' / 'Python Projects' / 'Pdf' / (str(value))

    def create_folder(self):
        if not os.path.exists(self.write_folder):
            os.mkdir(self.write_folder)

    def split_pdf(self):
        reader = PdfFileReader(str(self.read_dir))
        number = 1

        for page in reader.pages:
            writer = PdfFileWriter()
            writer.addPage(page)
            new_dir = list(os.path.splitext(self.write_dir))
            new_dir.insert(1, str(number))
            directory = "".join(new_dir)
            with open(directory, mode='wb') as output_file:
                writer.write(output_file)

            number += 1


if __name__ == '__main__':
    pdf = Split('olympiad-number-theory')

