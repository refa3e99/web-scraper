from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/History_of_Mexico#cite_note-133"


def get_citations_needed_count(url_string):
    page = requests.get(url_string)
    soup = BeautifulSoup(page.content, "html.parser")
    tags = soup.find(class_="vector-body")
    p_tags = tags.find_all("p")

    counter = 0

    for tag_p in p_tags:
        content = tag_p.text
        if "citation needed" in content:
            counter += 1

    return counter


def get_citations_needed_report(url_string):
    page = requests.get(url_string)
    soup = BeautifulSoup(page.content, "html.parser")
    tags = soup.find(class_="vector-body")
    p_tags = tags.find_all("p")

    text = ""

    for p_tag in p_tags:
        content = p_tag.text
        if "citation needed" in content:
            text += content

    return text


if __name__ == "__main__":

    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
