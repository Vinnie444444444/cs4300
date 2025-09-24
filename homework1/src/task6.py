def count_words(file_path):
    #reads a given gile and return the amount of words it contains
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    return len(words)

if __name__ == "__main__":
    print("Word count:", count_words("src/task6_read_me.txt"))

