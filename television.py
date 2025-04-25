class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = self.__volume

    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            elif self.__muted == True:
                self.__muted = False
                self.__volume = self.__prev_volume


    def channel_up(self):
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status == True:
            self.__muted = False
            self.__volume = self.__prev_volume + 1
            self.__prev_volume = self.__volume
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        if self.__status == True:
            self.__muted = False
            self.__volume = self.__prev_volume - 1
            self.__prev_volume = self.__volume
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

