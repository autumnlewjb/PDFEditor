import abc
from pathlib import Path
import os


class FileManager(metaclass=abc.ABCMeta):
    def __init__(self, read_name=None, write_name=None):
        self.read_dir = read_name
        self.write_dir = write_name
        self.description = None
        self.add_description()

    @property
    def read_dir(self):
        return self._read_dir

    @read_dir.setter
    def read_dir(self, value):
        self._read_dir = Path(os.getcwd()) / '..' / 'resources' / (str(value) + '.pdf')
        print(self._read_dir)

    @property
    def write_dir(self):
        return self._write_dir

    @write_dir.setter
    def write_dir(self, value):
        self._write_dir = Path(os.getcwd()) / '..' / 'output' / (str(value) + '.pdf')

    @abc.abstractmethod
    def add_description(self):
        pass

    @abc.abstractmethod
    def implement(self):
        pass

