# writer.py
"""
Creates a CSV file for testing uploading of dummy data
"""

import csv
from random import choice, randint
from string import ascii_lowercase, digits
from datetime import datetime
import click

def generateString(min=4, max=30):
  """Create a random string"""
  letters = ascii_lowercase
  letters_arr = list(letters)
  return ''.join(choice(letters_arr) for letter in range(randint(min, max)))

def generateNumber(min=1, max=10):
  """Create a random number"""
  numbers = digits
  numbers_arr = list(numbers)
  return ''.join(choice(numbers_arr) for num in range(randint(min, max)))

def generateEmail(min=3, max=10):
  """Create a email string"""
  recipient = generateString(min, max)
  return f"{recipient}@someplace.com"

def generateAddress(min=3, max=3):
  """Create an address string"""
  street_number = generateNumber(min, max)
  street_name = generateString(5, 10)
  street_label = generateString(2, 2)
  return f"{street_number} {street_name} ${street_label}."

def generateCSVFile(filename, row_count):
  """Create a csv file"""
  fields = ['firstname', 'lastname', 'email1', 'address1', 'city1', 'state1', 'zip1', 'notes'];
  rows = []

  number_of_rows = row_count if row_count else 100 
  for row in range(number_of_rows):
    rows.append([
      generateString(),
      generateString(),
      generateEmail(),
      generateAddress(),
      generateString(),
      generateString(2, 2).upper(),
      generateNumber(5, 5),
      generateString().upper()
    ])

  if (filename):
    filename_str = filename
  else:
    filename_str = f"output_{datetime.now().strftime('%Y-%m-%d-%H:%M')}.csv";

  with open(filename_str, 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(fields)
    writer.writerows(rows)

# generateCSVFile(filename=None)

@click.command()
@click.option('--filename', type=click.STRING, prompt='Enter filename', help='The generated filename for csv file')
@click.option('--rows', type=click.INT, prompt='Enter number of rows', help='The number of rows to create')
# @click.option('--headers', help="List of header value comma separated, 'firstname', 'lastname', 'age'")
def main(filename, rows):
    """Creates a CSV file with randomly-generated values for testing and manipulation of test data. Essentially, a generate file as a fake data source."""
    generateCSVFile(filename, rows)

if __name__ == '__main__':
    main()