
import numpy as np


# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()



def column_swap(input:np.array)->np.array:    
    return np.fliplr(input)



#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön





def compare_two_array(input1:np.array,input2:np.array) ->np.array:
    return np.array(np.where(np.equal(input1,input2)))




#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!


ar=np.array([2,3,2])

def get_array_shape(input_array:np.array):

    if input_array.ndim==2:
        return f"sor: {input_array.shape[1]}, oszlop: {input_array.shape[0]}, melyseg: 1"
    elif input_array.ndim==3:
        return  f"sor: {input_array.shape[2]}, oszlop: {input_array.shape[1]}, melyseg: {input_array.shape[0]}"
    elif input_array.ndim==1:
        return f"sor: {input_array.shape[0]}, oszlop: 1, melyseg: 1"
    else:
        return "incorrect input"
print(get_array_shape(ar))



# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges Y-okat egy numpy array-ből. 
#Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()



def encode_Y(input_array:np.array, num:int)->np.array:
    encoded=np.zeros((len(input_array),num))
    encoded[np.arange(len(input_array)),input_array]=1
    return encoded



# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()


def decode_Y(input_array:np.array)->np.array:
    return np.argmax(input_array,axis=1)



# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza a legvalószínübb element a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. 
# Ki: 'szilva'
# eval_classification()



def eval_classification(classes, prob):
    return classes[np.argmax(prob)]



# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()


def replace_odd_numbers(input_array)->np.array:
    return np.where(input_array % 2 == 1, -1, input_array)


# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()


ar=np.array([1, 2, 5, 0])
def replace_by_value(input_array:np.array,num:int)->np.array:
    return np.where(input_array >= num,1,-1 ) 
print(replace_by_value(ar,2))


# Készítsd egy olyan függvényt, ami az array értékeit összeszorozza és az eredmény visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza


def array_multi(input_array:np.array)->int:
    return np.prod(input_array) 


# Készítsd egy olyan függvényt, ami a 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()



def array_multi_2d(input_array:np.array)->np.array:
    return np.prod(input_array,axis=1)




# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()



def add_border(input_array:np.array)->np.array:
    return np.pad(input_array, pad_width=1)



# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot.
# Be: '2023-03', '2023-04'
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()


def list_days(date1:np.datetime64,date2:np.datetime64)->np.array:
    return np.arange(date1,date2,dtype='datetime64[D]')



# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD
# Be:
# Ki: 2017-03-24 


def current_date():
    date=np.datetime64('now','D')
    return np.datetime_as_string(date)

# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta.
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()



def sec_from_1970()->int:
    
    date=(np.datetime64('now')-np.datetime64('1970-01-01T00:02:00'))
    return int(date.item().total_seconds())


