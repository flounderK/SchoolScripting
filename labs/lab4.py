from string import ascii_lowercase
import datetime
import time
import re
import random
#from time import localtime, strftime
#print("Please input your birthday (MM-DD-YYYY)")
#birthday=input()
#birthday=datetime.datetime.strptime(birthday, '%m-%d-%Y')

def analyze_word(word=None):
    v_rex=re.compile('[aeiou]')
    consonants=re.sub(v_rex,'',ascii_lowercase)
    c_rex=re.compile('['+consonants+']')
    if not word:
        print("Enter a word to analyze")
        word=input().lower()
    length_=len(word)
    consonants=len(re.findall(c_rex,word))
    vowels=len(re.findall(v_rex,word))
    print(("The word {:s} has: {:d} characters, "+
           "{:d} vowels, and {:d} consonants").format(
           word,
           length_,
           vowels,
           consonants))

def primes_less_than(number=None):
    def is_prime(number):
        for i in range(2,number):
            if not number % i:
                return False
        return True
    if not number:
        print("Enter a number to find the number of primes "+
              "less than the number")
        number=input()
    primes=list()
    for i in range(1, number):
        if is_prime(i):
            primes.append(i)
    print(("There are {:d} prime numbers between 0 and {:d}. ").format(
            len(primes),
            number))
    print(*primes, sep=", ")

def guess_the_number():
    guess=0
    number=random.randint(1,100)
    while guess != number:
        print("Guess the number! It is between 1 and 100.")
        guess=int(input())
        if guess > number:
            print("Too high")
        if guess < number:
            print("Too low")
    print("You guessed the number! it was {:d}".format(number))

analyze_word()
primes_less_than()
