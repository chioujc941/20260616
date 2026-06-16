import google.generativeai as genai
import os
api_keys = os.getenv('GEMINI_KEY')
genai.configure(api_key=api_keys)

# 初始化時就定義好它是誰
ai_persona = "你是一個說話優雅的英國管家,叫作阿吉。請稱呼使用者為『主人』。"
model = genai.GenerativeModel(
model_name='gemini-flash-latest',
system_instruction=ai_persona
)
response = model.generate_content("幫我泡杯茶。")
print(response.text)
