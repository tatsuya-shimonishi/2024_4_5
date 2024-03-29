from bottle import route, run, template, request
import pandas as pd

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

#対象データの質問を抽出
def getQuestion(disp_no):
    target_index = disp_no
    output_question = rows_as_lists[target_index][question]
    return output_question

#質問画面のテンプレートを取得
def getQsTemp(disp_no):
    disp_no = int(disp_no)

    #質問Noを取得
    val = getNo(disp_no)
    output_no = val[0]
    back_question_disabled = val[1]
    next_question_disabled = val[2]

    #質問内容を取得
    output_question = getQuestion(disp_no)
    
    return template("question_temp", output_no=output_no, output_question=output_question, back_question_disabled=back_question_disabled, next_question_disabled=next_question_disabled)

