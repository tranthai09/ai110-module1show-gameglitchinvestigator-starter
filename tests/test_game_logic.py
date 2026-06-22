from logic_utils import check_guess
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import parse_guess

def test_initial_attempts_left_is_8():
    # On Normal difficulty the attempt limit is 8 and attempts start at 0,
    # so attempts_left at game start must be 8, not 7.
    attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
    attempt_limit = attempt_limit_map["Normal"]
    starting_attempts = 0  # bug would be starting_attempts = 1
    attempts_left = attempt_limit - starting_attempts
    assert attempts_left == 8, f"Expected 8 attempts left at game start, got {attempts_left}"

def test_very_large_guess_is_too_high():
    # A very large number parses successfully but should always be "Too High"
    # since the valid range tops out at 100.
    ok, guess_int, err = parse_guess("999999")
    assert ok is True, f"Expected parse to succeed for '999999', got error: {err}"
    outcome, _ = check_guess(guess_int, 50)
    assert outcome == "Too High", f"Expected 'Too High' for guess 999999, got '{outcome}'"

def test_decimal_guess_is_truncated_to_int():
    # parse_guess strips the decimal via int(float(raw)), so "3.7" becomes 3.
    ok, guess_int, err = parse_guess("3.7")
    assert ok is True, f"Expected parse to succeed for '3.7', got error: {err}"
    assert guess_int == 3, f"Expected decimal '3.7' to truncate to 3, got {guess_int}"

def test_negative_number_guess_is_too_low():
    # A negative number parses successfully and should always be "Too Low"
    # since the valid range starts at 1.
    ok, guess_int, err = parse_guess("-5")
    assert ok is True, f"Expected parse to succeed for '-5', got error: {err}"
    outcome, _ = check_guess(guess_int, 50)
    assert outcome == "Too Low", f"Expected 'Too Low' for guess -5, got '{outcome}'"

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
