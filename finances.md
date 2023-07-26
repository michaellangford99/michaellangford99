---
layout: default
title: Python Finance Tool
description:
top_bar: This was going to be the nav bar but now I might get rid of this lol.
left_sidebar: I haven't written hardly any code yet
right_sidebar: and what I have written is truly awful
---
# {{ title }}

Thoughts.

Each transaction will get categorized by me to say what it is - and that should probably be the same tag to determine what budget it falls into

transactions contain the account they credit, and the one they debit.

I don't know whether to create accounts for every tom dick and harry that has a purchase, or just lump everyone who isn't an account I own together as 'expenses'

need support for interest on loans

need support for credit card interest starting

when a transaction counts against 2 accounts I own, it's a transaction.

Example:

    I transfer 1000 to my chase account from my debit card
    1000 dollars is then credited to my chase account against my outstanding debt
    But I own the chase account so my net worth is the same until I get payed lol

```
    because before paying debt:

    debit card: 5,000
    chase acct: -24,000
    ----------------------
    sum:        -19,000

    after:
    debit card: 4,000
    chase acct: -23,000
    ----------------------
    sum:        -19,000
```

I do think it makes sense to be able to track how much I have been credited or debited by various places

So like for pay at work, it'd be nice to not just look at all credits that categorize as 'pay' but also look at OK
how much did Rincon pay me and see it as an account not owned by me that is being debited from itself and crediting to me.
In which case its balance is how much they've given me total.

I think an account should contain it's entire history and as such should not be a time snapshot.
However I don't know what the best wat to represent the present status is.
Indexing into a time series? Not sure. I don't want to have to recompute from the transaction set every time.

How should I handle stuff like taxes?

Anyways here's the object structure I have in mind (for tracking - will need another to handle budgeting, and another to merge the two cohesively):

---

transaction:
- amount //must be positive
- credit account
- debit account
- category
- date

account:
- balance (could be a computed time series)
- transactions
- additional properties such as APR, etc.

person:
- accounts
- balance (another time series)

---

Thus for me (a `person`), I can have a list of accounts I own. This would easily support transactions between my own accounts without modifying my worth.

Now how to support budgets?
I feel there is a difference between budgeting a certain amount to be used over a timeframe, and recurring payments.
I do like how pocketsmith tracks how much you spent of a given budget area with respect to how far you are through the time period that amount is allotted for.
I guess each 


On the topic of finances:

There comes a time in life when men observe that:
$$
women = time \cdot money
$$
however we all know that:
$$time = money$$
and of course:
$$money = \sqrt{all\space evil}$$
Which gives:
$$
women = money \cdot money
$$
$$
women = money^2
$$
$$
women = (\sqrt{all\space evil})^2
$$
$$
women = all\space evil
$$

That is of course a joke.

(Hi mom).


Test of embedded diagram:

(it worked but I don't want to include it because its hideous)

I think the first step is to implement a nice clean budgeting system.
Then I can define an input interface to it so I can modify the budget and get forecasts.
Next the input interface for giving updating it with transaction information. This would be very stripped data, just straight up debiting and crediting the budget accouts.
For example I have a food budget - passing it in a list of raw transactions where all it takes is the amount and the date. So then it can compute a time series of my consumption of the allocated budget over time.
