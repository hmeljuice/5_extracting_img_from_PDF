import fitz
import os

import sys

class pdf_document:

    def __init__(self, file_path):
        self.file_path = file_path

        self.doc = self.load(file_path)


    def load(self, file_path, import_pdf=False, import_jpg=False):
        """
        method for loading PDF document or JPG image into PDF object
        :return: 0. document object
        """
        file_name = self.extract_filename(file_path)
        print(file_name)

        if file_name[1] == ".pdf":
            document_data = fitz.open(f"{file_path}")
            return document_data
        else:
            print(f"Your document is not {file_name[1]} file.")


    def extract_filename(self, file_name):
        temp_name, temp_extension = os.path.splitext(file_name)
        return temp_name, temp_extension


    def extract_images(self):
        for page in self.doc:
            temp_xref = page.get_images()
            image_number = 0
            for page_object in temp_xref:
                print(page_object)
                img = self.doc.extract_image(page_object[0])
                export_img = open(f"image{image_number}.{img['ext']}", "wb")
                export_img.write(img["image"])
                export_img.close()
                image_number += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    document_object = pdf_document("C:\\Users\\Yugo\\PycharmProjects\\4_extracting_img_from_PDF\\123pdf.pdf")
    document_object.extract_images()
