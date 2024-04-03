<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <h1>質問一覧</h1>
        <div>
            <table>
                <thead>
                    <tr>
                        <th>No</th>
                        <th>質問</th>
                        <th>回答</th>
                        <th>アドバイス</th>
                    </tr>
                </thead>
                <tbody>
                    {{! content}}
                </tbody>
            </table>
        </div>
        <div class="button-container">
            <button onclick="location.href='/question_input_init'">質問内容の登録（画面入力）</button>
            <button onclick="location.href='/question_upload'">質問内容の登録（エクセルアップロード）</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>