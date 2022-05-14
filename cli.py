import json
from os import path
import click
from datetime import datetime
from datetime import date

file_name = 'notes.json'

now = datetime.now()


@click.group()
def cli():
    pass


@cli.group()
def note():
    pass


@cli.group()
def calendar():
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
@click.argument("name")
def get(name):
    data = get_data()
    print(data[name]["note"], "\n", data[name]["reminder_date"])


@calendar.command()
def today():
    global file_name
    data = get_data()
    today_date = datetime.today()

    for item in data.values():
        reminder = datetime.fromtimestamp(item["reminder_date"])
        if today_date.day == reminder.day and today_date.month == reminder.month and today_date.year == reminder.year:
            print(item["note"], "\n", reminder.time())


@calendar.command()
def week():
    global file_name, now
    data = get_data()
    start_date = datetime.strptime(f'{now.year} {now.timetuple().tm_yday - now.weekday()}', '%Y %j')
    end_date = datetime.strptime(f'{now.year} {now.timetuple().tm_yday + (6 - now.weekday())}', '%Y %j')

    print(start_date, end_date)
    for item in data.values():
        reminder = datetime.fromtimestamp(item["reminder_date"])
        if start_date <= reminder <= end_date:
            print(item["note"], "\n", reminder.date(), reminder.time())


if __name__ == '__main__':
    cli()
