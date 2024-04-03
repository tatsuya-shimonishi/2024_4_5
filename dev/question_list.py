from bottle import template
import get_data as gd

#テンプレートを取得
def getQsListtemp():
    file_pass = "views\question_list_temp.tpl"

    #Excelデータの取得
    rows_as_lists = gd.getExcel()

    #テンプレートデータへ表の書き込み
    content = ""
    for row_data in rows_as_lists:
        tmp = f"<tr><td>{row_data[0]}</td><td>{row_data[1]}</td><td>{row_data[2]}</td><td>{row_data[3]}</td></tr>"
        tmp = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            str(row_data[0]).replace('_x000D_', '<br>'),
            str(row_data[1]).replace('_x000D_', '<br>'),
            str(row_data[2]).replace('_x000D_', '<br>'),
            str(row_data[3]).replace('_x000D_', '<br>')
        )
        content = content + tmp

    return template("question_list_temp", content=content)