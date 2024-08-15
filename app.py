import streamlit as st
import requests

st.title('動画から感情分析')

# ユーザーが動画ファイルをアップロード
uploaded_file = st.file_uploader("動画ファイルをアップロードしてください", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    if st.button('分析'):
        # Google ColabのAPIに動画を送信
        api_url = "http://127.0.0.1:5000"  # Colabのngrok URLを設定
        files = {'video': uploaded_file}
        response = requests.post(api_url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            st.write("=== 音声のテキスト化結果 ===")
            st.write(result['audio_text_summary'])

            st.write("=== 動画の表情からの感情分析結果 ===")
            st.write(result['emotion_summary_text'])
        else:
            st.write("エラーが発生しました。")
