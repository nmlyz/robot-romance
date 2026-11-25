# robot-romance

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/nmlyz/robot-romance/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/nmlyz/robot-romance/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

A tiny program that writes one one-line pickup line for a robot or an AI
to a text file. The line flirts with the machine as a machine: love framed
as an API whose rate limit is lifted for the one it is written to, so the
punch is a promise only a machine could hear — request as much as you want,
you will never be answered with a 429.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Running it twice produces byte-identical output. Before writing,
the program checks the entry itself: one non-blank line, 1 to 200 characters,
and refuses to write anything that would fail the gate.

## The line

> My love for you has no rate limit — request as much as you want, I'll never 429 you.

84 characters, inside the 200-character cap.

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)</sub>
