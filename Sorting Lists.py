array = [123,23,1,3213,432,43532,2312,123124,1222,32324,2312,232344,999,77,665,5453,9877]
name = ["cian","ken","ben","ten","man","cian","ken","ben","ten","man","cian","ken","ben","ten","man""cian","ken","ben","ten","man"]


def sort(array1, names):
    for i in range(0, len(array1)-1):
        lowpos = i
        x = i +1
        while x < len(array1):
            if array[x] < array1[lowpos]:
                lowpos = x
            x= x+1
            temp = array1[i]
            array1[i] = array1[lowpos]
            array1[lowpos] = temp
            temp = names[i]
            names[i] = names[lowpos]
            names[lowpos] = temp
    return names, array1

print(sort(array, name))


def bubblesort(array1):
  for i in range(len(array1)):
    for j in range( len(array1) - 1, i, -1 ):
      if ( array1[j] < array1[j - 1] ):
          temp = array1[j]
          array1[j] = array1[j-1]
          array1[j-1] = temp
    return array1

print(bubblesort(array))

#really simple and basic functions for sorting lists in python
