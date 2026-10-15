from html import escape#
import re
import pymupdf

from pymupdf import pymupdf_git_diff

book = "books/EnsayosTeoriaPolitica.pdf"
title = "Ensayos de teoría política"

# start_page = 8
# end_page = 10

class Chapter:

    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page

def ConvertChapterToHTML(book, chapter):

    start_page = chapter.start_page
    end_page = chapter.end_page

    with (pymupdf.open(book) as doc):
        with open(book[book.find("/") + 1:-4] + ".html", "w", encoding="utf-8") as file:

            page = doc[start_page-1]

            title_rect = pymupdf.Rect(0, 0, page.rect.width, 130)
            title = page.get_text("text", clip=title_rect).split()

            # This is to ensure the roman index stays on top always and it's not removed or merged with the text
            roman_index = None
            for current_block in title:
                if all(x in set('IVXLCDM') for x in current_block):
                    roman_index = current_block
                    break
            if roman_index:
                title.remove(roman_index)
                title = roman_index + "\n" + "".join([x + " " for x in title])


            #.strip().replace("*", "").replace("\n", "")
            print(title)


#chapter1 = Chapter(13, 32)
chapter2 = Chapter(33, 32)

ConvertChapterToHTML(book, chapter2)
# with pymupdf.open(book) as doc:
#
#     with open(book[book.find("/") + 1:-4] + ".html", "w", encoding="utf-8") as file:
#         file.write("<!DOCTYPE html><html><head>")
#         file.write('<meta charset="utf-8">')
#         file.write(f"<title>{title}</title>")
#         file.write("</head><body>")
#
#         for page in doc:
#
#             text = page.get_text("text", sort=True).strip()
#
#             paragraphs = text.split("\n\n")
#
#             for paragraph in paragraphs:
#                 paragraph = paragraph.strip()
#                 if paragraph:
#                     file.write(f"<p>{escape(paragraph)}</p>\n")
