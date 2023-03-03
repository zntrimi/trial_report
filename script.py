from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import textwrap

#st.title("体験会用コメントシート")
st.set_page_config(page_title="体験会コメントシートメーカー")
st.title("体験会コメントシートメーカー")

book = st.selectbox(
    'どの絵本ですか？',
    ('たんぽぽのぽんちゃん', 'ぼくエスカレーター', 'グルメなペリカン'))

crew = st.selectbox(
    '読み手は誰ですか?',
    ('Zen', 'Cory')
)

upload_image = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])
name = st.text_input("こどものなまえ(〇〇ちゃん/くん)")
comment = st.text_area("コメント(難しい漢字は表示されないよ！)")

if upload_image is not None:

    if st.button("実行"):

        if book == "たんぽぽのぽんちゃん" and crew =="Cory":
            img = Image.open("Assets/1.jpg")
        elif book == "たんぽぽのぽんちゃん" and crew =="Zen":
            img = Image.open("Assets/3.jpg")
        elif book == "ぼくエスカレーター" and crew == "Cory":
            img = Image.open("Assets/2.jpg")
        elif book == "ぼくエスカレーター" and crew == "Zen":
            img = Image.open("Assets/4.jpg") 
        elif book == "グルメなペリカン" and crew == "Cory":
            img = Image.open("Assets/5.jpg") 
        else:
            img = Image.open("Assets/6.jpg") 




        ss_image = Image.open(upload_image).convert('RGBA')

        if ss_image is not None and name != "" and comment !="":
            # 画像を開く

            width = 1050 # 指定したい画像の幅
            height = int(ss_image.size[1] * (width / ss_image.size[0]))
            ss_image = ss_image.resize((width, height))
            img.paste(ss_image, (192, 1638), ss_image)

            # テキストを描画する
            draw = ImageDraw.Draw(img)
            font_name = ImageFont.truetype("Assets/b.ttc", 90) # フォントとサイズを指定する
            draw.text((1820, 300), name, fill=("white"), font=font_name)

            wrap_list = textwrap.wrap(comment, 22)  
            font_comment = ImageFont.truetype("Assets/c.otf", 90) # フォントとサイズを指定する
            line_counter = 0

            for line in wrap_list:
                y = line_counter*100+2734
                draw.multiline_text((313, y), line, fill=("black"), font=font_comment)
                line_counter = line_counter +1

            filename = 'line_followup.txt'  # 読み込むファイル名を指定する

# ファイルを読み込んで、文章全体を1つの変数に格納する
            with open(filename) as file:
                line_text = file.read()

            line_text = line_text.format(name)

            # 画像を保存する
            img.save("result.jpg", quality=100)
            with open("result.jpg", "rb") as file:
                btn = st.download_button(
                label="画像をダウンロード",
                data=file,
                file_name="comment_"+name+".jpg",
                mime="image/ipg"
            )
            
            st.image("result.jpg")
            st.code('', line_text)

        else:
            st.warning('コメントと名前を記入してから実行してください！', icon="⚠️")