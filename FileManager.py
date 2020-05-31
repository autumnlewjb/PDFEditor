from pathlib import Path


class FileManager:
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
