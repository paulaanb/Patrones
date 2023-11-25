from abc import ABC, abstractmethod

 class Component(ABC):
     @abstractmethod
     def tamaño(self):
         pass