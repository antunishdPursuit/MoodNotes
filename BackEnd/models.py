from sqlalchemy.orm import validates
from flask import jsonify

class MoodEntry(db.Model):
    __tablename__ = "moodentries"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_entry = db.Column(db.String, nullable=False)
    affirmation = db.column(db.String, nullable=False)

    def __repr__(self):
        return f"User Entry: {self.user_entry} returns '{self.affirmation}'"
    
    def to_dict(self):
        return{"id": self.id, "user_entry": self.user_entry, "affirmation": self.affirmation}