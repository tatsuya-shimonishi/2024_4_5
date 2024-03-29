from bottle import route, run, template, request
import pandas as pd
import random

#Excelファイルの読み込み
input_file_name = "question_list.xlsx"
df = pd.read_excel(input_file_name)

#リスト化
rows_as_lists = df.values.tolist()

#Excelの項目定義
no = 0
question = 1
answer = 2
advice = 3

#対象データのNoを抽出
def getNo(disp_no):
    target_index = disp_no
    output_no = rows_as_lists[target_index][no]
    return output_no

#対象データの質問を抽出
def getQuestion(disp_no):
    target_index = disp_no
    output_question = rows_as_lists[target_index][question]
    return output_question

#質問画面のテンプレートを取得
def getRdTemp():
    max_count = len(rows_as_lists)-1
    disp_no = random.randint(0, max_count)

    #質問Noを取得
    output_no = getNo(disp_no)

    #質問内容を取得
    output_question = getQuestion(disp_no)
    
    return template("random_temp", output_no=output_no, output_question=output_question)

