from html import escape#
import re
import pymupdf

book = "books/EnsayosTeoriaPolitica.pdf"
title = "Ensayos de teoría política"

# start_page = 8
# end_page = 10


with pymupdf.open(book) as doc:
    with open(book[book.find("/")+1:-4]+".html", "w", encoding="utf-8") as file:
        file.write("<!DOCTYPE html><html><head>")
        file.write('<meta charset="utf-8">')
        file.write(f"<title>{title}</title>")
        file.write("</head><body>")

        for page in doc:

            text = page.get_text("text", sort=True).strip()

            paragraphs = text.split("\n\n")

            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                if paragraph:
                    file.write(f"<p>{escape(paragraph)}</p>\n")
