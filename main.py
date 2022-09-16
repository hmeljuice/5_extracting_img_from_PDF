import fitz
import os

class pdf_document:

    def __init__(self, file_path):
        self.doc = self.load(file_path)


    def load(self, file_path, import_pdf=False, import_jpg=False):
        """
        Loads PDF document into object
        :return: Document object
        """
        file_name = self.extract_filename(file_path)

        if file_name[1] == ".pdf":
            document_data = fitz.open(f"{file_path}")
            return document_data
        else:
            message = f"# Your document is NOT pdf file. It's: {file_name[1]} file. #"
            print(f"{'#' * len(message)}\n{message}\n{'#' * len(message)}")


    def extract_filename(self, file_name):
        temp_name, temp_extension = os.path.splitext(file_name)
        return temp_name, temp_extension


    def extract_images(self, document_object=None):
        """
        Method for extracting images from PDF document object.
        If there is no specific document object passed to this metthod as argument,
        default class document object is used.

        Then it stores extracted images from that document.

        :param document_object: You can pass in
        :return:
        """
        if document_object is None:
            document_object = self.doc

        for page in document_object:
            temp_xref = page.get_images()
            image_number = 0
            for page_object in temp_xref:
                print(page_object)
                img = self.doc.extract_image(page_object[0])
                export_img = open(f"page{page.number}-image{image_number}.{img['ext']}", "wb")
                export_img.write(img["image"])
                export_img.close()
                image_number += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    document_object = pdf_document("C:\\Users\\Yugo\\PycharmProjects\\4_extracting_img_from_PDF\\1pdf.pdf")
    document_object.extract_images()
