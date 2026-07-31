import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_name = ['student_id', 'age']
    rezultat_dataframe = pd.DataFrame(student_data, columns = column_name)
    return rezultat_dataframe

if __name__ == '__main__':

    date_de_test = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    
    studenti = createDataframe(date_de_test)
    print(studenti)
 