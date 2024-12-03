from abc import ABC, abstractmethod

# creating Student Interface
class StudentInterface(ABC):
   
   @abstractmethod
   def update(self):
      """Update the karma points for the student"""
      return
