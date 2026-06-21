from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.9,
        messages=[
            {"role":"system", "content":"너는 사용자를 도와주는 상담사야."},
            {"role":"user", "content":user_input}
        ]
    )

    print("AI: "+response.choices[0].message.content)

# 출력 예시
 
# 사용자: 내 이름은 김똥개야
# AI: 안녕하세요, 김똥개님! 어떻게 도와드릴까요?
# 사용자: 내 이름이 뭐야?
# AI: 죄송하지만, 당신의 이름을 알 수 있는 정보는 없습니다. 당신이 원하는 이름을 말씀해 주시면 그에 맞춰 대화할 수 있어요!
