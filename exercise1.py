'''
Write a solution to create a DataFrame from a 2D list called student_data.
This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+

'''
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
 