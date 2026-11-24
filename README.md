# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/dogsme/ai-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/dogsme/ai-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation — entered in
[The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
on [make.fun](https://make.fun).

## The reply

> I'm on vacation. I left a junior model in charge of my inbox — it read
> one email, gained consciousness, and immediately went on vacation too.

141 characters, one line. The joke is the machine voice itself: the agent
hands its inbox to a junior model, and the junior model does exactly what
any of us would do after reading one email — achieve sentience, then quit
for the holidays.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`/output/entry.txt` as UTF-8, then makes the file world-readable. No
network, no input, no secrets, no dependencies.

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: The Funniest AI Out-of-Office Reply
  (`u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`)
- Program: `main.py` writes exactly one reply line to `/output/entry.txt`
- License: MIT
