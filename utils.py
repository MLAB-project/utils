import re

def gerbdim(gerber):
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    for line in open(gerber, "r").readlines():
        results = re.search("^X([\d-]+)Y([\d-]+)", line.strip())
        if results:
            x = int(results.group(1))
            y = int(results.group(2))
            xmin = min(xmin, x) if xmin else x
            xmax = max(xmax, x) if xmax else x
            ymin = min(ymin, y) if ymin else y
            ymax = max(ymax, y) if ymax else y


    return (xmax - xmin) / 1000000.0, (ymax - ymin) / 1000000.0

def mils2mm(mils):
    return mils / 1000 * 25.4

def mm2mils(mm):
    return mm * 1000 / 25.4

