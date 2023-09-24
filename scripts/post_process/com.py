#!/bin/usr/env python3 

import pandas as pd

df_finale = pd.DataFrame()


df1 = pd.read_csv("/home/arms04/catkin_ws/src/mrpp_sumo/ppa_exhaustive.csv")
df2 = pd.read_csv("/home/arms04/catkin_ws/src/mrpp_sumo/ppa_random.csv")
df3 = pd.read_csv("/home/arms04/catkin_ws/src/mrpp_sumo/ppa_greedy.csv")
df4 = pd.read_csv("/home/arms04/catkin_ws/src/mrpp_sumo/ppa_sampled.csv")


df_finale = df_finale.append(df1,ignore_index = True)
df_finale = df_finale.append(df2,ignore_index = True)
df_finale = df_finale.append(df3,ignore_index = True)
df_finale = df_finale.append(df4,ignore_index = True)

df_finale.to_csv("/home/arms04/catkin_ws/src/mrpp_sumo/ppas.csv")


print("run successful")