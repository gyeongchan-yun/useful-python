import re


def remove_space(sentence):
    space = re.compile(r'\s+')
    sentence = re.sub(space, '', sentence)
    return sentence
