
class Player(object):
    """
    Can have multiple active events.
    """

    def __init__(self, name, data):
        self.name = name
        self.data = data

        self.life_points = 0
        self.work_points = 0

        self.money = 100000
        self.round = 0

        self.active_events = []
        self.options = []

        self.choices = {}

    def __str__(self):
        return f'{self.name}'

    def add_event(self, event):
        self.active_events.append(event)

    def remove_event(self, event):
        self.active_events.remove(event)

    def create_options(self):
        while len(self.options) != 3:
            option = self.data.random_event(rand=False)
            if option not in self.options:
                self.options.append(option)
        self.choices = {idx+1: opt for idx, opt in enumerate(self.options)}

    def clear_options(self):
        self.options = []

    def make_choice(self):
        while True:
            try:
                choice = input('Make choice: ')
                self.add_event(self.choices[int(choice)])
                break
            except:
                print('Invalid input. Type 1, 2 or 3.')

    def update_player(self):
        """
        Update all player stats
        """

        self.update_money()
        self.update_points()
        self.update_event_duration()
        self.round += 1

    def update_points(self):
        life_change = 0
        for event in self.active_events:
            if event.category == 'life':
                life_change += event.value
        self.work_points = int(self.money*0.0001)
        self.life_points += life_change

    def update_event_duration(self):
        for event in self.active_events:
            if event.duration is None:
                continue
            elif event.duration <= 0:
                self.remove_event(event)
            else:
                event.decrease_duration()

    def update_money(self):
        change = 0
        for event in self.active_events:
            if event.category == 'work':
                change += event.value
        self.money += change

    def status(self):
        print(f'Round #{str(self.round)}', end='\n\n')
        print(f"You've got {self.work_points} work points and {self.life_points} life points.", end='\n\n')
        print(f'You have ${self.money} in a bank.\n')
        print('Your active events are:')
        [print(ev) for ev in self.active_events]
        print('\nYour list of options:')
        [print(f'{k}: {v}') for k, v in self.choices.items()]


    def action(self):
        self.create_options()
        self.status()
        self.make_choice()
        self.clear_options()
        input(f"next round ->")
        print('\n'*20)
