import uuid
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.String(36), primary_key=True)
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthday = sa.Column(sa.Integer)
	growth = sa.Column(sa.Integer)

def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def request_data():
	print("Привет я хочу записать твои данные: ")
	first_name = input("Введи свое имя: ")
	last_name = input("Теперь фамилию: ")
	gender = input("Пол (м/ж): ") 
	email = input("Адрес электронной почты: ")
	birthday = input("Дата рождения(дд.мм.гг.): ") 
	growth =input("Ваш рост(см): ")
	user_id = str(uuid.uuid4())
	user = User(
		id = user_id,
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthday = birthday,
		growth = growth
	)
	return user

def main():
    
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Ваши данные сохранены!")

if __name__ == "__main__":
    main()