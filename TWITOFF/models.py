from flask_sqlalchemy import SQLALchemy

DB = SQLAlchemy()

class User(DB.model):
    """Twitter users that we analyze"""
    id = DB.column(DB.BigInteger,primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """Tweets we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
        
