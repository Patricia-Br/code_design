from abc import ABC, abstractmethod

# Classe de interface
class NotificationSender(ABC):
  @abstractmethod
  def send_notification(self, message: str) -> None: pass

# Definir a regra de construção
class EmailNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f"Email message: {message}")

# Definir a regra de construção
class SMSNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f"SMS message: {message}")

class Notificator:
  def __init__(self, notication_sender) -> None: 
    self.__notication_sender = notication_sender

  def send(self, message: NotificationSender) -> None:
    #validação de dados
    self.__notication_sender.send_notification(message)

obj = Notificator(EmailNotificationSender())
obj.send('Ola mundo')