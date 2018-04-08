from os import path
from os import remove

import click
from click.testing import CliRunner

from cloudfoam import main


def test_cli_copy():
    runner = CliRunner()
    result = runner.invoke(main,
                           ['AWS::EC2::Subnet.yaml',
                            '/home/lw/code/open_source/cloudfoam/test.yaml'])
    assert path.exists('/home/lw/code/open_source/cloudfoam/test.yaml')
    remove('/home/lw/code/open_source/cloudfoam/test.yaml')


if __name__ == "__main__":
    test_cli_copy()
