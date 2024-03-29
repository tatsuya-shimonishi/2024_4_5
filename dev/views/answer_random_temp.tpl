<html>
    <body>
        <h1>回答</h1>
        <div>
            <h2>質問 No.{{output_no}}：{{output_question}}</h2>
            <p>回答：{{output_answer}}</p>
        </div>
        <div>
            <form method="post" action="/advice_random">
                <button type="submit" name="no" value="{{output_no}}">アドバイス</button>
            </form>
            <button onclick="location.href='random'">次の質問</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>