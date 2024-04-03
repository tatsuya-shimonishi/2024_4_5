<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <h1>質問内容の登録（画面入力）</h1>
        <div>
            <form method="post" action="/question_input">
                <div class="form-group">
                    <label for="no">No.</label>
                    <input type="text" name="no" value="{{next_no}}">
                </div>
                <div class="form-group">
                    <label for="question">質問</label>
                    <textarea type="text" name="question"></textarea>
                </div>
                <div class="form-group">
                    <label for="answer">回答</label>
                    <textarea type="text" name="answer"></textarea>
                </div>
                <div class="form-group">
                    <label for="advice">アドバイス</label>
                    <textarea type="text" name="advice"></textarea>
                </div>
                <input type="submit" value="登録">
            </form>
        </div>
        <div>
            <button onclick="location.href='question_input_init'">クリア</button>
            <button onclick="location.href='question_list'">質問一覧の表示</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>