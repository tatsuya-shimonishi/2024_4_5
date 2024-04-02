from bottle import template
import get_data as gd

#質問画面のテンプレートを取得
def getQsTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]
    back_question_disabled = tmp[1]
    next_question_disabled = tmp[2]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("question_temp", output_no=output_no, output_question=output_question, back_question_disabled=back_question_disabled, next_question_disabled=next_question_disabled)

