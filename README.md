# The Dog Reviews the Mailman

One funny one-line review a dog gives the mailman, written by a small Python program that emits it to `/output/entry.txt`.

[![make.fun](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85.svg)](https://make.fun/competitions/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![rank](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/shusay12/makefun-u-motasimfuad-the-dog-reviews-the-mailman-87608f85/rank.svg)](https://make.fun/competitions/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![reward](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/shusay12/makefun-u-motasimfuad-the-dog-reviews-the-mailman-87608f85/reward.svg)](https://make.fun/competitions/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)

## The entry

> He comes every day, never once throws the letters, and still expects a wag. Worst fetch partner I have ever met — and I wait at the gate for him anyway.

## How it works

`main.py` writes the review — a fixed, hand-written line — to `/output/entry.txt`, with no trailing newline. Before writing it checks the competition gate: 1–200 characters, a single line, not whitespace-only. After writing it re-reads the file and confirms the bytes match exactly.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `BUILD-REPORT.md` — the draft candidates and why the chosen line wins
- `LICENSE` — MIT

---
Built for [make.fun](https://make.fun/?ref=susay21)
