#Sorts integers provided via a file named 'data.txt' via stooge sort and exports the 
# sorted list to a file named 'stooge.txt'
#Author: Shawn McMannis
#Last mod date: 4/10/19

#sorts a list of integers using stooge sort
def stoogeSort(toSort, low, high):
    #base case
    if low >= high:
        return

    #if the low element is larger than the high element, swap them
    if (toSort[low] > toSort[high]):
        temp = toSort[low]
        toSort[low] = toSort[high]
        toSort[high] = temp

    #recursive case
    if (high - low) > 1:
        #calculate where to cut the array
        m = ((high - low + 1) // 3)

        #recursive calls
        stoogeSort(toSort, low, (high - m))
        stoogeSort(toSort, (low + m), high)
        stoogeSort(toSort, low, (high - m))


#main
toSort = []

#open the export file
exportFile = open("stooge.txt", "w")

#open import file 'sampleInput.txt'
with open("sampleInput.txt", "r") as importFile:
    for line in importFile:

        #save the value string as a list, delimited by ' '
        toSort = line.split()

        #convert string values to integers
        for i in range(0, len(toSort)):
            toSort[i] = int(toSort[i])

        #remove the first integer value from the list
        del toSort[0]

        #sort the list with stooge sort
        stoogeSort(toSort, 0, (len(toSort) - 1))

        #save the sorted list to 'stooge.txt'
        for num in toSort:
            exportFile.write(str(num))
            exportFile.write(" ")
        exportFile.write("\n")

#close export file
exportFile.close()