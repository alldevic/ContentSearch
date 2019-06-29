import click


@click.command()
@click.option("--url", help="Source URL", required=True)
@click.option("--out", help="Destination file", required=True)
def main(url, out):
    """
    A simple content parser for URL.
    This tool will find content blocks and write out onformation to out file.
    """
    print(url)
    print(out)


if __name__ == "__main__":
    main()
