from abc import ABC,abstractmethod

# Subject interface
class Youtube(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass    

# Concrete subject
class YoutubeChannel(Youtube):
    def __init__(self):
        self._observers = []
        self._video_title = None

    def register_observer(self,observer):
        self._observers.append(observer)

    def remove_observer(self,observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def upload_video(self,video_title):
        self._video_title = video_title
        self.notify_observers()

    def get_video_title(self):
        return self._video_title

# Concrete observer
class Subscriber(Observer):
    def __init__(self,name):
        self._name = name

    
    def update(self,youtube_channel: YoutubeChannel):
        print(f'{self._name} received notification: New video uploaded - {youtube_channel.get_video_title()}')



if __name__ == '__main__':
    youtubechannel = YoutubeChannel()
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")
    youtubechannel.register_observer(subscriber1)
    youtubechannel.register_observer(subscriber2)
    youtubechannel.upload_video("How to Learn Python")