from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from db.engine import Base


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    league_points = Column(Integer)
    scored_goals_home = Column(Integer)
    scored_goals_away = Column(Integer)


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    game_date = Column(DateTime)
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    home_team_goals = Column(Integer)
    away_team_goals = Column(Integer)
    tour_id = Column(Integer, ForeignKey("tours.id"))
    tour = relationship("Tour")


class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, primary_key=True)
    tour_games = Column(String)


class League(Base):
    __tablename__ = "leagues"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teams = relationship("Team", secondary="league_teams")
    tours = relationship("Tour")
