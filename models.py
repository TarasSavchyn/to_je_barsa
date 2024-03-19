import os
import dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    league_points = Column(Integer)


# class Game(Base):
#     __tablename__ = "games"
#     id = Column(Integer, primary_key=True)
#     home_team_id = Column(Integer, ForeignKey("teams.id"))
#     away_team_id = Column(Integer, ForeignKey("teams.id"))
#     home_team = relationship("Team", foreign_keys=[home_team_id])
#     away_team = relationship("Team", foreign_keys=[away_team_id])
#     home_goals = Column(Integer)
#     away_goals = Column(Integer)


class League(Base):
    __tablename__ = "leagues"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teams = relationship("Team", secondary="league_teams")


class Cup(Base):
    __tablename__ = "cups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teams = relationship("Team", secondary="cup_teams")


engine = create_engine("sqlite:///base.db")
Base.metadata.create_all(engine)
