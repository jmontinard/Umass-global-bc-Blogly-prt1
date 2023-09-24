"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



"""Models for Blogly."""

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    first_name = db.Column(db.Text,
                     nullable=False)
    last_name = db.Column(db.Text,
                     nullable=False)
    image_url = db.Column(db.Text,
                     nullable= False,
                     default='https://images.unsplash.com/photo-1525357816819-392d2380d821?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80')

    # @property
    # def __repr__(self):
    #     u = self
    #     return f"<User id={u.id} firstname={u.first_name} lastname={u.last_name} imgUrl ={u.image_url} >"
    #     # see if you need classmethod?z

    @property    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"


