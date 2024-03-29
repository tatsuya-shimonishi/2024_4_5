<html>
    <body>
        <h1>アドバイス</h1>
        <div>
            <h2>質問 No.{{output_no}}：{{output_question}}</h2>
            <p>アドバイス：{{output_advice}}</p>
        </div>
        <div>
            <form method="post" action="/random_advice">
                <button type="submit" name="no" value="{{output_no}}">質問に戻る</button>
            </form>
            <form method="post" action="/answer_random">
                <button type="submit" name="no" value="{{output_no}}">自己回答</button>
            </form>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>