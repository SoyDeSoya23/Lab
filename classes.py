# TODO: account for invalid input data
# TODO: Find where to implement exception handling
# TODO: Create an intuitive GUI

class Television:
    """
    Class which represents the Television objects.
    """

    def __init__(self, c_min=0, c_max=3, v_min=0, v_max=2) -> None:
        """
        Constructor which sets the default attributes for Television.
        :param c_min: Minimum TV channel
        :param c_max: Maximum TV channel
        :param v_min: Minimum TV volume
        :param v_max: Maximum TV volume
        """
        self.__MIN_CHANNEL: int = c_min
        self.__MAX_CHANNEL: int = c_max

        self.__MIN_VOLUME: int = v_min
        self.__MAX_VOLUME: int = v_max

        self.__channel: int = c_min
        self.__volume: int = v_min
        self.__status: bool = False

    def power(self) -> None:
        """
        Method that changes the on/off state of the Television.
        """
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method that increases the Television's channel value by one.
        Resets to the minimum channel value if called when the current channel
        is equal to the maximum channel value.
        """
        if self.__status is True:
            if self.__channel < self.__MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.__MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method that decreases the Television's channel value by one.
        Resets to the maximum channel value if called when the current channel
        is equal to the minimum channel value.
        """
        if self.__status is True:
            if self.__channel > self.__MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.__MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that increases the Television's volume value by one.
        Does not increase further if called when the current volume
        is equal to the maximum volume value.
        """
        if self.__status is True:
            if self.__volume < self.__MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method that decreases the Television's volume value by one.
        Does not decrease further if called when the current volume
        is equal to the minimum volume value.
        """
        if self.__status is True:
            if self.__volume > self.__MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method that returns a string describing all three attributes of a Television.
        :return: A Television's power status, channel, and volume attributes.
        """
        return f'TV status: is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
