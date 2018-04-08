# function ( file_to_copy, location_to_copy_to )
#     set file_to_copy
#     set location_to_copy_to
#     generate actual paths from the input strings
#     create copy of file
#     set copy
#     send copy to location
#     exit

from shutil import copyfile, copy

import click

@click.command()
@click.argument('template')
@click.argument('dest')

def main(template, dest):
    copy(template, dest)
    click.echo("Done")

if __name__ == "__main__":
    main() 
