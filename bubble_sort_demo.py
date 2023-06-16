import random 

def bubble_sort(data_list):
    number_of_items = len(data_list)
    #loop through the list to visit each item 
    for i in range(number_of_items):
        #loop through list to compare items to adjacent items on the list
        for j in range(number_of_items - 1):
            #compare adjacent items in the list
            if(data_list[j+1] > data_list[j]):
                #if right element is less than left element then swap position
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
    return data_list

def main(): 
    #create lsit of integers
    integer_list = random.sample(range(0,1000), 100)
    
    #call the bubble sort function 
    sorted_list = bubble_sort(integer_list)
    print(sorted_list)
main()

