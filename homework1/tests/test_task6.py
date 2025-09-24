from src.task6 import count_words

def test_task6_read_me():
    # Word count based on the provided text
    expected_count = 127
    assert count_words("src/task6_read_me.txt") == expected_count

