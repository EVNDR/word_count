
my_dict = {}
def in_put(string):
    string_list = string.split()
    for item in string_list:
        if item in my_dict:
            my_dict[item] +=1
        else:   
            my_dict[item] = 1
    print(my_dict)        

in_put("olly olly in come free")