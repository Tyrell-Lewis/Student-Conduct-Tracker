from App.database import db
from sqlalchemy.ext.declarative import declarative_base
from .karmaInterface import KarmaInterface




class Karma(db.Model, KarmaInterface):

  __tablename__ = "karma"
  karmaID = db.Column(db.Integer, primary_key=True)
  points = db.Column(db.Float, nullable=False, default=0.0)
  academicPoints = db.Column(db.Float, nullable=False) # unwanted attribute- removing causes import errors
  accomplishmentPoints = db.Column(db.Float, nullable=False, default=0.0) # unwanted attribute- removing causes import errors
  incidentPoints = db.Column(db.Float, nullable=False, default=0.0) # unwanted attribute- removing causes import errors
  reviewsPoints = db.Column(db.Float, nullable=False, default=0.0) # unwanted attribute- removing causes import errors
  rank = db.Column(db.Integer, nullable=False, default=-99)
  studentID = db.Column(db.Integer, db.ForeignKey('student.ID',
                                                  use_alter=True))

''' Removing unwanted attributes causes errors with importing wsgi.py
  def __init__(self, points, reviewsPoints, rank, studentID):
    self.points = points
    self.reviewsPoints = reviewsPoints
    self.rank = rank
    self.studentID = studentID
'''
def __init__(self, points, academicPoints, accomplishmentPoints,
               reviewsPoints, incidentPoints, rank, studentID):
    self.points = points
    self.academicPoints = academicPoints
    self.accomplishmentPoints = accomplishmentPoints
    self.reviewsPoints = reviewsPoints
    self.incidentPoints = incidentPoints
    self.rank = rank
    self.studentID = studentID
    
    
def calculate_total_points(self):
    print("Calculating total points using only review points...")

    # Multiplier for review points
    review_multiplier = 1.0  # Complete weighting of karma depends on reviews, to be altered to include diversity of reviewers

    # Calculation
    print("Review Points:", self.reviewsPoints) 
    print("Review Points Multiplier:", review_multiplier, "giving",
          self.reviewsPoints, "*", review_multiplier, "=", self.reviewsPoints * review_multiplier)

    self.points = round(self.reviewsPoints * review_multiplier, 2)

    # Display the total points calculation
    print("Total Karma Points:", self.points)


def to_json(self):
    return {
        "karmaID": self.karmaID,
        "score": self.points,
        "academicPoints": self.academicPoints,
        "accomplishmentPoints": self.accomplishmentPoints,
        "reviewPoints": self.reviewsPoints,
        "incidentPoints": self.incidentPoints,
        "rank": self.rank,
        "studentID": self.studentID
    }


#added
def attach(self, Student):
    self.studentID = Student.studentID
    return


def detach(self):
    self.studentID = ""
    return


def notify(self):
    """Notify all attached students"""
    return "Karma has been updated"


''' Methods including unwanted attributes in karma calculations, simplified calculation given above

  def __init__(self, points, academicPoints, accomplishmentPoints,
               reviewsPoints, incidentPoints, rank, studentID):
    self.points = points
    self.academicPoints = academicPoints
    self.accomplishmentPoints = accomplishmentPoints
    self.reviewsPoints = reviewsPoints
    self.incidentPoints = incidentPoints
    self.rank = rank
    self.studentID = studentID

  
  def calculate_total_points(self):
    # only review points
    if self.academicPoints == 0 and self.accomplishmentPoints == 0 and self.reviewsPoints != 0:
      print("Calculating total points with only review points...")
      print("Review Points:", self.academicPoints)
      print("Review Points Multiplier: 0.725 giving ", self.reviewsPoints,
            "* 0.725 = ", self.reviewsPoints * 0.725)
      self.points = round(
          ((self.academicPoints * 0.175) + (self.accomplishmentPoints * 0.1) +
           (self.reviewsPoints * 0.725)) - (self.incidentPoints * 0.3), 2)
      print("Total Points:", self.academicPoints * 0.725, ' + ',
      self.accomplishmentPoints, ' + ', self.reviewsPoints, ' - ',
      self.incidentPoints * 0.3, ' = ', self.points)
    # no review and accomplishment points, only academic points
    elif self.academicPoints != 0 and self.accomplishmentPoints == 0 and self.reviewsPoints == 0:
      print("Calculating total points with only academic points...")
      print("Academic Points:", self.academicPoints)
      print("Academic Points Multiplier: 0.725 giving ", self.academicPoints,
            "* 0.725 = ", self.academicPoints * 0.725)
      self.points = round(
          ((self.academicPoints * 0.725) + (self.accomplishmentPoints * 0.1) +
           (self.reviewsPoints * 0.175)) - (self.incidentPoints * 0.3), 2)
      print("Total Points:", self.academicPoints * 0.725, ' + ',
      self.accomplishmentPoints, ' + ', self.reviewsPoints, ' - ',
      self.incidentPoints * 0.3, ' = ', self.points)
    # no review points
    elif self.academicPoints != 0 and self.accomplishmentPoints != 0 and self.reviewsPoints == 0:
      print("Calculating total points without review points...")
      print("Academic Points:", self.academicPoints)
      print("Academic Points Multiplier: 0.625 giving ", self.academicPoints,
            "* 0.625 = ", self.academicPoints * 0.625)
      print("Accomplishment Points:", self.accomplishmentPoints)
      print("Accomplishment Points Multiplier: 0.275 giving ",
            self.accomplishmentPoints, "* 0.275 = ",
            self.accomplishmentPoints * 0.275)
      self.points = round(
          ((self.academicPoints * 0.625) +
           (self.accomplishmentPoints * 0.275) +
           (self.reviewsPoints * 0.175)) - (self.incidentPoints * 0.3), 2)
      print("Total Points:", self.academicPoints * 0.625, ' + ',
      self.accomplishmentPoints * 0.275, ' + ', self.reviewsPoints, ' - ',
      self.incidentPoints * 0.3, ' = ', self.points)
    # no accomplishment points
    elif self.academicPoints != 0 and self.accomplishmentPoints == 0 and self.reviewsPoints != 0:
      print("Calculating total points without accomplishment points...")
      print("Academic Points:", self.academicPoints)
      print("Academic Points Multiplier: 0.5 giving ", self.academicPoints,
            "* 0.5 = ", self.academicPoints * 0.5)
      print("Reviews Points:", self.reviewsPoints)
      print("Reviews Points Multiplier: 0.4 giving ", self.reviewsPoints,
            "* 0.4 = ", self.reviewsPoints * 0.4)
      self.points = round(
          ((self.academicPoints * 0.5) + (self.accomplishmentPoints * 0.1) +
           (self.reviewsPoints * 0.4)) - (self.incidentPoints * 0.3), 2)
      print("Total Points:", self.academicPoints * 0.5, ' + ',
      self.accomplishmentPoints, ' + ', self.reviewsPoints * 0.4, ' - ',
      self.incidentPoints * 0.3, ' = ', self.points)
    # has all attributes
    elif self.academicPoints != 0 and self.accomplishmentPoints != 0 and self.reviewsPoints != 0:
      print("Calculating total points with all attributes...")
      print("Academic Points:", self.academicPoints)
      print("Academic Points Multiplier: 0.45 giving ", self.academicPoints,
            "* 0.45 = ", self.academicPoints * 0.45)
      print("Accomplishment Points:", self.accomplishmentPoints)
      print("Accomplishment Points Multiplier: 0.35 giving ",
            self.accomplishmentPoints, "* 0.35 = ",
            self.accomplishmentPoints * 0.35)
      print("Reviews Points:", self.reviewsPoints)
      print("Reviews Points Multiplier: 0.2 giving ", self.reviewsPoints,
            "* 0.2 = ", self.reviewsPoints * 0.2)
      self.points = round(
          ((self.academicPoints * 0.45) + (self.accomplishmentPoints * 0.35) +
           (self.reviewsPoints * 0.2)) - (self.incidentPoints * 0.3), 2)
      print("Total Points:", self.academicPoints * 0.45, ' + ',
            self.accomplishmentPoints * 0.35, ' + ', self.reviewsPoints * 0.2, ' - ',
            self.incidentPoints * 0.3, ' = ', self.points)
    else:
      self.points = 0
      print("No attributes found for karma calculation.")

'''


