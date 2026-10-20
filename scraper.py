# # ============================================================
# # WHAT THIS SCRIPT DOES (beginner explanation)
# # ------------------------------------------------------------
# # 1. Downloads a Wikipedia page (the Game of Thrones episode list).
# # 2. Finds every table on that page (there are several: an
# #    overview, one per season, a specials table, a DVD table,
# #    and a ratings table).
# # 3. Reads every row and every cell of every table.
# # 4. Writes ALL of those rows into ONE single CSV file, so you
# #    can open it in Excel / Google Sheets.
# #
# # We add a "section" column as the first column of every row so
# # you can tell WHICH table each row came from (otherwise all the
# # rows would be mixed up with no context).
# # ============================================================
#
# # 'csv' is a built-in Python library for writing CSV files.
# # CSV = Comma Separated Values (a plain text spreadsheet format).
# import csv
#
# # 're' is Python's "regular expressions" library.
# # We use it to clean up messy whitespace and remove things
# # like "[11]" (footnote reference numbers) from the text.
# import re
#
# # 'requests' is a third-party library that downloads web pages.
# # Install it once with:  pip install requests
# import requests
#
# # 'BeautifulSoup' comes from the 'bs4' library (BeautifulSoup4).
# # It parses raw HTML into a structure we can search easily.
# # Install it once with:  pip install beautifulsoup4
# from bs4 import BeautifulSoup
#
# # The URL of the Wikipedia page we want to scrape.
# URL = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
#
# # HTTP headers we send with our request.
# # Wikipedia's robot policy REQUIRES a descriptive User-Agent
# # (otherwise it returns a 403 error, as you saw earlier).
# # 'Accept-Encoding: gzip' tells Wikipedia to compress the
# # response, which is faster and uses less bandwidth.
# HEADERS = {
#     "User-Agent": "GoTScraper/1.0 (https://example.com/contact; you@example.com) python-requests",
#     "Accept-Encoding": "gzip",
# }
#
# # Download the page. 'timeout=30' means: give up after 30 seconds
# # instead of hanging forever if the server is slow.
# resp = requests.get(URL, headers=HEADERS, timeout=30)
#
# # '.raise_for_status()' throws an error if the server returned
# # a failure code (like 403 Forbidden or 404 Not Found).
# # If we get here without an error, we know the download worked.
# resp.raise_for_status()
#
# # 'resp.text' is the raw HTML of the page as a string.
# # BeautifulSoup parses it using Python's built-in 'html.parser'.
# soup = BeautifulSoup(resp.text, "html.parser")
#
# # Find EVERY <table> tag on the page that has class "wikitable".
# # 'class_=' (with an underscore) is how BeautifulSoup takes a
# # CSS class name, because 'class' is a reserved Python keyword.
# # Wikipedia uses this class for all its data tables, so this
# # skips navigation boxes, infoboxes, etc.
# tables = soup.find_all("table", class_="wikitable")
#
# # Print how many tables we found so we know the scrape worked.
# print(f"Found {len(tables)} tables")
#
# # ------------------------------------------------------------
# # Open the output CSV file for writing.
# # 'w'  = write mode (overwrites any existing file).
# # 'newline=""' prevents blank lines between rows on Windows.
# # 'encoding="utf-8"' supports special characters like "é".
# # The 'with' block automatically closes the file when done.
# # ------------------------------------------------------------
# with open("got_all_tables.csv", "w", newline="", encoding="utf-8") as f:
#
#     # 'writer' is the object that actually writes rows to the file.
#     writer = csv.writer(f)
#
#     # Write the header row (the first line of the CSV).
#     # We add "section" so we know which table each row came from.
#     writer.writerow(["section", "row", "col1", "col2", "col3",
#                      "col4", "col5", "col6", "col7", "col8",
#                      "col9", "col10", "col11"])
#
#     # Loop over every table, numbered from 1.
#     # 'enumerate' gives us both the index (i) and the table.
#     for table_index, table in enumerate(tables, start=1):
#
#         # Try to find the nearest heading (h2/h3/h4) ABOVE this
#         # table, so we can label the section (e.g. "Season 1 (2011)").
#         # 'find_previous' searches backwards through the document.
#         heading = table.find_previous(["h2", "h3", "h4"])
#
#         # If a heading exists, use its text; otherwise use a
#         # generic label like "table_3".
#         if heading:
#             section_name = heading.get_text(" ")
#         else:
#             section_name = f"table_{table_index}"
#
#         # Remove footnote markers like "[11]" from the section name.
#         # r"\[\d+\]" means: a literal '[', one or more digits, ']'.
#         section_name = re.sub(r"\[\d+\]", "", section_name)
#
#         # Collapse runs of whitespace (newlines, tabs, double spaces)
#         # into a single space, then trim leading/trailing spaces.
#         section_name = re.sub(r"\s+", " ", section_name).strip()
#
#         # Print the section name so we can follow along in the console.
#         print(f"\nTable {table_index}: {section_name}")
#
#         # Get every row of THIS table. A row is a <tr> tag.
#         trs = table.find_all("tr")
#
#         # Loop over each row, numbered from 1.
#         for row_index, tr in enumerate(trs, start=1):
#
#             # Get every cell in the row. Cells are <td> (data)
#             # or <th> (header). Usually headers are only in row 1,
#             # but some Wikipedia tables mix them in.
#             cells = tr.find_all(["th", "td"])
#
#             # Some <tr> rows are empty or only contain a colspan
#             # spacer. Skip them so we don't write blank lines.
#             if not cells:
#                 continue
#
#             # This list will hold the cleaned text of each cell.
#             row_values = []
#
#             # Loop over each cell in the row.
#             for cell in cells:
#
#                 # 'get_text(" ")' pulls only the visible text out
#                 # of the HTML (ignores tags) and joins pieces with
#                 # a space. Example: "<b>Hi</b> there" -> "Hi there".
#                 text = cell.get_text(" ")
#
#                 # Remove footnote markers like "[19]".
#                 text = re.sub(r"\[\d+\]", "", text)
#
#                 # Collapse whitespace and trim.
#                 text = re.sub(r"\s+", " ", text).strip()
#
#                 # Read how many columns this cell spans.
#                 # 'colspan="2"' means the cell covers 2 columns.
#                 # If the attribute is missing, default to 1.
#                 colspan = cell.get("colspan", 1)
#
#                 # Convert to integer. Wikipedia sometimes writes
#                 # colspan as a string like "2" and sometimes as a
#                 # number. 'int(...)' handles both.
#                 colspan = int(colspan)
#
#                 # Append the cell's text once for each column it spans.
#                 for _ in range(colspan):
#                     row_values.append(text)
#
#             # Write this row to the CSV.
#             # We put 'section_name' and 'row_index' first,
#             # then the cell values. Python's csv writer handles
#             # commas and quotes inside values automatically.
#             writer.writerow([section_name, row_index] + row_values)
#
#             # Print the row to the console too (handy for checking).
#             print(f"  row {row_index}: {row_values}")
#
# # This line runs after the 'with' block, i.e. after the file
# # has been closed. It's just a friendly confirmation message.
# print("\nDone! Saved all tables to got_all_tables.csv")
# 1. Import the tools we need.
import requests                     # downloads the web page
from bs4 import BeautifulSoup       # reads the HTML
import csv                          # writes the CSV file

# 2. The page we want to scrape.
url = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"

# 3. Tell the website who we are (Wikipedia blocks fake browsers).
headers = {"User-Agent": "MyScraper/1.0 (you@example.com)"}

# 4. Download the page.
page = requests.get(url, headers=headers)

# 5. Turn the HTML into something we can search.
soup = BeautifulSoup(page.text, "html.parser")

# 6. Find every table on the page.
tables = soup.find_all("table")

# 7. Open a CSV file to write into.
with open("got.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # 8. Go through each table one by one.
    for table in tables:

        # 9. Go through each row of the table.
        for row in table.find_all("tr"):

            # 10. Get every cell in that row.
            cells = row.find_all(["th", "td"])

            # 11. Skip rows that have no cells.
            if not cells:
                continue

            # 12. Make a list of the text inside each cell.
            texts = []
            for cell in cells:
                texts.append(cell.get_text(strip=True))

            # 13. Write this row to the CSV file.
            writer.writerow(texts)

print("Done! Open got.csv")