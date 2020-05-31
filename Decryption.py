from PyPDF2 import PdfFileReader, PdfFileWriter
import os


class Decryption:
    def __init__(self, read_name, write_name):
        self.read_dir = read_name
        self.write_dir = write_name

    @property
    def read_dir(self):
        return self._read_dir

    @read_dir.setter
    def read_dir(self, value):
        home_dir = r'C:\\Users\Autumn'
        self._read_dir = os.path.join(home_dir, r'Documents\Python\Python Projects\Pdf', str(value) + '.pdf')

    @property
    def write_dir(self):
        return self._write_dir

    @write_dir.setter
    def write_dir(self, value):
        same = os.path.split(self.read_dir)
        self._write_dir = os.path.join(same[0], str(value) + '.pdf')

    def decrypt_file(self, password):
        reader = PdfFileReader(self.read_dir)
        writer = PdfFileWriter()
        reader.decrypt(password)
        writer.appendPagesFromReader(reader)

        with open(self.write_dir, 'wb') as output_file:
            writer.write(output_file)


if __name__ == '__main__':
    new_decrypt = Decryption('write_file', 'write_file_decrypted')
    new_decrypt.decrypt_file('autumnlewjb')
