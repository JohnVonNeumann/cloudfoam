from shutil import copy

import click


@click.command()
@click.argument('template')
@click.argument('dest')
def main(template, dest):
    copy(template, dest)
    click.echo("Done")


if __name__ == "__main__":
    main()
