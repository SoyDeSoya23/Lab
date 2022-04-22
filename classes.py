class Television:
    """
    Class which represents the Television objects.
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor which sets the default attributes for Television.
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Method that changes the on/off state of the Television.
        """
        if self.__status is False:
            self.__status: bool = True
        else:
            self.__status: bool = False

    def channel_up(self) -> None:
        """
        Method that increases the Television's channel value by one.
        Resets to the minimum channel value if called when the current channel
        is equal to the maximum channel value.
        """
        if self.__status is True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel: int = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method that decreases the Television's channel value by one.
        Resets to the maximum channel value if called when the current channel
        is equal to the minimum channel value.
        """
        if self.__status is True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel: int = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that increases the Television's volume value by one.
        Does not increase further if called when the current volume
        is equal to the maximum volume value.
        """
        if self.__status is True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method that decreases the Television's volume value by one.
        Does not decrease further if called when the current volume
        is equal to the minimum volume value.
        """
        if self.__status is True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method that returns a string describing all three attributes of a Television.
        :return: A Television's power status, channel, and volume attributes.
        """
        return f'TV status: is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
