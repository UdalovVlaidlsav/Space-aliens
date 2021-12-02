class Stats():
    """"Статистика игры"""

    def __init__(self):
        """"Инизализация статистики"""
        self.guns_left = 2
        self.reset_stats()
        self.lose_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        """"Статистика, которая меняется во время игры"""
        self.score = 0
