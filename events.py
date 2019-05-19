class Event(object):
    """
    Take effect on player status.
    """

    def __init__(self, title, value, duration, category):
        self.title = title
        self.value = value
        self.duration = duration
        self.category = category

    def __repr__(self):
        return f'{self.title:<45s}' + f" duration: {str(self.duration):<5s}" + f' {str(self.value):>5s}'

    def decrease_duration(self):
        self.duration -= 1


class RandomEvent(Event):
    
    def __init__(self, title, value, duration, category):
        super(RandomEvent, self).__init__(title, value, duration, category)


class Opportunities(Event):

    def __init__(self, title, value, duration, category):
        super(Opportunities, self).__init__(title, value, duration, category)

    # def __repr__(self):
    #     return f'{self.title:<45s}' + f" duration: {str(self.duration):<5s}" + f' ${str(self.value):>5s}'
