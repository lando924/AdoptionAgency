"""Models for pet agency"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Potential Pets for Adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text,
                     nullable=True,
                     default="data:image/png;base64,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")
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def __repr__(self):
        """Show pet name, species, availability"""
        return f'<{self.name} the {self.species} availability: {self.available}'