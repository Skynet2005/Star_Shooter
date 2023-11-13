# managers/leaderboard_manager.py
import json

class LeaderboardManager:
    def __init__(self, filename):
        self.filename = filename
        self.leaderboard = self.load_leaderboard()

    def load_leaderboard(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_leaderboard(self, name, score):
        self.leaderboard.append({"name": name, "score": score})
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]  # Keep only top 10 scores

    def save_leaderboard(self):
        with open(self.filename, 'w') as f:
            json.dump(self.leaderboard, f)
            
    def get_leaderboard(self):
        return self.leaderboard
