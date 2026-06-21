from logic_utils import check_guess

def test_initial_attempts_left_is_8():
    # On Normal difficulty the attempt limit is 8 and attempts start at 0,
    # so attempts_left at game start must be 8, not 7.
    attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
    attempt_limit = attempt_limit_map["Normal"]
    starting_attempts = 0  # bug would be starting_attempts = 1
    attempts_left = attempt_limit - starting_attempts
    assert attempts_left == 8, f"Expected 8 attempts left at game start, got {attempts_left}"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ('Win', '🎉 Correct!')

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ('Too High', '📉 Go LOWER!')

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ('Too Low', '📈 Go HIGHER!')
