from datetime import datetime
from app import db
from enum import Enum

class TaskStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)
    status = db.Column(db.Enum(TaskStatus), nullable = False, default = TaskStatus.PENDING)
    due_date = db.Column(db.DateTime, nullable = True)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now())
    updated_at = db.Column(db.DateTime, nullable = False, default = datetime.now(), onupdate = datetime.now())

    def __repr__(self):
        return f"<Task: {self.title}>"
    
    def mark_completed(self):
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()

    # You can add other methods here as well
    def mark_in_progress(self):
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now()

    def reset_to_pending(self):
        self.status = TaskStatus.PENDING
        self.updated_at = datetime.now()