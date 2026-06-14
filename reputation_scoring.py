# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class ReputationScoring(gl.Contract):

    scores: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def record_action(self, user: Address, value: u256) -> None:
        current = self.scores.get(user, u256(0))
        self.scores[user] = current + value

    @gl.public.view
    def get_score(self, user: Address) -> u256:
        return self.scores.get(user, u256(0))
