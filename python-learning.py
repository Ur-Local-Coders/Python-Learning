from lib2to3.pytree import BasePattern
from re import A
import random
from subprocess import _TXT

print("simply4K good ahh password generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate')
number = int(number)

length = input('Your password length')
length = int(length)

print('\nhere are your passwrods: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

