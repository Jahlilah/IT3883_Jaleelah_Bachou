# Name: Jaleelah Bachou
# Assignment: Sprint 2 Corrected Implementation
# Purpose: Convert pseudo-English coin statements into dollar amounts

def calculate_coin_total(sentence):
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

    words = sentence.lower().split()
    total = 0

    for i in range(len(words) - 1):
        if words[i].isdigit():
            quantity = int(words[i])
            coin_name = words[i + 1]

            if coin_name in coin_values:
                total += quantity * coin_values[coin_name]

    return total


user_sentence = input("Enter a coin sentence: ")
final_amount = calculate_coin_total(user_sentence)

print(f"{final_amount:.2f}")
