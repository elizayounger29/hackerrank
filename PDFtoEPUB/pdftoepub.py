import fitz  # PyMuPDF
from ebooklib import epub

def pdf_to_epub(pdf_path, epub_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create EPUB book
    book = epub.EpubBook()

    # Add metadata to the EPUB book
    book.set_identifier("your_identifier")
    book.set_title("Your Book Title")
    book.set_language("en")

    # Iterate through PDF pages and add them to the EPUB book
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text = page.get_text("text")
        chapter_title = f"Chapter {page_number + 1}"

        # Create EPUB item
        chapter = epub.EpubItem(uid=f"page{page_number}", file_name=f"page_{page_number}.xhtml", content=text)

        # Create EPUB chapter
        chapter_id = f"chapter_{page_number}"
        c = epub.EpubHtml(title=chapter_title, file_name=f"page_{page_number}.xhtml", lang="en")
        c.content = text
        chapter.add_item(c)
        book.add_item(chapter)

        # Add EPUB chapter to the spine
        book.spine.append(chapter)

    # Create EPUB file
    epub.write_epub(epub_path, book, {})

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    # Replace 'input.pdf' and 'output.epub' with your actual file paths
    pdf_to_epub("Hefted to Islay; The Islay Deer Management.pdf", "Hefted to Islay; The Islay Deer Management.epub")
