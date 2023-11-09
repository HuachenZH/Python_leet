import pandas as pd
import pdb

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    col1 = []
    col2 = []
    for student in student_data:
        col1.append(student[0])
        col2.append(student[1])
    df = pd.DataFrame({"student_id": col1, "age": col2})
    return df 


student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
res = createDataframe(student_data)
print(res)