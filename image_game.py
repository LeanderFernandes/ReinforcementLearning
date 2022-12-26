import random

def main(episodes):
    files = [1, 2]

    score = 0

    for _ in range(episodes):
        while True:
            target = random.choice(files)
            choice = int(input("What is the file, 1 or 2: "))
            if choice == target:
                score += 10
            else:
                score -= 10
            break
        
        print(score)




main(5)