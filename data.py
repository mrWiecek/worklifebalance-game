import random

from events import *


class Data(object):

    def __init__(self):
        self.random_events = []
        self.opportunities = []

        self.random_events_titles = {('work', 'poz', 'long'): ["You got a rise!", "You got compensation for an accident at work"],
                                     ('work', 'neg', 'long'): ["You have child!", "Your company makes cuts!"],
                                     ('work', 'poz', 'short'): ["You won a lottery!", "You've got bonus!"],
                                     ('work', 'neg', 'short'): ["You got robbed!", "You've missed deadline and have to pay."],
                                     ('life', 'poz', 'long'): ["You met love of your life!", "You've bought a pet you love!"],
                                     ('life', 'neg', 'long'): ["You lost your leg while skiing!", "Your love dumped you!"],
                                     ('life', 'poz', 'short'): ["You won a trip!", "Your friends made you BD party surprise."],
                                     ('life', 'neg', 'short'): ["You have to work extra hours", "You think nobody likes you."]
                                     }

        self.opportunities_titles = {('work', 'poz', 'long'): ["New job offer!", "You've got new passive income opportunity!"],
                                     ('work', 'poz', 'short'): ["Do you buy lottery ticket?", "Your friend offers you odd job"],
                                     ('life', 'poz', 'long'): ["Will you help friend in need?", "Do you decide to exercise?"],
                                     ('life', 'poz', 'short'): ["Do you want to get a massage?", "Do you go to your favorite band concert?"],
                                     }

        self.generate_events(self.random_events_titles)
        self.generate_events(self.opportunities_titles)

    def add_event(self, event):
        if isinstance(event, RandomEvent):
            self.random_events.append(event)
        elif isinstance(event, Opportunities):
            self.opportunities.append(event)
        else:
            print('Incorrect object.')

    def generate_events(self, titles):
        for i in range(3):
            for k, v in titles.items():
                title = random.choice(v)
                value = random.randint(5, 15)
                duration = random.randint(1, 5)
                category = k[0]

                if k[0] == 'work':
                    value *= 10000
                if k[1] == 'neg':
                    value = -value
                if k[2] == 'long':
                    duration *= 10

                if titles == self.random_events_titles:
                    self.random_events.append(RandomEvent(title, value, duration, category))
                else:
                    self.opportunities.append(Opportunities(title, value, duration, category))

    def random_event(self, rand=True):
        if rand:
            return random.choice(self.random_events)
        else:
            return random.choice(self.opportunities)

