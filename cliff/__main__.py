"""
cliff.__main__.py
~~~~~~~~~~~~~~~~~
"""
import logging

import typer
from typer import Option

__version__ = "0.0.1"


LOGGER = logging.getLogger("cliff.__main__")
APP = typer.Typer()


def version_cb(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@APP.callback()
def main(
    version: bool = Option(
        None,
        "--version",
        callback=version_cb,
        is_eager=True,
        help="Return version number and exit.",
    )
):
    LOGGER.debug(version)


if __name__ == "__main__":
    APP(prog_name="cliff")
