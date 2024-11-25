from typing import List, Dict
from .student import Student
from .karma import Karma 

class karmaManager:
    observers: List[Student]
    karma_records: Dict[int, Karma]

    def __init__(self):
        """Initializes the KarmaManager with empty observers and karma records."""
        self.observers = []
        self.karma_records = {}

    def addObserver(self, observer: Student):
        if observer not in self.observers:
            self.observers.append(observer)
        
    def removeObserver(self, observer: Student):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self, studentId: int, newKarma: float):
        """Notifies all observers about a student's new karma points."""
        for observer in self.observers:
            observer.updateKarma(studentId, newKarma)

    def addKarmaRecord(self, studentId: int):
        """Adds a new karma record for the student."""
        if studentId not in self.karma_records:
            self.karma_records[studentId] = Karma()  # Initialize with a new Karma instance
            self.notifyObservers(studentId, 0) 

    def removeKarmaRecord(self, studentId: int):
        """Removes a karma record for a student."""
        if studentId in self.karma_records:
            del self.karma_records[studentId]  # Remove the karma record
            self.notifyObservers(studentId, 0)  # Notify observers with 0 karma since record is removed
            
    def calculateKarma(self, studentId):
        """Calculates karma points for a specific student by calling the Karma model's method."""
        if studentId in self.karma_records:
            karma_record = self.karma_records[studentId]
            karma_record.calculate_total_points() # Call the model's method to update points
            return karma_record.points  # Return the updated karma points
        return 0

    def updateKarmaRecord(self, studentId: int):
        newKarma = self.calculateKarma(studentId)
        self.notifyObservers(studentId, newKarma)

