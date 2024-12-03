from abc import ABC, abstractmethod

# creating Karma Interface
class KarmaInterface():
   
   @abstractmethod
   def attach(self):
      """Attach a student to the Karma system"""
      pass

   @abstractmethod
   def detach(self):
      """Detach a student from the Karma system"""
      pass

   @abstractmethod
   def notify(self):
      """Notify all attached students"""
      pass
