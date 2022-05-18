import json
from datetime import datetime
from os import path
import click
import pandas as pd
import numpy as np

file_name = 'notes.json'

now = datetime.now()


@click.group()
def cli():
    pass


@cli.group()
def note():
    """Manipulations with note"""
    pass


@cli.group()
def calendar():
    """checking and outputting notes made today and this week"""
    pass


def get_data():
    global file_name
    if not path.exists(file_name):
        click.echo(f"{file_name} not exists", err=True)
        return

    data = {}
    if path.exists(file_name):
        with open(file_name, 'r') as file_json:
            data = json.load(file_json)
    return data


def set_data(data):
    global file_name
    if not path.exists(file_name):
        click.echo(f"{file_name} not exists", err=True)
        return

    with open(file_name, 'w') as file_json:
        json.dump(data, file_json)


@note.command()
@click.option("-n", '--name', prompt='Note name', help='Name of note')
@click.option("-nt", '--note', prompt='Note', help='Note text')
@click.option("-r", '--reminder', prompt='reminder_day', help='date',
              default=f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}")
def create(name, note, reminder):
    """create new note"""
    data = get_data()

    if len(reminder.split(" ")) != 2:
        click.echo(f"Reminder format is incorrect! Example: 10.03.2022 14:02", err=True)
        return
    date, time = reminder.split(" ")

    if len(date.split(".")) != 3:
        click.echo(f"Reminder format is incorrect! Example: 10.03.2022 14:02", err=True)
        return
    date = date.split(".")

    if len(time.split(":")) != 2:
        click.echo(f"Reminder format is incorrect! Example: 10.03.2022 14:02", err=True)
        return
    time = time.split(":")
    data[name] = {
        "name": name,
        "note": note,
        "reminder_date": datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]), hour=int(time[0]),
                                  minute=int(time[1])).timestamp()
    }
    set_data(data)


@note.command()
def list():
    """output of all notes"""
    data = get_data()
    head = ["day", "time", "note"]
    c = []
    for note_data in data.values():
        c.append([
            datetime.fromtimestamp(note_data["reminder_date"]).strftime("%d %B %Y"),
            datetime.fromtimestamp(note_data["reminder_date"]).strftime("%H:%M"),
            note_data["note"]
        ])
    table = pd.DataFrame(np.array(c), columns=head)
    print(table)


@note.command()
@click.argument("name")
def get(name):
    """search for a note by its name"""
    data = get_data()
    print(data[name]["note"], "\n", datetime.fromtimestamp(data[name]["reminder_date"]).strftime("%d.%B.%Y %H:%M"))


@calendar.command()
def today():
    """displays the note made today"""
    data = get_data()
    today_date = datetime.today()

    flag_ = False
    for item in data.values():
        reminder = datetime.fromtimestamp(item["reminder_date"])
        if today_date.day == reminder.day and today_date.month == reminder.month and today_date.year == reminder.year:
            print(item["note"], "\n", reminder.time())
            flag_ = True

    if not flag_:
        print("нет заметок на сегодня")


@calendar.command()
def week():
    """displays a note made during the week"""
    global now
    data = get_data()
    start_date = datetime.strptime(f'{now.year} {now.timetuple().tm_yday - now.weekday()}', '%Y %j')
    end_date = datetime.strptime(f'{now.year} {now.timetuple().tm_yday + (6 - now.weekday())}', '%Y %j')

    flag_ = False
    for item in data.values():
        reminder = datetime.fromtimestamp(item["reminder_date"])
        if start_date <= reminder <= end_date:
            print(item["note"], "\n", reminder.date(), reminder.time())
            flag_ = True

    if not flag_:
        print("нет заметок, сделанных этой на недели")


if __name__ == '__main__':
    cli()
