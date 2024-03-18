from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    home_team = Column(String)
    away_team = Column(String)
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))


class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rounds = relationship('Round', back_populates='tournament')
    teams = relationship('Team', secondary='tournament_teams')


class Round(Base):
    __tablename__ = 'rounds'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    tournament = relationship('Tournament', back_populates='rounds')
    matches = relationship('Match', back_populates='round')


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)



engine = create_engine('sqlite:///base.db')
Base.metadata.create_all(engine)