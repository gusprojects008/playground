import pandas as pd
import sqlite3
import sys

def conversor():
    if len(sys.argv) != 3:
       print("Error usage: python script.py input_file.csv output_file.db")
       sys.exit(1)

    csv_file = sys.argv[1]
    db_file = sys.argv[2]

    try:
       df = pd.read_csv(csv_file)

       # connect and create table in sqlite3 server
       conn = sqlite3.connect(db_file)
       # convertion
       df.to_sql("tabela", conn, if_exists="replace", index=False)
       conn.close()
       print("Success!")
    except Exception as error:
           print(f"Error: {str(error)}")

if __name__ == "__main__":
   conversor()
