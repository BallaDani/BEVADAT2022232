# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index): 
    sublist=input_list[start_index:end_index]
    return sublist


    
        


# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    outlist=input_list[::step_size]
    return outlist

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    for i, x in enumerate(input_list):
        isunique=True
        for j, y in enumerate(input_list):
            if (i!=j):
                if(input_list[i]==input_list[j]):
                    isunique=False
        if (isunique):
            return True
    return False                

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def fletten(input_list):
    flist=[]
    for x in input_list:
        for y in x:
            flist.append(y)
    return flist        

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    merged=[]
    for x in args:
        for y in x:
            merged.append(x)
    return merged        


# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    rlist=[]
    for x in input_list:
        rlist.append(x[::-1])
    return rlist

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list):
    for i,x in enumerate(input_list):
        for j,y in enumerate(input_list):
            if(i !=j):
                if(input_list[i]==input_list[j]):
                    input_list.pop(j)
    return input_list                

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    tList = [[0 for x in range(len(input_list))] for y in range(len(input_list[0]))] 
    for i, x in enumerate(input_list):
        for j, y in enumerate(x):
            tList[j][i] = y        
    return tList

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    lec = 0
    for x in input_list:
        lec += len(x)
    row = int(lec / chunk_size) + (lec % chunk_size > 0)
    column = chunk_size
    splittedList = [[0 for x in range(row)] for y in range(column)]
    for i, x in enumerate(input_list):
        for j, y in enumerate(x):
            id = i*len(input_list[i-1])+j
            splittedListRow = int(id/row)
            splittedListColumn = int(id%row)
            splittedList[splittedListRow][splittedListColumn] = input_list[i][j]
                
    return splittedList

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    mdict = []
    for d in dict:
        for x, y in d.items():
            mdict.append([x,y])
    return mdict

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    pdict = {
        "even": [],
        "odd": [],}
    for x in input_list:
        if (x%2==0):
            pdict["even"].append(x)
        else:
            pdict["odd"].append(x)
    return pdict


# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    mdict = {}
    for item in input_dict:
        mdict[item] = sum(input_dict[item]) / len(input_dict[item])
    return mdict

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


