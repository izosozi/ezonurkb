import shutil
from itertools import zip_longest
import sys
import random
import math
import argparse

character_groups = {
    "alphabet": list('abcdefghijklmnopqrstuvwxyz'),
    "qwertyLeft": list('qwertasdfgzxcvb'),
    "qwertyRight": list('yuiophjklnm'),
    "qwertyRightOuter": list('uiopjklm'),
    "qwertyLeftOuter": list('qweasdzxc'),
    "qwertyRightInner": list('yuihjknm'),
    "qwertyLeftInner": list('ertdfgcvb'),
    "numbers": list('0123456789'),
    "vowels": list('aeiouy'),
    "qwertyLeftVowels": list('ae'),
    "qwertyRightVowels": list('iouy'),
    "qwertyLeftTopTwo": list('qwertasdfg'),
    "qwertyRightTopTwo": list('yuiophjkl'),
    "qwertyLeftBottomTwo": list('asdfgzxcv'),
    "qwertyRightBottomTwo": list('hjklnmb'),
}

commands = {
    'interleave': lambda: outputGrid(reps, lambda: randInterleave(primaryChars, secondaryChars, vowelMult, outputStrLen)), 
    'palindrome': lambda: outputGrid(reps, lambda: createPalindrome(primaryChars, secondaryChars, vowelMult, outputStrLen))
}

parser = argparse.ArgumentParser(description='Generate a list of easily typable randomized strings')
parser.add_argument('-t', '--type', type=str, help='Type of string to generate', default='interleave', choices=commands.keys())
parser.add_argument('-r', '--repetitions', type=int, default=1, help='Number of repetitions')
parser.add_argument('-l', '--length', type=int, default=7, help='Length of palindrome')
parser.add_argument('-p', '--primary', nargs='+', default=[], help='Primary chars separated by spaces')
parser.add_argument('-P', '--primary-preset', type=str, help='Primary preset')
parser.add_argument('-s', '--secondary', nargs='+', default=[], help='Secondary chars separated by spaces')
parser.add_argument('-S', '--secondary-preset', type=str, help='Secondary preset')
parser.add_argument('-v', '--vowelmult', type=float, help='Change likelihood of vowels', default=1.0)

args = parser.parse_args()

reps = args.repetitions

if reps > 10000:
    inp = input(f'You asked for {reps} repetitions. Are you sure? [y/n]')
    if inp != 'y':
        exit()
elif reps < 1:
    print('Number of repetitions must be at least 1')
    exit()

outputStrLen = args.length

if outputStrLen > 1000:
    inp = input(f'You asked for length {outputStrLen}. Are you sure?')
    if inp != 'y':
        exit()

vowelMult = args.vowelmult

if vowelMult < 0:
    print('Vowel multiplier must be at least 0')
    exit()

primaryChars = set(letter.strip() for letter in args.primary) if args.primary else set()
primaryChars |= set(character_groups[args.primary_preset]) if args.primary_preset else primaryChars

secondaryChars = set(letter.strip() for letter in args.secondary) if args.secondary else set()
secondaryChars |= set(character_groups[args.secondary_preset]) if args.secondary_preset else secondaryChars

primaryChars = list(primaryChars)
secondaryChars = list(secondaryChars)

if len(primaryChars) == 0 and len(secondaryChars) == 0:
    primaryChars = character_groups['qwertyLeft']
    secondaryChars = character_groups['qwertyRight']

if len(primaryChars) == 0 or len(secondaryChars) == 0:
    print('One character set is empty, using the provided set for all characters')
    primaryChars, secondaryChars = secondaryChars + primaryChars

if outputStrLen < 1:
    print('palindrome length must be at least 1')
    exit()


def makeWeights(letters: list, vowelMultiplier: float) -> list:
    return [weight * vowelMultiplier if letter in character_groups['vowels'] else weight for weight, letter in zip([1] * len(letters), letters)]


def randInterleave(letters1: list, letters2: list, vowelMult: float, length: int) -> list:
    weights1 = makeWeights(letters1, vowelMult)
    choices1 = random.choices(letters1, weights=weights1, k=math.ceil(length / 2))

    weights2 = makeWeights(letters2, vowelMult)
    choices2 = random.choices(letters2, weights=weights2, k=math.floor(length / 2))

    interleaved = [item for pair in zip_longest(choices1, choices2, fillvalue='') for item in pair]

    return ' '.join(interleaved).split()


def createPalindrome(letters1: list, letters2: list, vowelMult: float, length: int) -> list:
    segmentLength = math.ceil(length / 2)
    interleaved = randInterleave(letters1, letters2, vowelMult, segmentLength)
    palin = interleaved + interleaved[-2 if outputStrLen % 2 == 1 else -1::-1]
    return ' '.join(palin).split()


def accumulateOut(reps: int, command: callable) -> list:
    output = []
    for i in range(reps):
        output.append(command())
    return output


def outputGrid(reps: int, func: callable) -> None:
    output = accumulateOut(reps, func)

    console_width = shutil.get_terminal_size().columns
    max_width = max(len(item) for item in output) + 2
    num_columns = console_width // max_width

    for i, item in enumerate(output):
        if num_columns > 0:
            print(f"{''.join(item):<{max_width}}", end='')
            if (i + 1) % num_columns == 0:
                print()
        else:
            print(item)

    if (num_columns > 0 and len(output) % num_columns != 0) or num_columns == 0:
        print()


if __name__ == "__main__":
    commands[args.type]()