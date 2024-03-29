<html>
    <body>
        <h1>回答</h1>
        <div>
            <h2>質問 No.{{output_no}}：{{output_question}}</h2>
            <p>回答：{{output_answer}}</p>
        </div>
        <div>
            <form method="post" action="/advice">
                <button type="submit" name="no" value="{{output_no}}">アドバイス</button>
            </form>
            <form method="post" action="/question_next">
                <button type="submit" name="no" value="{{output_no}}" id="next_question_button">次の質問</button>
            </form>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>