import csv
import numpy as np

# データを抽出する
def open_data(order=None):
    # testデータかfullデータか訊く
    if order == None:
        print('test or full = ', end='')
        order = input()

    # 取り敢えず全データぶっこ抜く
    with open ('../data')
