'''
FaseAPI

-한번에 설치
pip install fastapi[all]

fastapi 관련패키지들, uvicorn

-부분적으로 설치 설치
pip install fastapi
pip install unicorn

'''

#main.py :프로젝트 전체적인 환경을 설정하는 파일

from fastapi import FastAPI

app =  FastAPI()

@app.get('/')
async def root():
    return{"message" : "hello fastapi"}

#uvicorn main: app --reload

# main => main.py파일의 이름을 의미함
# app => main.py파일에서 fastapi()객체를 가지고잇는 app객체를 의미

#--reload :파일에 변화가 생기면 재시작하겠다는 옵션
