from bottle import template
import get_data as gd

#アドバイス画面のテンプレートを取得
def getAdTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)

    #アドバイス内容を取得
    output_advice = gd.getAdvice(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("advice_temp", output_no=output_no, output_question=output_question, output_advice=output_advice)

#アドバイス画面のテンプレートを取得　※ランダム画面からの遷移
def getAdRdTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)

    #アドバイス内容を取得
    output_advice = gd.getAdvice(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("advice_random_temp", output_no=output_no, output_question=output_question, output_advice=output_advice)

