import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = '1234'
host = 'localhost'
database = 'cvr'

connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

engine = create_engine(connection_string)

df_sql = pd.read_sql('SELECT * FROM student', engine)

print(df_sql)

"""
OUTPUT : 
     sno     sname  marks       city    mobile  gender
0   6701  Abhishek   90.0  Hyderabad  99887766    Male
1   6702      Abhi   80.0  Hyderabad  99887766    Male
2   6703      Rani   34.0       Pune  99887766  Female
3   6704   Hemanth   50.0  Hyderabad  99887766    Male
4   6705    Kalyan   78.0   Banglore  99887766    Male
5   6706       Raj   54.0  Hyderabad  99887766    Male
6   6707    Ganesh   10.0       Pune  99887766    Male
7   6708     Aryan   95.0  Hyderabad  99887766    Male
8   6709   Avinash   87.0   Banglore  99887766    Male
9   6710   Bharath   82.0  Hyderabad  99887766    Male
10  6711      Sita   77.0   Banglore  99887766  Female
11  6712     Geeta   75.0       Pune  99887766  Female
12  6713      Hema   77.0  Hyderabad  99887766  Female
13  6714    Ganesh   86.0  Hyderabad  99887766    Male

Process finished with exit code 0

"""