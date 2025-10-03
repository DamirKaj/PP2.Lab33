#1
class StringClass:
    def getString(self):
        return input("Enter a string: ")

    def printString(self, text):
        print(text.upper())

obj = StringClass()
s = obj.getString()
obj.printString(s)

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self, length):
        return length * length

s = Square()
print(s.area(5))  # 25

#3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self, length, width):
        return length * width


r = Rectangle()
print(r.area(5, 10))  # пример

#4
import math

class Point:
    def show(self, x, y):
        print(f"({x}, {y})")

    def move(self, x, y):
        return (x, y)

    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


p = Point()
p.show(2, 3)
new_coords = p.move(5, 7)
print("Moved to:", new_coords)
print("Distance:", p.dist(2, 3, 5, 7))

#5
class Account:
    def set_account(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance: {self.balance}")


a = Account()
a.set_account("Damir", 100)
a.deposit(50)
a.withdraw(30)
a.withdraw(200)

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 20]
primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)

#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    return (5/9)*(F-32)


# 3. Chickens and Rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if chickens*2 + rabbits*4 == numlegs:
            return chickens, rabbits
    return None, None


# 4. filter_prime from list
def filter_prime(lst):
    return [x for x in lst if is_prime(x)]


# 5. Permutations of string
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


# 6. Reverse words in sentence
def reverse_sentence(s):
    return ' '.join(s.split()[::-1])


# 7. has_33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False


# 8. spy_game
def spy_game(nums):
    code = [0,0,7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False


# 9. Volume of sphere
def volume_sphere(r):
    return (4/3)*math.pi*r**3


# 10. Unique elements from list
def unique_list(lst):
    new = []
    for i in lst:
        if i not in new:
            new.append(i)
    return new


# 11. Palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 12. Histogram
def histogram(lst):
    for n in lst:
        print('*'*n)


# 13. Guess the number game
def guess_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1,20)
    guessesTaken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guessesTaken += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
            break

#14
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_high_score(movie):
    return movie["imdb"] > 5.5

def high_score_movies(movies_list):
    result = []
    for m in movies_list:
        if m["imdb"] > 5.5:
            result.append(m)
    return result

def movies_by_category(movies_list, category):
    result = []
    for m in movies_list:
        if m["category"] == category:
            result.append(m)
    return result

def average_score(movies_list):
    total = 0
    for m in movies_list:
        total += m["imdb"]
    return total / len(movies_list)

def average_score_by_category(movies_list, category):
    filtered = []
    for m in movies_list:
        if m["category"] == category:
            filtered.append(m)
    total = 0
    for m in filtered:
        total += m["imdb"]
    return total / len(filtered)

print(is_high_score(movies[0]))
print(high_score_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_score(movies))
print(average_score_by_category(movies, "Romance"))
