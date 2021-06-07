import functools
import random
import string

def random_word(goal):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(len(goal)))

def distance(goal, current):
    current = map(ord, current)
    goal = map(ord, goal)
    return sum(min((c1 - c2) % 26, (c2 - c1) % 26) for c1, c2 in zip(current, goal))

def mutate(current):
    index = random.randrange(len(current))
    newchar = chr(ord('a') + (ord(current[index]) + [-1,1][random.randrange(2)] - ord('a')) % 26)
    return current[:index] + newchar + current[index + 1:]

def evolve(goal, size, generations):
    population = [random_word(goal) for _ in range(size // 10)]

    for index, _ in enumerate(range(generations)):
        for current in population[:size // 10]:
            for _ in range((size - (size // 10)) // 10):
                population.append(mutate(current))

        value = functools.partial(distance, goal)
        population = sorted(population, key=value)[:size // 10]

        print(population[0])

        if population[0] == goal:
            print(f"Evolution has found its way in iteration {index}!")
            return index

    print(f"Evolution created {population[0]} as the best.")


def main():
    goal = "hansjepansjekevertjeheefteengroteappel"
    size = 100  # % 100 == 0
    generations = 300

    print(sum(evolve(goal, size, generations) for _ in range(100)) // 100)

if __name__ == '__main__':
    main()
