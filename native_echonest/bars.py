import sys, os


import echonest.audio as audio
import random


# Lib
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# /Lib

subject = audio.LocalAudioFile(sys.argv[1])

bars = subject.analysis.bars

slices = list(chunks(bars, 10))
new_slices = []

while slices:
    i = random.randint(0, len(slices))
    for j in slices.pop(i-1):
        new_slices.append(j)


audio.getpieces(subject, new_slices).encode("%s-improved.mp3" % os.path.basename(sys.argv[1][:-4]))
