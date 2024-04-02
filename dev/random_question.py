from bottle import template
import random
import get_data as gd

#ランダム質問画面のテンプレートを取得
def getRdTemp():
    rows_as_lists = gd.getExcel()

    #質問Noをランダムに設定
    max_count = len(rows_as_lists)-1
    disp_no = random.randint(0, max_count)

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("random_temp", output_no=output_no, output_question=output_question)

#ランダム質問画面のテンプレートを取得　※アドバイス画面からの遷移
def getRdAdTemp(disp_no):
    rows_as_lists = gd.getExcel()

    #質問Noを取得
    tmp = gd.getNo(disp_no, rows_as_lists)
    output_no = tmp[0]

    #質問内容を取得
    output_question = gd.getQuestion(disp_no, rows_as_lists)
    
    #テンプレートを返却
    return template("random_temp", output_no=output_no, output_question=output_question)

