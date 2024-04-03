import pylab
import os,sys
import os
import io
import os.path 
import csv
import pandas as pd
import numpy as np
import numpy.matlib
from tkinter import *
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
from datetime import datetime as dt
import datetime
import copy
import openpyxl as px
import pprint
import math
import time
import xlrd
import random
from tqdm import tqdm
import itertools
from scipy.stats import multivariate_normal
from scipy.optimize import fmin
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.decomposition import PCA
import glob
import shutil
from sklearn import linear_model

def printer():
    #印刷データ読込
    df2 = pd.DataFrame()
    print_file = "C:/Users/00190409284/Desktop/04_MLCC品質改善PJT_検証ロット/台板紐付けツール_成形印刷積層/printer/printer_data.csv"
    printer_collist = ["測長C現在値[m]","TOTAL印刷C[枚]","ロール使用長"]
    df2 = pd.read_csv(print_file,usecols=printer_collist,header=0,encoding="shift-jis")
    df2["測長C現在値[m]"] = pd.to_numeric(df2["測長C現在値[m]"],errors="coerce")

    #印刷の使用長さを反転させて、成形と紐付けようにする






    #積層データ読込
    df3 = pd.DataFrame()
    sps_file = "C:/Users/00190409284/Desktop/04_MLCC品質改善PJT_検証ロット/台板紐付けツール_成形印刷積層/sps/sps_data.csv"
    sps_collist = ["SET CNT","積層数(現)","LOT総枚数現在値"]
    df3 = pd.read_csv(sps_file,usecols=sps_collist,header=0,encoding="shift-jis")

    df_merge = pd.DataFrame()
    df_merge = pd.merge(df2,df3,left_on="TOTAL印刷C[枚]", right_on="LOT総枚数現在値")
    df_merge.reset_index()
    df2["紐付用、反転"] = df2["ロール使用長"].max() - df2["ロール使用長"] + df2["ロール使用長"]
    df_merge.to_csv(dir + "/df_merge.csv")
    print("===========積層完了=============")
#result = printer()
#print(result)

