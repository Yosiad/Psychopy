from psychopy import visual, core, event
import random

# Set up window
win = visual.Window(size=(800, 600), color="white", units="pix")

# Word list
all_words = ["apple", "chair", "moon", "river", "car", "book", "shoe", "flower", "tree", "cloud", "banana", "mountain"]
study_words = random.sample(all_words, 10)

# Instruction screen
instruction = visual.TextStim(win, text="Memorize the following words", color="black", height=30)
instruction.draw()
win.flip()
event.waitKeys()

# Show words one by one
for word in study_words:
    stim = visual.TextStim(win, text=word, color="blue", height=50)
    stim.draw()
    win.flip()
    core.wait(1)

core.wait(1)

# Recognition phase
test_words = random.sample(all_words, 10)
results = []

for word in test_words:
    prompt = visual.TextStim(win, text=f"Did you see this word?\n\n{word}\n\n(y = yes, n = no)", color="black", height=40)
    prompt.draw()
    win.flip()

    keys = event.waitKeys(keyList=["y", "n", "escape"])
    if "escape" in keys:
        break

    seen_before = word in study_words
    response = keys[0]
    correct = (response == "y" and seen_before) or (response == "n" and not seen_before)

    results.append({"word": word, "seen_before": seen_before, "response": response, "correct": correct})

# Show score
num_correct = sum(1 for r in results if r["correct"])
num_wrong = len(results) - num_correct

score_text = visual.TextStim(win, text=f"Correct: {num_correct}\nWrong: {num_wrong}", color="black", height=40)
score_text.draw()
win.flip()
core.wait(3)


# Show all results on screen (paged)
result_lines = [
    f"{r['word']} | Seen: {'Yes' if r['seen_before'] else 'No'} | Answer: {r['response']} | {'Correct' if r['correct'] else 'Wrong'}"
    for r in results
]

for i in range(0, len(result_lines), 10):
    page = "\n".join(result_lines[i:i + 10])
    result_text = visual.TextStim(win, text=page, color="black", height=20, wrapWidth=700)
    result_text.draw()
    win.flip()
    core.wait(5)

win.close()

# Goodbye message
end = visual.TextStim(win, text="Thanks for playing!", color="black")
end.draw()
win.flip()
core.wait(2)


