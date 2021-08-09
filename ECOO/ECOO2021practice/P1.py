n = int(input())

def run(n):
    if n<3:
        return "Rocket!"
    if n>7:
        return "Tootsie Roll!"
    else:
        return "NO"

print(run(n))