import sys
import traceback

import random
import sympy
import numpy
import scipy
from py_asciimath.translator.translator import ASCIIMath2Tex, Tex2ASCIIMath
from py_asciimath.grammar.asciimath_grammar import asciimath_grammar
genList = []


class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

        (filename, line_number, function_name,
         text) = traceback.extract_stack()[-2]
        funcname = filename[filename.rfind('/'):].strip()
        funcname = funcname[1:-3]
        subjectname = filename[:filename.rfind('/')].strip()
        subjectname = subjectname[subjectname.rfind('/'):].strip()
        subjectname = subjectname[1:]
        genList.append([id, title, self, funcname, subjectname])

    def __str__(self):
        return str(
            self.id
        ) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, format='raw', *args, **kwargs):
        return preprocess_set(format, self.func(*args, **kwargs))

        # This section only runs if the format key was not used

        # Detect and remove math indicator in problem and solution
        # return self.func(*args, **kwargs)


def getGenList():
    correctedList = genList[-1:] + genList[:-1]
    # Orders list by id
    correctedList.sort()
    return correctedList

def preprocess_set(format, set):
    if format == 'latex':
        #sentence.index('$$')
        # Find location of asciimath between $$ delimiters
        # Then replace current asciimath with tex
        asciimath2tex = ASCIIMath2Tex(asciimath_grammar)
        problem = asciimath2tex.translate(set[0])
        solution = asciimath2tex.translate(set[1])
        problem = '$' + problem + '$'
        solution = '$' + solution + '$'
        return problem, solution
    elif format == 'asciimath':
        return set
    elif format == 'raw':
        problem = set[0].replace('$$', '')
        solution = set[1].replace('$$', '')
        return problem, solution
