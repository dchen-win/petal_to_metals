from multiprocessing.resource_sharer import stop
import re
string_val = "<a> <b> <c>  foo </c> </b> <d>  bar </d>  baz </a>"
string_val_new = string_val.split()
print(string_val_new)
pattern = re.compile('<.*?>', string_val_new[0])

    # temp_data_list = string_val_new.copy()
    # new_list = []
    # while temp_data_list:
        
    #     a = temp_data_list[0] 
    #     for x in temp_data_list: 
    #         if re.match('<.*>', temp_data_list[x]) != None
    #              new_list.append( temp_data_list[x])
           
    #         elif stop
                    
    #     #Add values in the new list
    #     new_list.append(minimum)
    #     #Remove values from the original list
    #     temp_data_list.remove(minimum) 






print(re.match('<.*>', string_val_new[7]))
# print(re.match('<.*>', string_val_new).group())


# def sldfaj(string_in):
#     """sfdlsfkj"""
#     pass
# list = sldfaj(string_val) # ['<a>', '<b>', '<c>', '</c>', '</b>', '<d>', '</d>', '</a>']



  