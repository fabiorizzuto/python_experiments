# https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts/
from random import randint
import re


def get_lines_in_beat_range(_table, measure, position):
    beat_low = measure * 3
    beat_hi = (measure + 1) * 3
    _lines = []
    for element in _table:
        if beat_hi >= element[1] >= beat_low:
            beat_offset = element[1] - beat_low
            actual_beat = position * 3 + beat_offset
            _lines += [element[0] + ' ' + str(actual_beat) + ' ' + element[2]]
    return _lines


def parse_table(text):
    _table = []
    for line in re.finditer(re.compile('([^\n]+)\n'), text):
        founds = re.split('\s', line.group(1))
        if len(founds) != 3:
            raise Exception('Three elements expected')

        _table += [
            [
                founds[0],
                float(founds[1]),
                founds[2]
            ]
        ]
    return _table


class SelectionBuilder:
    @staticmethod
    def get_selection(_lines):
        # building table
        _table = SelectionBuilder._build_selection_table(_lines)
        # getting selection
        selection = [int(row[SelectionBuilder._roll_dices() - 2]) for row in _table]
        return selection

    @staticmethod
    def _roll_dices():
        return randint(1, 6) + randint(1, 6)

    @staticmethod
    def _build_selection_table(_lines):
        # loading selection table using regexp
        _table = []
        for line in _lines:
            _table += [re.findall(re.compile('[0-9]+'), line)]
        return _table


# reads lines from selection_table file, then builds selection
text_file = open("selection_table.txt", "r")
measure_selection = SelectionBuilder.get_selection(text_file.readlines())
text_file.close()

# reads content from mozart-dice-starting file, then puts values in a table
text_file = open("mozart-dice-starting.txt", "r")
table = parse_table(text_file.read())
text_file.close()

# prints melody
for i in range(len(measure_selection)):
    lines = get_lines_in_beat_range(table, measure_selection[i], i)
    print('\n'.join(lines))
