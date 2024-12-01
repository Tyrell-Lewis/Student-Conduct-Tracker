from abc import ABC, abstractmethod

# creating Karma Interface
class KarmaInterface(ABC):
   
   @abstractmethod
   def attach(self):
      return

   @abstractmethod
   def detach(self):
      return

   @abstractmethod
   def notifyStudents(self):
      return