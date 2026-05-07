# Name: Jaleelah Bachou
# Assignment: Sprint 1 Implementation
# Purpose: Convert coin sentences into dollar amounts

coin_values = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}

sentence = input("Enter a coin sentence: ")
words = sentence.split()

total = 0

for i in range(len(words) - 1):
    if words[i].isdigit():
        quantity = int(words[i])
        coin = words[i + 1].lower()

        if coin in coin_values:
            total += quantity * coin_values[coin]

print(f"{total:.2f}")
