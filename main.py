from DTW import calcDTW
from datetime import datetime

if __name__=="__main__":
    start = datetime.now()
    dtwVector = calcDTW("0.wav")
    print("DONE in: {0}".format(datetime.now()-start))