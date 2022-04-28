
PosInList = 0

def shortBubbleSort(unordered_list):
    LengthOfList = len(unordered_list)
    for bubbleSort in range(LengthOfList):
        for PosInList in range(LengthOfList - 1):
            if unordered_list[PosInList] > unordered_list[PosInList + 1]:
                temp = unordered_list[PosInList]
                unordered_list[PosInList] = unordered_list[PosInList + 1]
                unordered_list[PosInList + 1] = temp
            
            
unordered_list = [200, 20, 30, 5, 40, 90, 50, 60, 70, 80, 100 ,110 ,101]
shortBubbleSort(unordered_list)
print(unordered_list)

