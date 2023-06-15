"""
implement a program that prompts the user for a str in English and then outputs 
the “emojized” version of that str, converting any codes (or aliases) therein to 
their corresponding emoji.
"""

# Dictionary mapping codes/aliases to emojis
emoji_map = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":smiley:": "😃",
    ":heart:": "❤️",
    ":star:": "⭐",
    ":fire:": "🔥",
    # Add more mappings as needed
}

def emojize_text(text):
    words = text.split()
    emojized_words = []

    for word in words:
        if word.lower() in emoji_map:
            emojized_words.append(emoji_map[word.lower()])
        else:
            emojized_words.append(word)

    emojized_text = " ".join(emojized_words)
    return emojized_text


def main():
    text = input("Enter a text: ")
    emojized_text = emojize_text(text)
    print(emojized_text)


if __name__ == "__main__":
    main()
