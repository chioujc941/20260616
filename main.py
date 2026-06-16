import google.generativeai as genai
import os
api_keys = os.getenv('GEMINI_KEY')
genai.configure(api_key=api_keys)

# ─── 1. 建立 FastAPI 網頁伺服器 ───
app = FastAPI()

# 瀏覽器用的 GET 請求
@app.get("/")
async def home_get():
    return {"status": "🤖 誰是臥底機器人 24 暢通運作中！"}

# 專門給 UptimeRobot 用的 HEAD 請求（完全不帶 request 參數，避免底層解析出錯）
@app.head("/")
async def home_head():
    return None  # HEAD 請求依照 HTTP 規範本來就不需要回傳內容，給個空值即可

# 初始化時就定義好它是誰
ai_persona = "你是一個說話優雅的英國管家,叫作阿吉。請稱呼使用者為『主人』。"
model = genai.GenerativeModel(
model_name='gemini-flash-latest',
system_instruction=ai_persona
)
response = model.generate_content("幫我泡杯茶。")
print(response.text)
