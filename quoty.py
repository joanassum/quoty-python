import click
import csv
import random
import os

@click.group()
def quoty():
    """A CLI wrapper for storing quotes."""

storage_path = os.environ['QUOTY_PATH'] + '/quotes.csv'
#storage_path = 'quotes.csv'

@quoty.command()
@click.argument('quote', type=click.STRING)
@click.option('-t', '--tags')
def add(quote, tags):
    """Add a quote."""
    # Create csv file for storage if not exist
    open(storage_path, "a")

    if ',' in quote:
        print("Symbol , is not allowed in quote")
        return

    # Read the csv file to check if the quote already exist.
    with open(storage_path, 'r') as csvfile:
        for line in csvfile:
            if quote == line.split(",")[0]:
                print("Quote already exist")
                return


    print("Adding Quote: " + quote)
    if tags:
        tags = tags.split(",")
        tags = ":".join(tags)
        print("With tags: " + str(tags))
    else:
        tags = []
    # Add the quote
    with open(storage_path, 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([quote, str(tags)])
        print("Quote added")

@quoty.command()
@click.option('-t', '--tag', type=click.STRING)
def inspireme(tag):
    """Get a random quote."""
    with open(storage_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        if tag != None:
            filtered = list(filter(lambda x: tag in list(x[-1].split(":")), list(reader)))
            chosen_row = random.choice(filtered)
        else:
            chosen_row = random.choice(list(reader))
        print(chosen_row[0])

if __name__ == '__main__':
    quoty(prog_name='quoty')