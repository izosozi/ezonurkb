# ezonurkb
>*"easy on your keyboard"*

ezonurkb is a straightforward, cut-and-dry, pleasant-on-the-eyes script that outputs a bunch of randomized, customizable strings that are easy to type quickly, especially on mobile screens.

This can be useful for generating names that don't need to have any denotative meaning, but will be inputted on a keyboard often. For example:

- Hard drives and other devices

- Usernames

- Domains

- Prototypes

- Codewords

- Aliases & pseudonyms

- Fictional characters

- Magical spells

- Newly discovered species of mushroom

- Inventing slurs

If you know what you're doing, you could potentially use this for UUIDs, cryptographic keys, or passwords, but even then you probably shouldn't.

## Features

- Select primary and secondary character sets to alternate between

- Custom lengths

- Vowel multiplier to make outputs more (or less) pronounceable

- Palindrome mode!

## Usage

```bash

python ezonurkb.py [-h] [-t {interleave,palindrome}] [-r REPETITIONS] [-l LENGTH] [-p PRIMARY [PRIMARY ...]] [-P PRIMARY_PRESET] [-s SECONDARY [SECONDARY ...]] [-S SECONDARY_PRESET] [-v VOWELMULT]

```

## Options

| Flag                   | Description                   | Default      | Options                    | Type   |
| ---------------------- | ----------------------------- | ------------ | -------------------------- | ------ |
| `-h, --help`           | Show help message and exit    |              |                            |        |
| `-t, --type`           | Type of string to generate    | "interleave" | "interleave", "palindrome" | string |
| -r, --repetitions      | Number of strings to generate | 1            | x>0                        | int    |
| -l, --length           | Length of each string         | 7            | x>0                        | int    |
| -p, --primary          | Primary characters            | null         | Space separated characters | list   |
| -s, --secondary        | Secondary characters          | ^            | ^                          | ^      |
| -P, --primary-preset   | Primary preset                | null         | See [[#Character sets]]    | str    |
| -S, --secondary-preset | Secondary preset              | ^            | ^                          | ^      |
| -v, --vowelmult        | Change likelihood of vowels   | 1            | x>=0                       | float  |

## Character sets

If no characters or presets are specified, the primary set and secondary set are filled by qwertyLeft and qwertyRight.

If you pick both a preset and individual characters, the characters from both will be combined in a set.

> e.g., `--primary d r f --primary-preset qwertyLeftVowels` will result in the primary set being `aedrf`

```py

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

```

Feel free to modify and make PRs.

## Examples

An interleaved string from default settings (1 string 7 chars long interleaved between qwertyLeft and qwertyRight)

```bash

> python ezonurkb.py

tuxhxkr

```

---

A palindrome string with default settings

```bash

> python ezonurkb.py -t palindrome

gocjcog

```

---

15 interleaved strings of length 5.

```bash

> python ezonurkb.py -r 15 -l 5

qnekr blclt ghfyc fogjv wkxyc tiwmf cnbjf qpriw titkq ekryz fpdhe xovms sixhc

xlspf fuahw

```

> If you want nice sounding strings, you'll need to read through a lot of outputs, so set -r somewhere in the 100-1000 range and get comfy---

10 interleaved strings which alternate between primary set qwertyRightVowels + l + m, and secondary set qwertyLeft

```bash

> python ezonurkb.py -r 10 -p l m -P qwertyRightVowels -S qwertyLeft

oquqmdm iayqyem ieizmfy ozmqoem ybiwuvo ysmflei ixytyxi oxmdiey yzmwltu msituey

```

---

Same as above, but with vowel multiplier of 2.8

```bash

> python ezonurkb.py -r 10 -p l m -P qwertyRightVowels -S qwertyLeft -v 2.8

idydiqi uzueywi ueyeyey ovywuvi ltuayfy owlvybu ycidiei ycuvovo uvuqyao uaoaigl

```

## Building

Too lazy to make binaries yet but I recommend [pyinstaller](https://pyinstaller.org/)