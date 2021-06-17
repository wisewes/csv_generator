# writer.py
import csv
from random import choice, randint
from string import ascii_lowercase, digits
from datetime import datetime

def generateString(min=4, max=30):
  letters = ascii_lowercase
  letters_arr = list(letters)
  return ''.join(choice(letters_arr) for letter in range(randint(min, max)))

def generateNumber(min=1, max=10):
  numbers = digits
  numbers_arr = list(numbers)
  return ''.join(choice(numbers_arr) for num in range(randint(min, max)))

def generateEmail(min=3, max=10):
  recipient = generateString(min, max)
  return f"{recipient}@someplace.com"

def generateAddress(min=3, max=3):
  street_number = generateNumber(min, max)
  street_name = generateString(5, 10)
  street_label = generateString(2, 2)
  return f"{street_number} {street_name} ${street_label}."

def generateCSVFile():
  fields = ['firstname', 'lastname', 'email1', 'address1', 'city1', 'state1', 'zip1', 'notes'];
  rows = []

  for row in range(1000):
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

  filename = f"output_{datetime.now().strftime('%Y-%m-%d-%H:%M')}.csv";

  with open(filename, 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(fields)
    writer.writerows(rows)

generateCSVFile()
