import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

def csv_to_df(path):
    data=pd.read_csv(path)
    return data



#df=csv_to_pd("StudentsPerformance.csv")
#print(df)


'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

def capitalize_columns(df_data):
   df_copy = df_data.copy()   
   return df_copy.rename(columns=lambda x: x if ('e' in x) else x.upper())
   



'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

def math_passed_count(df_data):
    df_copy = df_data.copy()
    return  len(df_copy[df_copy["math score"]>=50])




'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

def did_pre_course(df_data):
    df_copy = df_data.copy()    
    return df_copy[df_copy["test preparation course"]=="completed"]


'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

def average_scores(df_data):
     df_copy = df_data.copy()
     return df_copy.groupby(['parental level of education']).mean()
    


'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

def add_age(df_data):
    df_copy = df_data.copy()
    np.random.seed(42)
    df_copy['age']=np.random.randint(18,67,df_copy.shape[0])    
    return df_copy


'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

def female_top_score(df_data):
     df_copy = df_data.copy()
     df_copy['total']=(df_copy['math score']+df_copy['reading score']+df_copy['writing score'])/300
     return tuple(df_copy.nlargest(1,'total').where(df_copy['gender']=='female').values.tolist()[0][5:8])



'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

def add_grade(df_data):
    df_copy = df_data.copy()
    grade=[]
    df_copy['total']=(df_copy['math score']+df_copy['reading score']+df_copy['writing score'])/300
    for row in df_copy['total']:
        if row>0.90:grade.append('A')
        elif row>0.80:grade.append('B')
        elif row>0.70:grade.append('C')
        elif row>0.60:grade.append('D')
        else :grade.append('F') 
    df_copy['grade']=grade
    df_copy=df_copy.drop(columns=['total'])
    return df_copy


'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''



def math_bar_plot(df_data):
    df_copy = df_data.copy()    
    df_seged=df_copy.groupby('gender').mean()
    df_seged = df_seged.drop(df_seged.columns[[1,2 ]], axis=1)
    fig,ax=plt.subplots()
    ax.bar(df_seged.index,df_seged['math score'])
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    ax.set_title('Average Math Score by Gender')      
    return fig




''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

def writing_hist(df_data):
    df_copy = df_data.copy()
    fig,ax=plt.subplots()   
    ax.hist(df_copy['writing score'])
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')
    return fig



''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

def ethnicity_pie_chart(df_data):
    df_copy = df_data.copy()
    eth= df_copy.groupby("race/ethnicity")["race/ethnicity"].count()   
    fig,ax=plt.subplots()
    ax.pie(eth.values, labels = eth.index, autopct="%0.01f%%")
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig



