from os import path
from os import remove

import click
from click.testing import CliRunner

from cloudfoam import main


def test_cli_copy():
    cwd = path.realpath('.')
    test_file = path.join(cwd, 'test.yaml')
    runner = CliRunner()
    result = runner.invoke(main,
                           ['AWS::EC2::Subnet.yaml',
                            test_file])
    assert path.exists(test_file)
    remove(test_file)


if __name__ == "__main__":
    test_cli_copy()
