<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <h1>アドバイス</h1>
        <div>
            <p>質問 No.{{output_no}}：{{output_question}}</p>
            <h3>{{output_advice}}</h3>
        </div>
        <div class="button-container">
            <form method="post" action="/question_return">
                <button type="submit" name="no" value="{{output_no}}">質問に戻る</button>
            </form>
            <form method="post" action="/answer">
                <button type="submit" name="no" value="{{output_no}}">自己回答</button>
            </form>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>