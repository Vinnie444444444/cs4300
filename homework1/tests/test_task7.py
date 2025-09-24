from src.task7 import get_status_code

def test_example_status():
    #example.com should return 200
    assert get_status_code("https://www.example.com") == 200

