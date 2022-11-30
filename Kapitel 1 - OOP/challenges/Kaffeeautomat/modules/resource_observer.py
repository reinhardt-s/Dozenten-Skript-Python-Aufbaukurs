class ResourceObserver:
    """Interface für die Observer"""

    def update(self, caller):
        """
        Wird vom Subject aufgerufen, sofern ein beobachteter Zustand sich ändert

        :param caller: Der Observer.
        """
        pass
