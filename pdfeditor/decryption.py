from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfeditor.file_manager import FileManager


class Decryption(FileManager):
    # def __init__(self, read_name=None, write_name=None):
    #     super().__init__(read_name, write_name)
    #     self.description = 'Decryption and Make New File'

    def add_description(self):
        self.description = 'Decryption and Make New File'

    def decrypt_file(self, password):
        reader = PdfFileReader(str(self.read_dir))
        writer = PdfFileWriter()
        reader.decrypt(password)
        writer.appendPagesFromReader(reader)

        with self.write_dir.open(mode='wb') as output_file:
            writer.write(output_file)

    def implement(self):
        password = str(input('Password: '))
        self.decrypt_file(password)


if __name__ == '__main__':
    new_decrypt = Decryption('write_file', 'write_file_decrypted')
    new_decrypt.decrypt_file('autumnlewjb')
