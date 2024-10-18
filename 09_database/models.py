from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

# String => 고정된길이 (길이제한)
# Text => 길이제한이 없다.

class Teacher(Base):
    __tablename__ = 'teachers'
    
    # 컬럼설정
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    is_active = Column(Boolean, default=True)
    description = Column(Text)
    
#student crud만들기
class Student(Base):
    __tablename__ = 'students'
    
    id= Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    launch_menu = Column(String(100))
    description = Column(Text)
    
    #관계 설정이 가능 한번해보세요