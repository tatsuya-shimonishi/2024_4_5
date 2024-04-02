from bottle import route, request
import pandas as pd

#Excelの項目定義
no = 0
question = 1
answer = 2
advice = 3

#Excelファイル名
file_name = "question_list.xlsx"

#Excelデータの取得
def getExcel():
    #Excelファイルの読み込み
    df = pd.read_excel(file_name)

    #リスト化
    rows_as_lists = df.values.tolist()
    return rows_as_lists

#対象データのNoを取得
def getNo(disp_no, rows_as_lists):
    val = [0, 0, 0]

    #最初の質問の時だけ「前の質問」の非活性フラグを立てる
    if not disp_no:
        val[1] = 1
    
    #最後の質問の時だけ「次の質問」の非活性フラグを立てる
    if len(rows_as_lists) == disp_no+1:
        val[2] = 1

    #対象データの特定
    target_index = disp_no
    val[0] = rows_as_lists[target_index][no]
    return val

#対象データの質問を取得
def getQuestion(disp_no, rows_as_lists):
    target_index = disp_no
    output_question = rows_as_lists[target_index][question]
    return output_question

#対象データの回答を取得
def getAnswer(disp_no, rows_as_lists):
    target_index = disp_no
    output_answer = rows_as_lists[target_index][answer]
    return output_answer

#対象データのアドバイスを取得
def getAdvice(disp_no, rows_as_lists):
    target_index = disp_no
    output_advice = rows_as_lists[target_index][advice]
    return output_advice

#次のNoを取得
def getNextNo(rows_as_lists):
    next_no = len(rows_as_lists)+1
    return next_no