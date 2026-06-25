from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.9,
        messages=messages
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
]

while True:
    user_input=input("사용자: ")

    if user_input=="exit":
        break

    messages.append({"role": "user", "content": user_input})
    ai_response = get_ai_response(messages)
    messages.append({"role":"assistant", "content": ai_response})
    print("AI: "+ai_response)

# 출력 예시
"""
사용자: 미국에서 인기있는 연예인은 누구야?
AI: 미국에서 인기 있는 연예인들은 여러 분야에서 활동하고 있으며, 특정 시기에 따라서 변할 수 있지만, 현재로서는 다음과 같은 연예인들이 인기를 얻고 있습니다:

1. **Taylor Swift** - 가수 겸 작곡가로, 특히 최근 앨범과 투어로 큰 주목을 받고 있습니다.
2. **Beyoncé** - 세계적인 팝 스타로, 음악뿐만 아니라 패션과 사회 운동에서도 큰 영향력을 미치고 있습니다.
3. **Dwayne "The Rock" Johnson** - 배우이자 프로레슬러로, 다양한 영화와 TV 프로그램에서 활약하고 있습니다.
4. **Kim Kardashian** - 미디어 인플루언서이자 사업가로, 소셜 미디어에서 강력한 존재감을 발휘하고 있습니다.
5. **Billie Eilish** - 젊은 세대의 아이콘으로, 독특한 음악 스타일과 패션으로 주목받고 있습니다.

이 외에도 많은 스타들이 다양한 분야에서 활발히 활동하고 있습니다. 특정한 분야나 선호하는 장르가 있다면, 더 구체적인 추천을 드릴 수 있어요!

사용자: 한국은?
AI: 한국에서도 많은 인기 연예인들이 활동하고 있습니다. 최근 몇 년 간 주목받고 있는 몇몇 연예인들을 소개할게요:

1. **BTS (방탄소년단)** - 글로벌 슈퍼스타로, K-pop을 세계에 알리는 데 큰 기여를 했습니다.
2. **BLACKPINK** - 세계적으로 유명한 걸그룹으로, 음악과 패션 모두에서 큰 인기를 얻고 있습니다.
3. **IU (아이유)** - 가수이자 배우로서 여러 히트곡과 드라마에서 활약하며 많은 팬들에게 사랑받고 있습니다.
4. **Seo Ye-ji (서예지)** - 최근 드라마에서의 연기로 주목받고 있는 배우입니다.
5. **Park Seo-joon (박서준)** - 다양한 드라마와 영화에서 활발히 활동하며 인기를 얻고 있는 배우입니다.

이 외에도 많은 뛰어난 연예인들이 있으며, 정기적으로 새로운 스타가 등장하고 있습니다. 특정 분야나 장르에서 더 많은 정보를 원하시면 말씀해 주세요!
사용자: exit
"""