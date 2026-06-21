# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looks like a simple guessing game with a settings side bar. There are 3 settings of diffiulty: easy, normal, and hard. Each setting has a range and number of attempts. Easy is range of 1 to 20 with 6 attempts. Normal is range 1 to 100 with 8 attempts. Hard is range 1 to 50 with 5 attempts. There is an instruction box that tells us to guess a number between 1 and 100 with the number of attempts. The guesser has a textbox where the user can input their guess. When the user clicks and types in a guess, there is a message that says press enter to apply. The game is unplayable as there are many bugs for hints that the game currently has involving the hints given based on the number. 



- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

-doesn't give correct hints for negative numbers (-1 not between 1 and 100 and tells us to go lower)
-pressing enter doesnt work even though the hint says press enter to apply
-we start out with 7 attempts left even though we are allowed 8 attempts
-hints are incorrectly given
-attempts dont update to correct value when u reach 0 attempts
-right when u have 1 more attempt, the hint tells you the number and the score
-pressing new game gives us 8 attempts intead of starting at 7
-we can't guess again for some reason when we start a new game ( the attempt doesn't update and restart only when we run out of attempts)
-when on easy mode, the attempts get reduced to 6 when we start over and the new game still doesn't work
-when we are in easy mode, the rules don't update to between 1 to 20. it still says between 1 and 100.
-why is normal mode we get a range of 1 to 100 and 8 attempts. in hard mode, we have range 1 to 50 and 5 attempts (maybe mode settings are switched and attempts are switched?).
-when the user enters a guess that is not a number the hint says that is not a number. 
even though the attempt number allowed is 8, the instructions says 7 for normal difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 60 | Too high hint - Go lower (secret number is 47) | Too low hint - Go Higher | none |
| 1  | Too low hint - Go higher (secret number is 47) | Too high hint - Go Lower | none |
| -1 | Too low hint - Go higher (secret number is 47) | Too high hint - Go Lower | none |
| 101| Too high hint - Go lower (secret number is 47) | Too high hint - Go Lower | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example suggestion is thea that the every attempt compares int vs string (lines 130-134). That could make sense that the type error can cause the strings to be compared incorrectly. Also the AI says we start on attempt 2 since the code on line 93:
if "attempts" not in st.session_state:
    st.session_state.attempts = 1   # starts at 1, not 0

This means that the very first attempt is already broken since our first guess is already attempt 2. This also means that the starting on attempt 2, the guess is a string not an integer. Python also does not allow comparing int to str with < or > which creates the crash in the try block in check_guess and we get a TypeError fallback. 

Claude also states since both sides are strings, but string comparison is lexicographic not numeric so it compares character by character left to right. 

except TypeError:
    g = str(guess)      # convert guess to string too
    if g > secret:      # now comparing "1" > "47"
        return "Too High", "ð Go HIGHER!"
    return "Too Low", "ð Go LOWER!"

Thus, if we guess "6" it is guessing and comparing each letter by letter. If the correct number is 55, it is comparing "4" in "47" first. Which means, the logic will go to 6 > 4, which is False and returns "Too High" -> "Go HIGHER!" However, the logic should return "Too Low" -> "Go HIGHER!" I verified this by entering the guess and this is the behavior the app shows. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One suggested bug Claude gave was that the hint messages are swapped in check_guess (line 29-33). The logic is inverted, if the guess is greater than the secret we need to guess lower, not higher. The messages should be flipped. The logic itself is correct as if the guess is greater than the secret, it should return too high. Rather the messages are incorrect, not the logic. 

I verified this with the bug found, wich makes sense since given a number that is too low like 1, when the correct number is 47, the hint given should be "Too low, go Higher." However, the actual result is Too low, go Lower. The AI should tell us only that the messages are incorrect, not the logic. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I determined the bug was really fixed by adding test cases in test_game_logic.py specifiying the correct assertions and the correct case. I also looked at the test cases to make sure it makes sense. Lastly, I test in the actual app to make sure the specific test case works and the bug works. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The one test I ran using pytest was checking if the starting attempt has 8 attemts left, as it should if we start out. Since in normal mode the max number of attempts is 8. The bug originally is that we are given only 7 attempts remaining rather than the full 8 attempts. This test covers this bug. 


- Did AI help you design or understand any tests? How?
The AI helped me design and understand the test that where the initial attempt left shoudl be 8 when we first start the game. It explains that the normal attempt limit is 8 and by initializing the starting attempt to 0 instead of 1. It explains that if someone changed the starting attemtp to 1 (which is the bug) the test would fail with a clear message. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
