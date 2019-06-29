import click
import requests
from bs4 import BeautifulSoup, Comment
import html5lib


@click.command()
@click.option("--url", help="Source URL", required=True)
@click.option("--out", help="Destination file", required=True)
def main(url, out):
    """
    A simple content parser for URL.
    This tool will find content blocks and write out onformation to out file.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    response = requests.get(url, headers)

    soup = BeautifulSoup(response.text, 'html5lib').body

    ignored_tags = ['script', 'header', 'footer', 'style', 'noscript']
    for tag in ignored_tags:
        for entity in soup(tag):
            entity.decompose()

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    with open(out, 'w') as output_file:
        output_file.write(soup.prettify())


if __name__ == "__main__":
    main()
