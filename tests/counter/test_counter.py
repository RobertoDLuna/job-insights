from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'

    with open(path) as file:
        data = file.read()

        expected = {
            "python": data.lower().count("python"),
            "javascript": data.lower().count("javascript"),
        }

        assert expected["python"] == count_ocurrences(path, 'python')
        assert expected["javascript"] == count_ocurrences(path, 'javascript')