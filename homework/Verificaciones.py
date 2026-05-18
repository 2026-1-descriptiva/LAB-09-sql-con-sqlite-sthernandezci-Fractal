import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

# Cargar CSV exactamente como el test
df = pd.read_csv(
    "files/input/tbl1.csv",
    names=["K0","K1","c12","c13","c14","c15","c16"]
)
df.to_sql("tbl1", conn, index=False, if_exists="replace")

query = """
SELECT COUNT(*)
FROM tbl1
WHERE strftime('%Y', c14) = '2018'
"""

print(pd.read_sql_query(query, conn).to_dict())