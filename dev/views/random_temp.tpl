<html>
    <body>
        <h1>質問 No.{{output_no}}</h1>
        <div>
            <p>{{output_question}}</p>
        </div>
        <div>
            <form method="post" action="/advice">
                <button type="submit" name="no" value="{{output_no}}">アドバイス</button>
            </form>
            <form method="post" action="/answer">
                <button type="submit" name="no" value="{{output_no}}">自己回答</button>
            </form>
            <button onclick="location.href='random'">次の質問</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>