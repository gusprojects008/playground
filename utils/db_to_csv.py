import sqlite3
import pandas as pd

path = input("DB filepath: ")

conn = sqlite3.connect(path)

df = pd.read_sql_query("SELECT * FROM nome_da_tabela", conn)

df.to_csv('resultado.csv', index=False)
