contract ReputationScoring:

    def __init__(self):
        self.scores = {}

    def record_action(self, user, action_type, weight):
        if user not in self.scores:
            self.scores[user] = 0

        if action_type == "positive":
            self.scores[user] += weight * 2
        elif action_type == "negative":
            self.scores[user] -= weight * 3
        else:
            self.scores[user] += weight

        return self.scores[user]

    def get_score(self, user):
        return self.scores.get(user, 0)
