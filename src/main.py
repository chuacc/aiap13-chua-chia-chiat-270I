import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from utils import *



con = sqlite3.connect("../data/failure.db")
df = pd.read_sql_query("SELECT * from failure", con)
con.close()

# Data cleaning
df = dataclean(df)

# Data preparation
# Transform ordinal features into numerical features
df= encode(df)


