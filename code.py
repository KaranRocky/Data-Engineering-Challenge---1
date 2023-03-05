import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set()
city_df = pd.read_csv("/kaggle/input/housing-data/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
county_df = pd.read_csv("/kaggle/input/housing-data/County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
metro_df = pd.read_csv("/kaggle/input/housing-data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
neighb_df = pd.read_csv("/kaggle/input/housing-data/Neighborhood_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
state_df = pd.read_csv("/kaggle/input/housing-data/State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
zip_df = pd.read_csv("/kaggle/input/housing-data/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")

df_ls = [city_df, county_df, metro_df, neighb_df, state_df, zip_df]
labels = ["City", "County", "Metro", "Neighbors", "State", "Zip"]
for i, df in enumerate(df_ls):
    print(f"\n\n\n------------{labels[i]}-------------")
    print(df.columns[:10])
    print(df[df.columns[:10]].head(2))
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
## Pandas Profiling
from pandas_profiling import ProfileReport

for i, df in enumerate(df_ls):
    profile = ProfileReport(df)
    profile.to_file(f"./analysis_{labels[i]}.html")

