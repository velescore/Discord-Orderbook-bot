# Request for improvement

Add a market depth chart

See #otc-trades , type !market  there.  
I'd want to display the order book as an horizontal (or vertical) bar chart like

https://cdn.discordapp.com/attachments/397422988779061248/537569453064323073/figure_barchar.png

with 2 colors for wtb/wts, cumulative amount in btc as x axis

I'd need the python snippet to build a pyplot chart image from that data and save it to disk.
You can use https://pythonspot.com/matplotlib-bar-chart/ as a reference for the plot, only needs a few lines of code really

something like this: https://hackernoon.com/depth-chart-and-its-significance-in-trading-bdbfbbd23d33?gi=31fccc615e7e


See files in this dir as a starting point:

- orderlist.txt is the current data from the bot
- STATICS.PY is the real current file with some constant definition  
These 2 you don't have to touch
- order.py is the part that reads the orderlist.txt, and prints out the discord orderbook answer.  
You can tweak this one to save the plot instead.
