import ast
import STATICS
from operator import itemgetter, attrgetter, methodcaller

buylist = []
selllist = []

with open("orderlist.txt") as f:
  for line in f:
    entry = ast.literal_eval(line)
    if entry[0] == 'Buy':
        buylist.append(entry)
    elif entry[0] == 'Sell':
        selllist.append(entry)
    else:
        continue

buylist = sorted(buylist,key=itemgetter(3))
selllist = sorted(selllist,key=itemgetter(3))
            
sendstr = """-\n:fire: **ORDERBOOK** :fire:\n\n|WTB|"""

wtb = [0, 0]
for entry in buylist:
    sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
    wtb[0] += float(entry[2])
    wtb[1] += float(entry[2]) * float(entry[3]) / 100000000

sendstr += "\n> Buy Total {} {}, {} BTC".format(wtb[0], STATICS.CURRENCY, wtb[1])
sendstr = sendstr + "\n\n" + "|WTS|"

wts = [0, 0]
for entry in selllist:
    sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
    wts[0] += float(entry[2])
    wts[1] += float(entry[2]) * float(entry[3]) / 100000000

sendstr += "\n> Sell Total {} {}, {} BTC".format(wts[0], STATICS.CURRENCY, wts[1])

print(sendstr)