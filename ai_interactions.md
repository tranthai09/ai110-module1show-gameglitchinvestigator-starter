# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
1. Generate a test case for negative numbers as the guesses 
2. Generate a test case for decimal numbers
3. Generate a test case for very large values

Each of these test cases were chosen as they were specific edge cases that didn't work when playing the initial game. The game wouldn't show the correct hints for negative numbers, decimal numbers, or very large values greater than 100.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
The AI created 3 test cases for each task given by first thinking and understanding the given task by looking at parse_guess in app.py:15-30. Then it read the file test_game_logic.py and edited it to add the imports for each task and then it thought and edited the same file to add the test cases for each task. Claude then explains the test cases as well as what it did and which lines. 

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
If it didn't specify where to add the test cases, I had to specify the test_game_logic.py file.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
