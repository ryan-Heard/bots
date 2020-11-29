from bs4 import BeautifulSoup
import requests

VIZ_SITE = 'https://www.viz.com/shonenjump/chapters/'


def read_manga_html(manga: str) -> str:
    link = VIZ_SITE + manga
    
    html_doc = requests.get(link).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find("div", {"class": "o_sortable brdr-dotted-lid"})
    row = table.find('td', {"valign":"middle"})

    # if row.getText().split(' ')[0] == "Today":
    return "{} was updated. You can read it at {}".format(manga, link)

    #print(soup.prettify())


if __name__ == "__main__":
    read_manga_html('my-hero-academia')