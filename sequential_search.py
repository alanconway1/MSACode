import random 

def sequential_search(number_list, target_value):
    for index in range(len(number_list)): 
        #determine if the number at the current index is equal to target 
        #if return the index and end the loop 
        if target_value == number_list[index]:
            return index
        
    return -1

def main():
    #creates list of 100 numbers from 1 to 100
    number_list = random.sample(range(1,101), 100)
    number_list.sort()

    found_index = sequential_search(number_list, 105)

    print(found_index)
main()