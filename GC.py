# Compute the GC content in seqs (strings) given in FASTA format
# Print the string and GC content (%) of the string with the highest
# GC content of all stirngs provided
#
#         FASTA format:
#         * There are newlines within the strings
#         * '>' denotes the start of a new seq sequence. '>' is followed
#             directly by the label (ie., name of string), followed by a newline,
#             followed by the actual seq sequence

import re
import itertools

def make_seq_dict(filename):
    '''
    :param filename: name of text file of DAN sequences in FASTA format
    :return: A dictionary of with FASTA labels as keys and nucleotide sequences
        as the values.
    '''
    input = open(filename, 'r').read()

    input_cleaned = input.replace('\n', '')
    # Regex: "starts wth '>' followed by letters_numbers"
    seq_list = re.split(r'>([a-zA-Z]*_[\d]*)', input_cleaned)
    seq_list = list(filter(None, seq_list))

    seq_dict = dict(
        itertools.zip_longest(*[iter(seq_list)] * 2, fillvalue=''))

    return seq_dict


def gc_content(seq_dict):
    '''
    :param seq_dict: list of strings containing seqs. with FASTA labels
    :return:
        * dict containing GC content of each seq, with FASTA label as the key.
        * key for the entry with the highest gc content
    '''

    gc_dict = {}
    highest_gc_key, highest_gc = '', 0

    for key in seq_dict:
        gc_content_item = ((seq_dict[key].count('C')
                           + seq_dict[key].count('G'))
                           / len(seq_dict[key]) * 100)
        if gc_content_item > highest_gc:
            highest_gc = gc_content_item
            highest_gc_key = key

        gc ={key: gc_content_item}
        gc_dict.update(gc)

    return gc_dict, highest_gc_key

def print_highest_gc(filename):
    '''
    This function just wraps around all of the others written above so that I
    can get the output the the format prescribed by the challenge
    '''
    seq_dict = make_seq_dict(filename)
    gc_dict, highest_gc_key = gc_content(seq_dict)

    print(highest_gc_key)
    print(gc_dict[highest_gc_key])

if __name__ == '__main__':
    print_highest_gc('gc_input-train.txt')
    print_highest_gc('gc_input-test.txt')



###### Even simpler solution

# Elegant solution that effectively ignores newlines
# Since they don't contain ACTGs, they really don't affect the result...

# Does rely on the FASTA label not containing ACTG, however...


if __name__ == '__main__':
    s = open('gc_input-train.txt', 'r').read()
    seqs = s.split(">")[1:]
    gc = []

    for seq in seqs:
        a = seq.count("C") + seq.count("G")
        b = a + seq.count("A") + seq.count("T")
        gc.append(float(a)*100/b)

    print(seqs[gc.index(max(gc))].split('\n')[0])
    print(max(gc))