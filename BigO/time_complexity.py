import datetime

nemo = ['nemo'] * 10000
boxes = [1,2,3,4,5] * 100

def findNemo(array):
    for elelment in array:
        if elelment == 'nemo':
            print('Found Nemo!')
            break


def logFirsrTwoBoxes(boxes):
    print(boxes[0])
    print(boxes[1])

def logAllPairs(boxes):
    for i in boxes:
        for j in boxes:
            print("{}{}".format(i,j))

start_time = datetime.datetime.now()
# findNemo(nemo) # O(n) ---> Linear Time
# logFirsrTwoBoxes(boxes) # O(1) ---> Constant Time
logAllPairs(boxes) # O(n^2) ---> Quadratic Time
process_time = datetime.datetime.now() - start_time
print("--- %s seconds ---" % (process_time.seconds))