from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
from FileManager import FileManager


class Encryption(FileManager):
    # def __init__(self, read_name=None, write_name=None):
    #     super().__init__(read_name, write_name)
    #     self.description = 'Encryption and Make New File'

    def add_description(self):
        self.description = 'Encryption and Make New File'

    def encrypt_pdf(self, password):
        file_reader = PdfFileReader(str(self.read_dir))
        file_writer = PdfFileWriter()
        file_writer.appendPagesFromReader(file_reader)
        file_writer.encrypt(password)
        with self.write_dir.open(mode='wb') as write_file:
            file_writer.write(write_file)

    def implement(self):
        password = str(input('Password: '))
        self.encrypt_pdf(password)


if __name__ == '__main__':
    en = Encryption('MS1913108800', 'write_file')
    en.encrypt_pdf('autumnlewjb')
    print(en.description)
