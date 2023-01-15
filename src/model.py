import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



con = sqlite3.connect("../data/failure.db")
df = pd.read_sql_query("SELECT * from failure", con)
con.close()