def build_major_scale(major_scale_name):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    mj_pattern = [0, 2, 4, 5, 7, 9, 11]

    # zero_position = notes.index(major_scale_name)
    # res = []
    # for i in mj_pattern:
    #     pos = (zero_position + i) % len(notes)
    #     res += [notes[pos]]
    # this block can be expressed as a comprehension

    return [notes[(notes.index(major_scale_name) + i) % len(notes)] for i in mj_pattern]


def note(major_scale_name, solfeage_name):
    solfege = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
    mj = build_major_scale(major_scale_name)
    return mj[solfege.index(solfeage_name)]
