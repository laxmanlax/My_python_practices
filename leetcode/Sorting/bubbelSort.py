def bubble_sort(input_list):

    for i in range(len(input_list)):
        swapped = False 

        for j in range(len(input_list) - 1):
            if input_list[i] < input_list[j]:
                input_list[i] , input_list[j] = input_list[j] , input_list[i]
                
            
