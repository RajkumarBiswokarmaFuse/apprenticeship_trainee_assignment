# Design a document generator using the Builder Design
# Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF,
# HTML, Plain Text). Implement the builder methods to format the document content and
# structure according to the chosen type. Demonstrate how the Builder Design Pattern
# allows for the creation of different document formats without tightly coupling the
# document generation logic.

from abc import ABC, abstractmethod

# Document Builder interface
class DocumentBuilder(ABC):
    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def add_heading(self, heading):
        pass

    @abstractmethod
    def add_paragraph(self, paragraph):
        pass

    @abstractmethod
    def get_result(self):
        pass

# Concrete PDF Document Builder
class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.pdf_document = PDFDocument()

    def set_title(self, title):
        self.pdf_document.add_content(f"Title: {title}")

    def add_heading(self, heading):
        self.pdf_document.add_content(f"\n{heading}\n")

    def add_paragraph(self, paragraph):
        self.pdf_document.add_content(f"{paragraph}\n")

    def get_result(self):
        return self.pdf_document

# Concrete HTML Document Builder
class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.html_document = "<html><head><title></title></head><body>"

    def set_title(self, title):
        self.html_document = self.html_document.replace("<title></title>", f"<title>{title}</title>")

    def add_heading(self, heading):
        self.html_document += f"<h1>{heading}</h1>"

    def add_paragraph(self, paragraph):
        self.html_document += f"<p>{paragraph}</p>"

    def get_result(self):
        return self.html_document + "</body></html>"

# Concrete Plain Text Document Builder
class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.plain_text_document = ""

    def set_title(self, title):
        self.plain_text_document += f"Title: {title}\n"

    def add_heading(self, heading):
        self.plain_text_document += f"\n{heading}\n"

    def add_paragraph(self, paragraph):
        self.plain_text_document += f"{paragraph}\n"

    def get_result(self):
        return self.plain_text_document


# Document Director
class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_document(self, title, heading, paragraphs):
        self.builder.set_title(title)
        self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)

# Product class for PDF Document
class PDFDocument:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content


if __name__ == "__main__":
    title = "Sample "
    heading = "Introduction of Me"
    paragraphs = [
        "Hello I am Raj Kumar Biswokarma. ",
        "I am from Butwal Rupandehi.",
        "I am currently pursing Bachelor degree in Computer Science and Information Technology.",
    ]

    # Create PDF Document
    pdf_builder = PDFDocumentBuilder()
    pdf_director = DocumentDirector(pdf_builder)
    pdf_director.construct_document(title, heading, paragraphs)
    pdf_document = pdf_builder.get_result()
    print("PDF Document:")
    print(pdf_document.content)

    # Create HTML Document
    html_builder = HTMLDocumentBuilder()
    html_director = DocumentDirector(html_builder)
    html_director.construct_document(title, heading, paragraphs)
    html_document = html_builder.get_result()
    print("\nHTML Document:")
    print(html_document)

    # Create Plain Text Document
    plain_text_builder = PlainTextDocumentBuilder()
    plain_text_director = DocumentDirector(plain_text_builder)
    plain_text_director.construct_document(title, heading, paragraphs)
    plain_text_document = plain_text_builder.get_result()
    print("\nPlain Text Document:")
    print(plain_text_document)
