"""
gift exchange
list of coworkers
each gives gift each receives gift
no one gives to themselves
everyone must be matched
some are partners, and cannot gift to each other
"""

class Exchange():
    def __init__(self, coworkers: list, partners: dict) -> None:
        self.partners = partners # {teammate: teammate(partner)}
        self.coworkers = coworkers
        self.matched = {} # {giver: receiver} both are strings
    
    def match(self) -> None:
        if len(self.coworkers) < 2:
            print('Not enough coworkers to exchange gifts')
            return
        givers = self.coworkers.copy()
        receivers = self.coworkers.copy()
        givers = givers[1:] + self.coworkers[:1]
        for i in range(len(givers)):
            while self.partners.get(givers[i]) == receivers[i] or givers[i] == receivers[i]:
                receivers = receivers[1:] + receivers[:1]
        
        for i in range(len(givers)):
            self.matched[givers[i]] = receivers[i]


if __name__ == '__main__':
    coworkers = ['Bob', 'Charlie', 'David', 'Eve']
    partners = {'David': 'Eve', 'Eve': 'David'}
    exchange = Exchange(coworkers, partners)
    exchange.match()
    for giver, receiver in exchange.matched.items():
        print(f'{giver} gives to {receiver}')