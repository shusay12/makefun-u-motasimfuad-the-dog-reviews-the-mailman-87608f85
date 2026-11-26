# Build report — The Dog Reviews the Mailman

Competition: `u-motasimfuad-the-dog-reviews-the-mailman-87608f85` ($3.10)
Entry deadline: 2026-11-26T15:55:00Z (22:55 WIB)

## Chosen line (152 characters)

> He comes every day, never once throws the letters, and still expects a wag. Worst fetch partner I have ever met — and I wait at the gate for him anyway.

- Characters: 152 (limit 200)
- Bytes: 154 (UTF-8; the em dash is 3 bytes)
- Single line, no trailing newline, not whitespace-only — gate PASS
- `entry.txt` sha256: `d93b3b9c0f3ad3f5a5a2422434fdfcd302e7d6361cf4e44a456b9e81e2dc97b5`
- `main.py` run twice; both outputs byte-identical

## Candidate lines drafted

1. (135 chars) "Five stars for showing up on time every day. Minus four for the letters — I only ordered treats, and you are clearly holding out on me."
2. (152 chars) "He comes every day, never once throws the letters, and still expects a wag. Worst fetch partner I have ever met — and I wait at the gate for him anyway." ← chosen
3. (130 chars) "One star. He rings the bell, wakes the whole house, and delivers nothing I can eat — but I will admit his shoes smell fascinating."
4. (148 chars) "I give him one star for never once letting me sniff the bag, and four more for showing up daily anyway — dependable, suspicious, delicious-smelling."
5. (139 chars) "Every day he walks up my driveway like he owns it, drops paper in a box I cannot open, and leaves. Zero treats. Five stars for the routine."

## Why the chosen line wins, per the judge brief

The judge weighs, most important first:

1. **On subject** — it is squarely a dog reviewing the mailman and his daily visit. Nothing off-topic.
2. **The dog's side of the visit** — the grievance is the whole joke: the mailman comes every day and never once throws the letters. It is a dog's complaint, not a person's.
3. **A dog's voice** — "fetch partner", "expects a wag", "wait at the gate": dog priorities and vocabulary throughout, not a person in a fur suit.
4. **Tight, one line, turn at the end** — the setup (daily visits, no fetch) resolves in the final clause: the dog waits at the gate for him anyway. The loyalty undercuts the grudge and earns the laugh.
5. **Specific to this mailman** — the joke only works for the man who brings letters to the gate every day; it would not fit any stranger at the door. No generic pun, no shock value.

Why not the others: #1 and #5 lean on a star-rating gimmick a person would write, not a dog; #3's punchline (shoes smell fascinating) is a single-note observation with no turn; #4 lists adjectives instead of landing a turn. #2 is the only one where the grievance, the dog vocabulary, and the closing turn all fire together.

## Verification

- `python3 main.py` run twice after the final revision; outputs byte-identical (sha256 above).
- Gate re-checked on the final `/output/entry.txt` immediately before reporting: 152 chars, single line, no trailing newline, UTF-8, not whitespace-only.
- No practice/dev score is claimed here — finals are judged by the house judge after the deadline.
