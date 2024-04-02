from bottle import template
import get_data as gd

#回答画面のテンプレートを取得
def getAnTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]
    next_question_disabled = tmp[2]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)

    #回答内容を取得
    output_answer = gd.getAnswer(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("answer_temp", output_no=output_no, output_question=output_question, output_answer=output_answer, next_question_disabled=next_question_disabled)

#回答画面（ランダム）のテンプレートを取得
def getAnRdTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)

    #回答内容を取得
    output_answer = gd.getAnswer(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("answer_random_temp", output_no=output_no, output_question=output_question, output_answer=output_answer)
