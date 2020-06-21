import click
from modules.zdb import Client
from modules.models import Tenet, Achievement


@click.group()
@click.option("--db-location", default="tenets.json")
@click.pass_context
def cli(ctx, db_location):
    ctx.obj = Client(location=db_location)


@cli.command()
@click.pass_context
def add_tenets(ctx):
    tenets = []
    while True:
        description = click.prompt("Enter description", type=str)
        frequency = click.prompt("Enter frequency", type=int)
        days = click.prompt("Enter days", type=int)

        tenets.append(Tenet(description, frequency, days))

        if click.confirm("Add another?", default=True):
            continue
        else:
            ctx.obj.set("tenets", tenets)
            break


@cli.command()
@click.pass_context
def get_tenets(ctx):
    tenets = ctx.obj.get("tenets")
    print(tenets)
    return tenets
