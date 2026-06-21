# Chapter 02. OpenAI GPT API 사용해보기

## 학습 목표

이번 장에서는 OpenAI Python SDK를 이용하여 GPT API를 호출하고 응답을 받아보는 실습을 진행하였다.

AI Agent를 개발하기 위해서는 먼저 LLM과 직접 통신하는 방법을 이해해야 한다.

---

# 실습 내용

## 1. OpenAI 라이브러리 설치

```bash
pip install openai
pip install python-dotenv
```

### 사용 목적

* openai : GPT API 호출
* python-dotenv : 환경변수 관리

---

## 2. API Key 관리

### .env 파일 생성

```env
OPEN_API_KEY=sk-xxxxxxxxxxxxxxxx
```

### 환경변수 로드

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")
```

### 왜 환경변수로 관리할까?

API Key를 코드에 직접 작성하면 다음과 같은 문제가 발생한다.

* GitHub에 업로드될 위험
* API Key 유출 가능성
* 협업 시 관리 어려움

따라서 실제 프로젝트에서는 .env 파일을 사용하는 것이 일반적이다.

---

## 3. OpenAI Client 생성

```python
from openai import OpenAI

client = OpenAI(api_key=api_key)
```

### 역할

OpenAI 서버와 통신하기 위한 객체를 생성한다.

이후 모든 GPT 호출은 client 객체를 통해 수행한다.

---

# GPT API 호출

## 전체 코드

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "2022년 월드컵 우승 팀은 어디야?"},
    ]
)

print(response)
print(response.choices[0].message.content)
```

---

# 코드 분석

## model

```python
model="gpt-4o"
```

사용할 LLM 모델을 지정한다.

이번 실습에서는 GPT-4o를 사용하였다.

### 내가 이해한 내용

같은 질문을 하더라도 어떤 모델을 사용하느냐에 따라

* 응답 품질
* 응답 속도
* 비용

이 달라질 수 있다.

---

## temperature

```python
temperature=0.1
```

응답의 창의성을 조절하는 파라미터이다.

### 특징

| 값         | 특징       |
| --------- | -------- |
| 0.0       | 가장 일관적   |
| 0.1 ~ 0.3 | 사실 기반 답변 |
| 0.7       | 일반적인 대화  |
| 1.0 이상    | 창의적 생성   |

### 내가 이해한 내용

temperature가 낮을수록 같은 질문에 대해 비슷한 답변을 생성한다.

AI Agent나 업무 자동화에서는 보통 낮은 값을 사용할 것 같다.

---

## messages

```python
messages=[
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":"2022년 월드컵 우승 팀은 어디야?"}
]
```

대화 내용을 전달하는 부분이다.

---

### system 역할

```python
{
    "role":"system",
    "content":"You are a helpful assistant."
}
```

모델의 행동 방식을 정의한다.

예시)

```text
너는 정보보안 전문가다.
```

```text
너는 친절한 영어 선생님이다.
```

---

### user 역할

```python
{
    "role":"user",
    "content":"2022년 월드컵 우승 팀은 어디야?"
}
```

사용자의 질문을 전달한다.

---

### assistant 역할

실습에서는 사용하지 않았지만,

이전 대화 내용을 전달할 때 사용된다.

예시)

```python
[
    {"role":"user","content":"안녕"},
    {"role":"assistant","content":"안녕하세요."},
    {"role":"user","content":"내 이름은 세영이야."}
]
```

### 내가 이해한 내용

ChatGPT도 내부적으로는 messages 형식으로 대화가 관리될 것 같다.

---

# 응답 확인

## 전체 응답 출력

```python
print(response)
```

응답 객체 전체를 확인할 수 있다.

포함 정보

* 모델명
* 응답 내용
* 토큰 사용량
* 응답 ID

등

---

## 응답 내용만 출력

```python
print(response.choices[0].message.content)
```

실제 답변만 추출하는 코드이다.

예상 출력

```text
2022년 FIFA 월드컵 우승 팀은 아르헨티나입니다.
```

---

# 응답 객체 구조 이해

응답 구조를 단순화하면 다음과 같다.

```text
response
 └── choices
      └── [0]
           └── message
                └── content
```

실제 답변은

```python
response.choices[0].message.content
```

에 저장되어 있다.

---

# 이번 실습에서 배운 점

1. OpenAI API를 사용하여 GPT와 직접 통신할 수 있다.

2. API Key는 반드시 환경변수로 관리해야 한다.

3. GPT는 messages 구조를 통해 대화를 이해한다.

4. system 메시지를 활용하여 모델의 역할을 설정할 수 있다.

5. temperature를 통해 응답 스타일을 제어할 수 있다.

---

# 느낀 점

ChatGPT를 웹에서 사용하는 것과 GPT API를 사용하는 것은 다르다고 생각했는데, 실제로는 ChatGPT의 동작 원리를 코드로 직접 호출하는 것에 가깝다는 것을 알게 되었다.

이번 장에서는 단순히 질문과 답변을 주고받는 수준이었지만, 이후 Tool Calling, RAG, LangChain 등을 활용하면 GPT가 단순한 챗봇을 넘어 실제 업무를 수행하는 AI Agent로 발전할 수 있을 것 같다.
