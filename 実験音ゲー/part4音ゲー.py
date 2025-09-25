#しばらく勉強しようと思っていたのですが、番外編として、音ゲーのシステムを作ってみたいと思います！
# 最近音ゲーにはまってて、その動きに興味があったので、自分で作ってみることにしました。
import time
import json
#言い忘れていましたが、実験的なものなので、グラフィックも当たり判定もないものになっています。
#譜面の保存形式はjsonで、手打ちです

#最悪なことに、ここまで完成したコードが消えてしまいました。。。(´;ω;｀)
# 書き直すのは苦ではないのですが、コメントを書きなおすのはだるすぎるので許してください
with open("musical.json","r",encoding="utf-8") as f:
    score_data = json.load(f)
    notes = score_data["notes"]

    print("譜面データの読み取りに成功しました")

    height = 800
    d_speed = 300
    frame = 1 / 30

    input("enterを押して実行→")

    start_time = time.time()

    while time.time() - start_time < 10:
        now = time.time() - start_time
        print(f"--- 現在時刻: {now:.2f}秒 ---")

        for note in notes:
          hit = note["timing"] - now
          distance = d_speed * note["speed"] * hit

          if 0 < distance < height:
            print(f"レーン{note['position']}のタイプ{note['type']}のノーツが、距離{distance:.0f}ピクセル上にあり、残り{hit:.2f}秒でヒットします！")
        time.sleep(1 / 30)
print("10秒経過したので、終了しました")        

# ここまで書き直すのに1時間くらいかかりました。。。疲れた
# めっちゃ簡単にしたので、実際の音ゲーとは全然違いますが、雰囲気はわかると思います。
#本来の音ゲーでは、jsonを手入力じゃなくて、譜面エディタで作成したりするらしいです
#グラフィック、当たり判定なんかもそこまで難しいわけではないので、技術が身に付いたらまた挑戦してみたいと思います！

#番外編になりましたが、ここまで読んでいただきありがとうございました！
#次回は