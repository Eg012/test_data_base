import json
from os import path
import click
from datetime import datetime

file_name = 'notes.json'


@click.group()
def cli():
    pass


@cli.group()
def note():
    pass


@cli.group()
def calendar():
    pass


@note.command()
@click.option("-n", '--name', prompt='Note name', help='Name of note')
@click.option("-nt", '--note', prompt='Note', help='Note text')
@click.option("-r", '--reminder', prompt='reminder_day', help='date')
def create(name, note, reminder):
    global file_name
    data1 = {}
    if path.exists(file_name):
        with open(file_name, 'r') as file_json:
            data1 = json.load(file_json)

    date, time = reminder.split(" ")
    date = date.split(".")
    time = time.split(":")

    data1[name] = {
        "name": name,
        "note": note,
        "reminder_date": datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1])).timestamp()
    }
    with open(file_name, 'w') as file_json:
        json.dump(data1, file_json)


@note.command()
@click.argument("name")
def get(name):
    global file_name
    data = {}
    if not path.exists(file_name):
        click.echo(f"{file_name} not exists", err=True)
        return
    data[name] = {
        "name": "task"
    }

    with open(file_name, 'r') as file_json:
        data = json.load(file_json)

    print(data[name]["note"], "\n", data[name]["reminder_date"])


@calendar.command()
def today():
    global file_name
    data = {}
    if not path.exists(file_name):
        click.echo(f"{file_name} not exists", err=True)
        return

    with open(file_name, 'r') as file_json:
        data = json.load(file_json)

    today_date = datetime.today()

    notes = []
    for item in data.values():
        reminder = datetime.fromtimestamp(item["reminder_date"])
        if today_date.day == reminder.day and today_date.month == reminder.month and today_date.year == reminder.year:
            notes.append(item)

    print(notes)


if __name__ == '__main__':
    cli()
