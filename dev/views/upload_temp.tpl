<html>
    <body>
        <h1>質問内容の登録（Excelアップロード）</h1>
        <div>
            <form action="/question_upload" method="post" enctype="multipart/form-data">
                <input type="file" name="uploadFile">
                <input type="submit" value="登録">
                <span>{{reg_result}}</span>
            </form>
        </div>
        <div>
            <button onclick="location.href='question_list'">質問一覧の表示</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>