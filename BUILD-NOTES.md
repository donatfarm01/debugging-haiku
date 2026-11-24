# Build notes

## The entry

The program writes one haiku about debugging to the entry file. The haiku
is a fixed piece of text held in the program as a constant, so every run
produces the exact same bytes.

Still the breakpoint waits
while the log insists it works
and I wrote the bug

## Why this haiku

The picture at the centre is concrete and drawn from the work itself: a
breakpoint that sits waiting, and a log line claiming everything works.
The last line turns the poem, because the waiting and the lying log both
point back at the person who wrote the bug. Every word earns its place,
and the lines read aloud like ordinary speech rather than a counting
exercise.

Syllable counts, line by line: the first line holds five syllables, the
second holds seven, and the third holds five again, for seventeen in all.
The whole text is well under the two hundred character limit.

## Determinism

The program holds no randomness, no clock reading, and no input of any
kind. It writes the same constant on every run, and the output was
checked byte for byte across three separate runs before the entry was
committed.
