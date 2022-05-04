import json
from os import path
import click
from datetime import datetime

file_name = 'notes.json'

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


@click.group()
def cli():
    pass


@cli.command()
def get_date():
    click.echo(datetime.now())


@cli.command()
@click.option('--name', prompt='Note name', help='Name of note')
@click.option('--note', prompt='Note', help='Note text')
@click.option('--reminder', prompt='reminder_day', help='date')
def create_note(name, note):
    global file_name
    data = {}
    if path.exists(file_name):
        with open(file_name, 'r') as file_json:
            data = json.load(file_json)

    data[name] = {
        "note": note,
        "reminder_date": None
    }

    with open(file_name, 'w') as file_json:
        json.dump(data, file_json)


@cli.command()
@click.option('--name', prompt='Note name', help='Name of note')
@click.option('--reminder', prompt='reminder_day', help='date')
@click.option('--note', prompt='Note', help='Note text')
def reminder_data(name, reminder, note):
    global file_name
    data1 = {}
    if path.exists(file_name):
        with open(file_name, 'r') as file_json:
            data1 = json.load(file_json)
    data1[name] = {
        "note": note,
        "reminder_date": reminder

    }
    with open(file_name, 'w') as file_json:
        json.dump(data1, file_json)


@cli.command()
@click.argument("name")
def get_note(name):
    global file_name
    data = {}
    if not path.exists(file_name):
        click.echo(f"{file_name} not exists", err=True)
        return

    with open(file_name, 'r') as file_json:
         data = json.load(file_json)

    print(data[name])

if __name__ == '__main__':
    cli()
