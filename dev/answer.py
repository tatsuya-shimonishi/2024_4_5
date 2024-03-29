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

#対象データの質問を抽出
def getAnswer(disp_no):
    target_index = disp_no
    output_answer = rows_as_lists[target_index][answer]
    return output_answer

#質問画面のテンプレートを取得
def getAnTemp(disp_no):

    #質問Noを取得
    output_no = getNo(disp_no)

    #質問内容を取得
    output_question = getQuestion(disp_no)

    #回答内容を取得
    output_answer = getAnswer(disp_no)
    
    return template("answer_temp", output_no=output_no, output_question=output_question, output_answer=output_answer)

#質問画面のテンプレートを取得
def getAnRdTemp(disp_no):

    #質問Noを取得
    output_no = getNo(disp_no)

    #質問内容を取得
    output_question = getQuestion(disp_no)

    #回答内容を取得
    output_answer = getAnswer(disp_no)
    
    return template("answer_random_temp", output_no=output_no, output_question=output_question, output_answer=output_answer)
