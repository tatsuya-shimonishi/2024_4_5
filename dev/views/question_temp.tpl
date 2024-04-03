<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <span id="back_question_disabled"  style="display: none;">{{back_question_disabled}}</span>
        <span id="next_question_disabled"  style="display: none;">{{next_question_disabled}}</span>
        <h1>質問 No.{{output_no}}</h1>
        <div>
            <p>{{output_question}}</p>
        </div>
        <div class="button-container">
            <form method="post" action="/question_back">
                <button type="submit" name="no" value="{{output_no}}" id="back_question_button">前の質問</button>
            </form>
            <form method="post" action="/advice">
                <button type="submit" name="no" value="{{output_no}}">アドバイス</button>
            </form>
            <form method="post" action="/answer">
                <button type="submit" name="no" value="{{output_no}}">自己回答</button>
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
                var back_question_disabled = document.getElementById("back_question_disabled").textContent;
                var next_question_disabled = document.getElementById("next_question_disabled").textContent;
                if(Number(back_question_disabled)){
                    document.getElementById("back_question_button").disabled = true;
                }
                if(Number(next_question_disabled)){
                    document.getElementById("next_question_button").disabled = true;
                }
            }
        </script>
    </body>
</html>