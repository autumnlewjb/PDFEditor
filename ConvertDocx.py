from FileManager import FileManager


class ConvertDocx(FileManager):

    def add_description(self):
        self.description = "convert docs"

    def implement(self):
        pass


if __name__ == '__main__':
    new_docx = ConvertDocx()
    print(new_docx.description)
