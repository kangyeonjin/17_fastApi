from pydantic import BaseModel
from typing_extensions import Optional

# request 받거나, response를 받을때
# 기본 형식을 만들어 놓을 수 있다.
class StudentBase(BaseModel):
    name: str
    launch_menu: bool
    nickname: Optional[str] = None
    description: Optional[str] = None

# SqlAlchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조정의
# Pydantic 모델 : API 요청과 응답을 위한 데이터 구조정의 

# request 요청 모델
class StudnetCreate(StudentBase):
    pass

# response 응답 모델
class StudnetResponse(StudentBase):
    id : int
    
# 업데이트할때 사용되는 request모델
class StudnetUpdate(BaseModel):
    name: Optional[str] = None
    launch_menu: Optional[bool] = None
    nickname: Optional[str] = None
    description: Optional[str] = None