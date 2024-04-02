<html>
    <body>
        <h1>質問内容の登録（画面入力）</h1>
        <div>
            <form method="post" action="/question_input">
                <li><label for="no">No.</label><input type="text" name="no" value="{{next_no}}">　※新規番号が自動入力されています</li>
                <li><label for="question">質問</label><input type="text" name="question"></li>
                <li><label for="answer">回答</label><input type="text" name="answer"></li>
                <li><label for="advice">アドバイス</label><input type="text" name="advice"></li>
                <input type="submit" value="登録">
            </form>
            <button onclick="location.href='question_input_init'">クリア</button>
        </div>
        <div>
            <button onclick="location.href='question_list'">質問一覧の表示</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>