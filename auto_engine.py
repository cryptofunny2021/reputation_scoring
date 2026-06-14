class AutoEngine:

    def calculate_score(self, reputation, tokens):
        return reputation * 2 + tokens

    def level(self, score):
        if score > 50:
            return "HIGH"
        elif score > 20:
            return "MEDIUM"
        else:
            return "LOW"
