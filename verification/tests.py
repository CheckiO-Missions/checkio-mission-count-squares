"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[(0, 0), (1, 0), (0, 1), (1, 1)]],
            "answer": 1,
        },
        {
            "input": [[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]],
            "answer": 6,
        },
        {
            "input": [[(4, 3), (1, 1), (5, 3), (2, 3), (3, 2), (3, 1), (4, 2), (2, 1), (3, 3), (1, 2), (5, 2)]],
            "answer": 3,
        },
    ],
    "Extra": [
        {
            "input": [[(3, 4), (1, 2), (3, 2), (4, 5), (4, 2), (5, 3), (4, 1), (5, 4), (3, 5), (2, 4), (2, 2), (1, 1), (4, 4), (2, 5), (1, 5), (2, 1), (2, 3), (4, 3)]],
            "answer": 15,
        },
        {
            "input": [[(4, 3), (4, 2), (3, 1), (6, 1), (7, 4), (4, 4), (3, 3), (5, 4), (7, 1), (3, 4), (5, 2), (5, 1), (1, 1), (2, 3), (2, 4)]],
            "answer": 3,
        },
    ]
}
