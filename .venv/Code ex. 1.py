def Shift(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    concatenated = s + s
    return goal in concatenated
print(Shift("abcde", "cdeab"))