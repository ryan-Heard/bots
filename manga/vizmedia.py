from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date

VIZ_SITE = 'https://www.viz.com/shonenjump/chapters/'


def read_manga_html(manga: str) -> str:
    link = VIZ_SITE + manga
    html_doc = requests.get(link).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find("div", {"class": "o_sortable brdr-dotted-lid"})
    row = table.find('td', {"valign":"middle"})

    # See if the manga was updated today
    if datetime.datetime.strptime(row.getText(), '%B %d, %Y').date() == date.today():
        return "{} was updated. You can read it at {}".format(manga, link)
    else:
        return ''

if __name__ == "__main__":
    read_manga_html('my-hero-academia')