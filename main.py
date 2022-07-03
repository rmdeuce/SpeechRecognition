from DTW import calcDTW
from datetime import datetime

if __name__=="__main__":
    start = datetime.now()
    dtwVector = calcDTW("happy_max.wav")
    print("DONE in: {0} result: {1}".format(datetime.now()-start, dtwVector[1]))
