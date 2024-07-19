import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pivottablejs import pivot_ui

#schedule is a list of planned transfers

#sequence is start date	amount	recurrence	account	merchant 	category	events

schedule = [
    {"date":"5/26/2024", "amount":2906.51, "recurrence":"14D", "account":"3Rivers Savings", "merchant":"RRC", "category":"income", "num":26},
    {"date":"6/1/2024", "amount":-100, "recurrence":"M", "account":"3Rivers Savings", "merchant":"Electric", "category":"utilities", "num":12},
    {"date":"6/1/2024", "amount":-130, "recurrence":"7D", "account":"3Rivers Savings", "merchant":"King Soopers", "category":"food", "num":52},
    {"date":"6/1/2024", "amount":-45, "recurrence":"7D", "account":"3Rivers Savings", "merchant":"Gas", "category":"gas", "num":52},
    {"date":"6/1/2024", "amount":-1100, "recurrence":"M", "account":"3Rivers Savings", "merchant":"Venmo", "category":"rent", "num":12},
    {"date":"6/1/2024", "amount":-629.74, "recurrence":"M", "account":"3Rivers Savings", "merchant":"church", "category":"tithe", "num":12},
    {"date":"7/8/2024", "amount":-950, "recurrence":"6M", "account":"3Rivers Savings", "merchant":"Geico", "category":"car insurance", "num":2},
    #{"date":"1/6/2024", "amount":-130, "recurrence":"7D", "account":"3Rivers Savings", "merchant":"King Soopers", "category":"food", "num":52},
    #{"date":"1/6/2024", "amount":-130, "recurrence":"7D", "account":"3Rivers Savings", "merchant":"King Soopers", "category":"food", "num":52},
    #{"date":"1/6/2024", "amount":-130, "recurrence":"7D", "account":"3Rivers Savings", "merchant":"King Soopers", "category":"food", "num":52}
    #{} #etc.
]

schedule = pd.DataFrame(schedule)

#TODO add one off charges, that you know are going to happen
#TODO insert all missing days with zero charges when plotting
#TODO add option for gradually spent budget category

#TODO add logic for transfers and mechanics of multiple accounts

s = schedule
s['date']=pd.to_datetime(s['date'])
s=s.set_index('date')

print(s)

s["date_range"] = s.apply(lambda x: pd.date_range(x.name, periods=x.num, freq=x.recurrence), axis=1)
s = s.explode("date_range").reset_index(drop=True)
s=s.drop("num", axis=1)
s=s.drop("recurrence", axis=1)
#s=s[["date_range", "amount", "account", "merchant"]]
s=s.set_index("date_range")
s.index.names=["date"]
s=s.sort_index()
print(s)

#dtale.show(s, subprocess=False)
pivot_ui(s)


starting_amt=11000

ts = pd.Series(s["amount"], index=s.index)
ts = ts.cumsum()+starting_amt
ts.plot()
plt.show()

#events = np.array([])
#
#for i in schedule:
#    #generate N events
#    dates = pd.date_range(i.date, periods=i.count, freq="14D")
#    events = pd.DataFrame(i.amount, index=dates, columns="Amount", )