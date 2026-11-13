import random
import sys
import matplotlib.pyplot as plt

class Algo:
    def __init__(self,arr):
        self.arr = arr.copy()

    def print1(self):
        print(self.arr)
        
    def bubbleSort(self):
        arr = self.arr.copy()
        n = len(arr)
        megaArr = []
        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):

                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            megaArr.append(arr.copy())
            if (swapped == False):
                break
            
        return megaArr

    def insertionSort(self):
        arr = self.arr.copy()
        n = len(self.arr)
        megaArr = []
        i = j = 0
        while i<n:
            j = i
            while j>0 and arr[j-1]>arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j = j-1
                megaArr.append(arr.copy())
            i = i +1
        return megaArr
    
    def selectionSort(self):
        arr = self.arr.copy()
        n = len(arr)
        megaArr = []

        for i in range(n):
            minIndex = i

            for j in range(i+1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j

            arr[i], arr[minIndex] = arr[minIndex], arr[i]

            megaArr.append(arr.copy())

        return megaArr

    def linearSearch(self,what):
        arr = self.arr.copy()
        n = len(arr)
        x = 0
        for i in range(n):
            x = arr[i]
            if x == what:
                return i+1
            else:
                continue
        print("Please enter a valid input \n")
        return -1
    
    def binarySearch(self,x):
        arr = self.arr.copy()
        arr = sorted(self.arr)
        low = 0
        high = len(arr) -1
        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == x:
                return mid+1,arr
            elif arr[mid] < x:
                low = mid +1
            else:
               high = mid -1
        return -1,arr
    
def listmaker(length):
    i = 0
    list1 = []
    while i<length:
        n = random.randint(10,100)
        list1.append(n)
        i = i+1
    return list1

def visualizer(vari,name):
    
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(vari[0])), vari[0])

    ax.set_ylim(0, 110)

    for state in vari:
        for bar, height in zip(bars, state):
            bar.set_height(height)
        
        plt.title(name)
        plt.pause(0.5)

    plt.show()

def main():
    arr = listmaker(10)
    arr2 = Algo(arr)
    print("\nWelcome to the Algorithm Visualizer\n")
    inp1 = input("Press 1 for sorting algorithms, Press 2 for searching algorithms, Press 3 to exit. \n >")
    inp1 = int(inp1)
    if inp1 == 1:
        inp2 = input("press I for Insertion sort, B for Bubble sort, S for Selection sort \n >")
        inp2 = inp2.strip().upper()
        if inp2 == "I":
            insSrt = arr2.insertionSort()
            visualizer(insSrt,"Insertion sort")
        elif inp2 == "B":
            insSrt = arr2.bubbleSort()
            visualizer(insSrt,"Bubble sort")
        elif inp2 == "S":
            insSrt = arr2.selectionSort()
            visualizer(insSrt,"Selection sort")
        else:
            print("Invalid Input")
            main()
    elif inp1 ==2:
        newnewarr = ["","","","",'',"","","","",""]
        newnewnewarr = ["","","","",'',"","","","",""]
        print()
        arr2.print1()
        inp3 = input("\nPlease enter the number you want to find the index of \n >")
        inp3 = int(inp3)
        x = arr2.linearSearch(inp3)
        y,newarr = arr2.binarySearch(inp3)
        if x == -1 or y == -1:
            return
                
        newnewarr[y-1] = "↑"
        newnewnewarr[x-1] = "↑"


        print("\n Linear Search Result:",x)
        arr2.print1()
        print(newnewnewarr,"\n","\nBinary Search Result:",y,"\n",newarr,"\n",newnewarr,"\n")
    elif inp1 ==3:
        sys.exit()
    else:
        print("Invalid Input\n")
        main()     

main()




