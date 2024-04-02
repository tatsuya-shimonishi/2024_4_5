from bottle import route, run, template, request
import question as qs
import random_question as rdqs
import answer as ans
import advice as adv
import question_input as inp
import question_upload as upl
import question_list as lis

#ホーム画面
@route("/home")
def home():
    return template("home_temp")

#質問画面（順次）
@route("/question")
def question():
    disp_no = 0
    return qs.getQsTemp(disp_no)

#質問画面（順次）※「前の質問」ボタン押下時
@route("/question_back", method="POST")
def do_question():
    disp_no = request.forms.no
    disp_no = int(disp_no)-2
    return qs.getQsTemp(disp_no)

#質問画面（順次）※「次の質問」ボタン押下時
@route("/question_next", method="POST")
def do_question():
    disp_no = request.forms.no
    disp_no = int(disp_no)
    return qs.getQsTemp(disp_no)

#質問画面（ランダム）
@route("/random")
def randomQuestion():
    return rdqs.getRdTemp()

#質問画面（ランダム）※アドバイス画面からの遷移
@route("/random_advice", method="POST")
def randomQuestion():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return rdqs.getRdAdTemp(disp_no)

#質問画面　※「質問に戻る」ボタン押下時
@route("/question_return", method="POST")
def do_question():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return qs.getQsTemp(disp_no)

#回答画面
@route("/answer", method="POST")
def answer():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return ans.getAnTemp(disp_no)

#回答画面　※ランダム画面からの遷移
@route("/answer_random", method="POST")
def answer():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return ans.getAnRdTemp(disp_no)

#アドバイス画面
@route("/advice", method="POST")
def advice():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return adv.getAdTemp(disp_no)

#アドバイス画面　※ランダム画面からの遷移
@route("/advice_random", method="POST")
def advice():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return adv.getAdRdTemp(disp_no)

#質問内容の登録（画面入力）画面
@route("/question_input_init")
def question_input_init():
    #キャッシュクリア
    global cache_data
    cache_data = {}
    return inp.getQsInp()

#質問内容の登録（画面入力）画面　※登録ボタン押下
@route("/question_input", method="POST")
def question_input():

    #画面入力内容を取得
    input_data = [
        int(request.forms.no),
        request.forms.question,
        request.forms.answer,
        request.forms.advice
    ]

    #画面入力より登録or更新
    inp.inputQs(input_data)

    #キャッシュクリア
    global cache_data
    cache_data = {}

    #画面更新
    return inp.getQsInp()

#質問内容の登録（Excelアップロード）画面
@route("/question_upload")
def question_upload():
    return "質問内容の登録（Excelアップロード）画面"

#質問一覧画面
@route("/question_list")
def question_list():
    return "質問一覧画面"

# キャッシュをクリアするエンドポイント
@route('/clear_cache')
def clear_cache():
    global cache_data
    cache_data = {}  # キャッシュを空にする
    return 'Cache cleared!'

run(host="localhost", port=8080, debug=True)
