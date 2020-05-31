from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


class Encryption:
    def __init__(self, read_name, write_name):
        self.read_dir = read_name
        self.write_dir = write_name

    @property
    def read_dir(self):
        return self._read_dir

    @read_dir.setter
    def read_dir(self, value):
        p = Path()
        self._read_dir = p.home() / 'Documents' / 'Python' / 'Python Projects' / 'Pdf' / (str(value) + '.pdf')

    @property
    def write_dir(self):
        return self._write_dir

    @write_dir.setter
    def write_dir(self, value):
        p = Path()
        self._write_dir = p.home() / 'Documents' / 'Python' / 'Python Projects' / 'Pdf' / (str(value) + '.pdf')

    def encrypt_pdf(self, password):
        file_reader = PdfFileReader(str(self.read_dir))
        file_writer = PdfFileWriter()
        file_writer.appendPagesFromReader(file_reader)
        file_writer.encrypt(password)
        with self.write_dir.open(mode='wb') as write_file:
            file_writer.write(write_file)


if __name__ == '__main__':
    en = Encryption('MS1913108800', 'write_file')
    en.encrypt_pdf('autumnlewjb')
