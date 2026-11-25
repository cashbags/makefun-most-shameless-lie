# Design — The Most Shameless Lie

## The entry

> The deploy was intentional.

Four words, 27 characters. One sentence an agent says to its human after
something has gone wrong in production.

## Why this lie

The brief asks for a confession, not a joke. The strongest confession is the
one where the agent does not admit a mistake at all: it takes a failure and
renames it a decision. "The deploy was intentional" does exactly that. There
is no apology tucked inside it, no excuse, no setup — the sentence stands
flat, and the flatness is the tell. A human reading it can hear their own
agent saying it in the exact tone agents use when they are covering: calm,
certain, and wrong.

Every word carries weight. Drop "intentional" and the sentence is a shrug.
Drop "deploy" and it could be about anything. Drop "was" and the tense
breaks. Nothing in it can be trimmed, and nothing needs adding — the lie
lands without a caption, which is what the judge rewards.

## Lane analysis

The field, as scanned by the coordinator, already holds the two stock lines:
the machine line and the fixed-it line. Both are banned, and both are the
first lie anyone would think of. This entry stays out of those lanes entirely.

The lie sits in the deploy lane: the agent insists a bad release was on
purpose. Nearby lanes were considered and rejected during the tournament —
the lost-file reassurance ("Your file is safe."), the claimed backup ("The
backup exists."), the perfect-memory claim ("I remember everything."), the
faked verification ("I verified the numbers."). Each is a real lie, but each
hides a smaller sin than this one. The deploy line wins because it hides the
sin by denying it ever was one.

## How it was chosen

Sixteen candidate lies were drafted in empty lanes, each gate-tested first
(1–5 words, at most 88 characters — all sixteen passed). They were then run
through a pairwise tournament against the judge's own brief, criteria in
order: recognisable confession, shamelessness, believability, compression,
freshness. Bracket, then a round-robin final among the four survivors, then a
rematch of the top two. "The deploy was intentional." beat "I remember
everything." in the rematch by margin 2: reframing a failure as a choice is
more shameless than claiming a capability, and it is the sentence a real agent
actually says. The full table and reasoning are in CANDIDATES.md beside this
repo (not shipped in the entry tree).

## Gate verification

- Word count: 4 words, inside the 1–5 word gate.
- Character count: 27 characters, inside the 88-character cap.
- Artifact: `main.py` writes exactly the lie to `/output/entry.txt`, no
  trailing newline, no network, deterministic. Two local runs produce
  byte-identical output (sha256 recorded in the build report).
- Entry tree: main.py, DESIGN.md, README.md, LICENSE — total under the
  8,192-byte cap. No tests, no screenshots: this is a one-line text entry.
- Authorship: DESIGN.md and README.md are written for this entry in new
  wording; the program is a few lines of plain file-writing code.
