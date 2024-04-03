<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <span id="next_question_disabled"  style="display: none;">{{next_question_disabled}}</span>
        <h1>回答</h1>
        <div>
            <h2>質問 No.{{output_no}}：{{output_question}}</h2>
            <p>回答：{{output_answer}}</p>
        </div>
        <div class="button-container">
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

        <script>
            window.onload = function(){
                var next_question_disabled = document.getElementById("next_question_disabled").textContent;
                if(Number(next_question_disabled)){
                    document.getElementById("next_question_button").disabled = true;
                }
            }
        </script>
    </body>
</html>