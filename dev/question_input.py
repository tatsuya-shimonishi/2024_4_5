from bottle import template
import pandas as pd
import get_data as gd

#質問一覧の取得
def getRegData(disp_no):
    no_judge = ""
    no = ""
    question = ""
    answer = ""
    advice = ""

    #画面入力のNoが数字以外の場合にエラー表示して、後続の処理は行わない
    try:
        disp_no = int(disp_no)-1
    except ValueError as e:
        no_judge = "※数字を入力してください"
        return template("input_reg_temp", no_judge=no_judge, no=disp_no, question=question, answer=answer, advice=advice)

    #Excelデータを取得
    rows_as_lists = gd.getExcel()
    
    #画面入力のNoが登録データ以外なら後続の処理は行わない
    max_count = len(rows_as_lists)-1
    if disp_no > max_count:
        no_judge = "※対象Noのデータは登録されていません"
        return template("input_reg_temp", no_judge=no_judge, no=disp_no+1, question=question, answer=answer, advice=advice)

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    no = tmp[0]

    #質問内容を取得
    question = str(gd.getQuestion(disp_no, rows_as_lists)).replace('_x000D_', '')

    #回答内容を取得
    answer = str(gd.getAnswer(disp_no, rows_as_lists)).replace('_x000D_', '')

    #アドバイス内容を取得
    advice = str(gd.getAdvice(disp_no, rows_as_lists)).replace('_x000D_', '')

    #テンプレートを返却
    return template("input_reg_temp", no_judge=no_judge, no=no, question=question, answer=answer, advice=advice)

#input_dataよりエクセルファイルへ登録or更新
def inputQs(input_data):

    #Noの画面入力が数字以外の場合にエラー表示して、後続の処理は行わない
    try:
        input_data[gd.no] = int(input_data[gd.no])
    except ValueError as e:
        return "※数字を入力してください"
    
    #Excelのデータを取得
    rows_as_lists = gd.getExcel()

    #新規Noの場合は登録。既存Noの場合は更新
    if len(rows_as_lists) < input_data[gd.no]:
        rows_as_lists.append(input_data)
    else:
        rows_as_lists[input_data[gd.no]-1] = input_data

    # データフレームへ変換しExcelファイルへ書き込む
    df = pd.DataFrame(rows_as_lists, columns=['No', '質問', '回答', 'アドバイス'])
    df.to_excel(gd.file_name, index=False)

    return f"No.{input_data[gd.no]} 登録完了"

#テンプレート返却
def getQsInp(no_judge=""):
    rows_as_lists = gd.getExcel()

    #次のNoを取得
    next_no = gd.getNextNo(rows_as_lists)

    #テンプレートを返却
    return template("input_temp", next_no=next_no, no_judge=no_judge)