import echonest.audio as audio
import random


# Lib
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# /Lib

subject = audio.LocalAudioFile("cloak-and-dagger-2.mp3")

beats = subject.analysis.beats

slices = list(chunks(beats, 10))
new_slices = []

while slices:
    i = random.randint(0, len(slices))
    for j in slices.pop(i-1):
        new_slices.append(j)


audio.getpieces(subject, new_slices).encode("SweetSweetHax.mp3")


