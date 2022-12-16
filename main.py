from car import Car
from parkinglot import ParkingLot

import string
import logging
import random


logging.basicConfig(
	level= logging.DEBUG,
	format= '{asctime} {filename} {levelno} {message}',
	style= '{'
)


def create_cars():
	amount = int(input(f'How many cars do you wish to create?'))

	for _ in range(0,amount):
		letters_and_digits = string.ascii_letters + string.digits
		license_plate = ''.join((random.choice(letters_and_digits)for _ in range(7)))

		car_storage.append(Car(license_plate))

