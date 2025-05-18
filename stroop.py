from psychopy import visual, core, event
import random

# Set up the window
win = visual.Window(size=(800, 600), color="white", units="pix")

# Colors and words
colors = ["red", "green", "blue", "yellow"]
color_rgb = {
    "red": "red",
    "green": "green",
    "blue": "blue",
    "yellow": "yellow"
}

# Instructions
instruction = visual.TextStim(win, text="Name the **COLOR** of the word. Press any key to start.", color="black")
instruction.draw()
win.flip()
event.waitKeys()

# Trials
n_trials = 10
trials = [(random.choice(colors), random.choice(colors)) for _ in range(n_trials)]

# Clock
clock = core.Clock()
results = []

# Run trials
for word, ink in trials:
    stim = visual.TextStim(win, text=word, color=color_rgb[ink], height=50)
    stim.draw()
    win.flip()

    clock.reset()
    keys = event.waitKeys(keyList=["r", "g", "b", "y", "escape"], timeStamped=clock)

    key, rt = keys[0]
    if key == "escape":
        break

    correct = (
        (key == "r" and ink == "red") or
        (key == "g" and ink == "green") or
        (key == "b" and ink == "blue") or
        (key == "y" and ink == "yellow")
    )

    results.append({"word": word, "ink": ink, "key": key, "rt": rt, "correct": correct})

# Show score
num_correct = sum(1 for r in results if r["correct"])
num_wrong = len(results) - num_correct

score_text = visual.TextStim(
    win,
    text=f"Correct: {num_correct}\nWrong: {num_wrong}",
    color="black",
    height=40
)
score_text.draw()
win.flip()
core.wait(3)


# Show all results on screen (paged)
result_lines = [
    f"{r['word']} in {r['ink']} | key: {r['key']} | {'Correct' if r['correct'] else 'Wrong'} "
    for r in results
]

for i in range(0, len(result_lines), 10):
    page = "\n".join(result_lines[i:i + 10])
    result_text = visual.TextStim(win, text=page, color="black", height=20, wrapWidth=700)
    result_text.draw()
    win.flip()
    core.wait(5)

win.close()

# Thank you message
end_text = visual.TextStim(win, text="Thank you for participating!", color="black")
end_text.draw()
win.flip()
core.wait(2)

