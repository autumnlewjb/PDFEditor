from pdfeditor.encryption import Encryption
from pdfeditor.decryption import Decryption
from pdfeditor.split import Split
from pdfeditor.extraction import Extraction
from pdfeditor.convert_docx import ConvertDocx


menu = {
    '1': Extraction(),
    '2': Split(),
    '3': Encryption(),
    '4': Decryption(),
    '5': ConvertDocx(),
}

if __name__ == '__main__':
    for key, value in menu.items():
        print(key + '-' + value.description)

    user_option = str(input('What would you like to do? '))
    choice = menu[user_option]
    read_directory = str(input('Which file would you like to read? '))
    write_directory = str(input('What you would like to call you new PDF file? '))

    choice.write_dir = write_directory
    choice.read_dir = read_directory

    choice.implement()


