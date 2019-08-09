# TwitterStats
Twitter script in Python that creates a graph of how many tweets you have per hour.

To run:
> python tweepy_tool.py username 

I got an error (apparently my ISP is blocking certain connections including this one) while running 'pip install tweepy' so I ran the following and it worked:
> sudo sh -c 'echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6'

Install libraries:
> apt-get install python-tk
> pip install matplotlib
