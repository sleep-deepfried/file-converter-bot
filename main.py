import random

word_list = ["apple", "banana", "orange", "grape", "kiwi", "lemon", "melon"]

secret_word = random.choice(word_list)

def wordle_game():
    attempts = 5
    guessed_letters = set()

    print("Chatbot: Welcome to Wordle! Try to guess the secret five-letter word.")
    print(f"Chatbot: You have {attempts} attempts.")

    while attempts > 0:
        user_guess = input("You: ").lower()

        # Check if the user's guess is valid
        if len(user_guess) != 5 or not user_guess.isalpha():
            print("Chatbot: Invalid guess. Please enter a five-letter word.")
            continue

        # Check if the user has already guessed the same letter before
        if user_guess in guessed_letters:
            print("Chatbot: You already guessed that word.")
            continue

        guessed_letters.add(user_guess)

        # Check if the user guessed the correct word
        if user_guess == secret_word:
            print(f"Chatbot: Congratulations! You guessed the word '{secret_word}' correctly!")
            break
        else:
            attempts -= 1
            print(f"Chatbot: Incorrect guess. You have {attempts} attempts remaining.")
    else:
        print(f"Chatbot: Sorry, you ran out of attempts. The secret word was '{secret_word}'.")


print("Chatbot: Hello! I'm a chatbot playing the Wordle game. Can you guess the word?")
while True:
    user_input = input("You: ").lower()
    if user_input in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    wordle_game()

