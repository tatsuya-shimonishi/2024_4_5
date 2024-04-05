from bottle import template, request

#テンプレートを取得
def getQsUptemp(reg_result=""):
    return template("upload_temp", reg_result=reg_result)

#Excelファイルを登録
def regExcel():
    result = ""
    uploaded_file = request.files.get("uploadFile")
    uploaded_file_name = uploaded_file.filename
    file_path = "question_list.xlsx"
    extensions = ('.xlsx', '.xls', '.xlsm')

    #Excelファイルの判定
    if uploaded_file_name.endswith(extensions):
        # ファイルをバイナリ書き込みモードで保存
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.file.read())
        result = "登録完了"
    else:
        result = "※Excelファイルを選択してください"

    return result
