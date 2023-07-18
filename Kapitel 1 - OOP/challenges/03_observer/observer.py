class Observer:
    """
    The Observer class is inherited by the class that should inform other classes about a change in state.
    """

    def __init__(self):
        self._observers = []

    def notify(self, modifier=None):
        """
        Notifies all subscribers about a change in state.

        :param modifier: Indicates who called notify.
        """
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """
        Adds subscribers.

        :param observer: The object to be added.
        """
        if observer not in self._observers:
            print(f"New subscriber: {observer.name}")
            self._observers.append(observer)

    def detach(self, observer):
        """
        Removes subscribers.

        :param observer: The object to be removed.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            # If it is not possible to remove the subscriber, we inform the caller with an exception.
            print(f"Observer {observer} could not be removed.")
