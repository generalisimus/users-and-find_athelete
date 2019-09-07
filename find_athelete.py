import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_ = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Atlet(Base):
	__tablename__ = "user_atlet"
	id = sa.Column(sa.Integer, primary_key=True)
	age = sa.Column(sa.Integer)
	birthdate = sa.Column(sa.Integer)
	gender = sa.Column(sa.Text)
	height = sa.Column(sa.Integer)
	name = sa.Column(sa.Text)
	weight = sa.Column(sa.Integer)
	gold_medals = sa.Column(sa.Integer)
	silver_medals = sa.Column(sa.Integer)
	bronze_medals = sa.Column(sa.Integer)
	total_medals = sa.Column(sa.Integer)
	sport = sa.Column(sa.Text)
	country =sa.Column(sa.Text)

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
	engine = sa.create_engine(DB_)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def request_date():
	print("Поиск нужных спортсменов")
	_id = input("Введите идентификатор спортсмена: ")
	return int(_id)

def convert(date_str):
    parts = date_str.split("-")
    date_parts = map(int, parts)
    date = datetime.date(*date_parts)
    return date

def birthday(usesr, session, min_dist = None, atlete_id_=None,atlete_bd=None):
	atlete_list = session.query(Atlete).all()
	atlete_id = {}
	for atlete in atlete_list:
		bd = convert(athlete.birthdate)
		atlete_id[atlete.id] = bd

	user_bd = convert(user.birthdate)
	for id_, value in athlete_id.items():
		dist = abs(user_bd - bd)
		if not min_dist or dist < min_dist:
			min_dist = dist
			atlete_id = id_
			athlete_bd = bd
	return athlete_id, athlete_bd


def height(user, session, min_dist = None, athlete_id = None, athlete_height = None):
	atlete_list = session.query(Atlet).filter(Atlet.height != None).all()
	atlete_height = {athlete.id: athlete.height for athlete in athlete_list}

	user_height = user.height

	for id_, value in athlete_height.items():
		dist = abs(user_height - height)
		if not min_dist or dist < min_dist:
			min_dist = dist
			athlete_id = id_
			athlete_height = height

	return athlete_id, athlete_height

def main():
	session = connect_db()
	user_id = request_date()
	user = session.query(User).filter(User.id == user_id).first()
	if not user:
		print("Нет такого!")
	else:
		bd_athlete, bd = birthday(user, session)
		height_athlete, height = height(user, session)
		print(f'По дате рождения подходит спортсмен:({bd_athlete} дата рождения{bd}')
		print(f'По росту подходит спортсмен:{height_athlete},его рост{height}')

if __name__ == "__main__":
    main()        