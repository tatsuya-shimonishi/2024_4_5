from bottle import template
import pandas as pd
import get_data as gd

#input_dataよりエクセルファイルへ登録or更新
def inputQs(input_data):
    rows_as_lists = gd.getExcel()

    #新規Noの場合は登録。既存Noの場合は更新
    if len(rows_as_lists) < input_data[gd.no]:
        rows_as_lists.append(input_data)
    else:
        rows_as_lists[input_data[gd.no]-1] = input_data

    # データフレームへ変換しExcelファイルへ書き込む
    df = pd.DataFrame(rows_as_lists, columns=['No', '質問', '回答', 'アドバイス'])
    df.to_excel(gd.file_name, index=False)

def getQsInp():
    rows_as_lists = gd.getExcel()

    #次のNoを取得
    next_no = gd.getNextNo(rows_as_lists)

    #テンプレートを返却
    return template("input_temp", next_no=next_no)