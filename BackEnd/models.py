from sqlalchemy.orm import validates
from flask import jsonify

class MoodEntry(db.Model):
    __tablename__ = "moodentries"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_entry = db.Column(db.String, nullable=False)
    affirmation = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User Entry: '{self.user_entry}' returns '{self.affirmation}'"
    
    def to_dict(self):
        return{"id": self.id, "user_entry": self.user_entry, "affirmation": self.affirmation}
    
    @validates("user_entry")
    def validate_entry(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Entry must be a string.")
        if not len(value.strip()) > 0:
            raise ValueError("Entry must exist.")
        return value
    
    @validates("affirmation")
    def validate_affirmation(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Affirmation must be a string.")
        cleaned_value = value.strip()
        if not len(cleaned_value) > 0:
            raise ValueError("Affirmation must not be empty.")
        return cleaned_value

