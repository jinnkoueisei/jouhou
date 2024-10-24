# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('足し算します。')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示

# スライダーを作成し、値を選択
number1= st.slider('好きな数字を選んでください', 0, 1000000)
number2 = st.slider('好きな数字を選んでください', 0, 1000000)

number3=number1+number2

st.info(f'🔢 「{number1}」と「{number2}」を足すと「{number3}」になります。 🔢')  # 2進数の表示をハイライト
