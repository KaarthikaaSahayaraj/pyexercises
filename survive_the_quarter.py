
# =====================================================================
# SURVIVE THE QUARTER - Croissant Rocket
# Name: Kaarthikaa Sahayaraj          Group: CL05
# =====================================================================
#

#
# 1) WHAT GOES IN?
#    The file scenarios_A.csv. Separator: comma. Text with commas or
#    quotes inside is wrapped in double quotes ("..."), and a quote
#    inside text is written twice ("").
#    One header line, then one line per scenario, 14 columns:
#    ID, Scenario, OptionA, OptionB, OptionC,
#    BudgetA, BudgetB, BudgetC, ReputationA, ReputationB, ReputationC,
#    FeedbackA, FeedbackB, FeedbackC.
#    The file is "wide": the 3 options are spread over 4 groups of columns.
#    Numbers are plain integers, negative with a minus sign (-800), no
#    "EUR", no thousand separator. They are read as text, so I convert
#    them with int(). The impact of option B = BudgetB and ReputationB.
#
# 2) WHAT HAPPENS? (one day)
#    - show the day number and both gauges
#    - show the situation and options A, B, C
#    - ask A, B or C until the answer is valid
#    - add the budget and reputation change (reputation max 100)
#    - show the feedback line and the changes
#    - save (reputation change, day, option text) in the history
#    - if budget or reputation <= 0: game over at once
#
# 3) WHAT COMES OUT?
#    On screen: "fired" and why, or "Quarter survived!" with budget,
#    reputation, score (reputation + budget // 200) and title, then the
#    best and the worst move (biggest / smallest reputation change).
#    One line appended to results.csv, for example:
#    Mithra,6350,100,CMO Material,2026-11-17 15:40
#
# 4) WHAT COULD GO WRONG?
#    - The scenario file is missing -> clear message, the program stops
#      cleanly instead of crashing.
#    - A line in the file is broken (missing column, number that is not
#      a number) -> that line is skipped, the other scenarios still load.
#    - The player types something else than A, B or C (d, 1, empty) ->
#      the question is asked again; lower case a, b, c is accepted.
#    - A gauge goes to 0 or below -> the loop stops at once (break).
#    - Reputation would go above 100 -> it is capped at 100.
#    - The player gives an empty name -> "Anonymous" is used.
#    - results.csv does not exist yet -> it is created with a header.
#    - Fewer than 10 scenarios in the file -> the game plays all of them.
#
# FEATURE CHOSEN: (a) Streak bonus.
#    Three reputation gains in a row give +500 EUR. I chose it because
#    it rewards the balance the game is about, and it reuses the history
#    list I already keep for best and worst move.
#
# MISSING / NOT FINISHED: nothing, the game runs completely.
# =====================================================================

# --- Imports: csv to read/write files, random to shuffle, datetime for the date --- Imports: csv to read/write files, random to shuffle, datetime for the date
import csv
import random
from datetime import datetime

# --- Game settings, all in one place so they are easy to change
SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
STREAK_LENGTH = 3
STREAK_BONUS = 500


# --- Read the scenario file and turn every line into a dictionary.
# Each option is stored as a tuple: (text, budget_change, reputation_change, feedback)
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                options = {}
                for letter in ("A", "B", "C"):
                    options[letter] = (
                        row["Option" + letter],
                        int(row["Budget" + letter]),
                        int(row["Reputation" + letter]),
                        row["Feedback" + letter],
                    )
                scenarios.append({"text": row["Scenario"], "options": options})
            except (KeyError, ValueError, TypeError):
                # broken line: skip it and keep the rest of the game working
                print("Warning: skipped a broken line in the file (ID", row.get("ID"), ")")
    return scenarios


# --- Show one day: number, gauges, situation and the three options
def show_day(day, budget, reputation, scenario):
    print()
    print("--- Day", day, "---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(scenario["text"])
    for letter in ("A", "B", "C"):
        print(f"  {letter}: {scenario['options'][letter][0]}")


# --- Ask A, B or C again and again until the answer is valid
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ("A", "B", "C"):
        answer = input("Please type A, B or C: ").strip().upper()
    return answer


# --- Apply an option to the gauges and return the new gauges as a tuple
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# --- Feature (a): update the streak counter and return (new_streak, bonus)
def update_streak(streak, reputation_change):
    if reputation_change > 0:
        streak += 1
    else:
        streak = 0
    if streak == STREAK_LENGTH:
        return 0, STREAK_BONUS      # bonus earned, the streak starts again
    return streak, 0


# --- Turn the final gauges into a score and a title
def get_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return None, "Fired"
    score = reputation + budget // 200
    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


# --- Find the best and worst move in the history.
# Each tuple starts with the reputation change, so max() and min() compare that first.
def best_and_worst(history):
    return max(history), min(history)


# --- Add one line to results.csv (and the header if the file is new)
def save_result(name, budget, reputation, title):
    try:
        with open(RESULTS_FILE, newline="", encoding="utf-8") as f:
            file_is_new = f.read().strip() == ""
    except FileNotFoundError:
        file_is_new = True
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if file_is_new:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title,
                         datetime.now().strftime("%Y-%m-%d %H:%M")])


# --- The whole game, from the name to the saved result
def play():
    # Load the file, stop cleanly if it is missing or empty
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("Error:", SCENARIO_FILE, "was not found. Put it next to this program.")
        return
    if not scenarios:
        print("Error: no valid scenario in", SCENARIO_FILE)
        return

    # Welcome and name
    print("=== SURVIVE THE QUARTER - Croissant Rocket ===")
    name = input("Your name: ").strip() or "Anonymous"

    # Starting gauges, shuffled scenarios, empty history
    budget = START_BUDGET
    reputation = START_REPUTATION
    random.shuffle(scenarios)
    history = []          # one tuple per day: (reputation_change, day, option_text)
    streak = 0            # reputation gains in a row
    reason = ""

    # The ten days
    for day in range(1, min(DAYS, len(scenarios)) + 1):
        scenario = scenarios[day - 1]
        show_day(day, budget, reputation, scenario)
        letter = ask_choice()
        option = scenario["options"][letter]
        text, budget_change, reputation_change, feedback = option

        budget, reputation = apply_choice(budget, reputation, option)
        print(feedback)
        print(f"Budget {budget_change:+d} EUR, Reputation {reputation_change:+d}")
        history.append((reputation_change, day, text))

        # Feature (a): streak bonus
        streak, bonus = update_streak(streak, reputation_change)
        if bonus:
            budget += bonus
            print(f"STREAK! Three reputation gains in a row: +{bonus} EUR")

        # Game over at once if a gauge hits zero
        if budget <= 0:
            reason = "the budget hit zero. The bank said no."
            break
        if reputation <= 0:
            reason = "the reputation hit zero. The internet hates you."
            break

    # End of game: result, title, best and worst move
    print()
    print("=" * 30)
    score, title = get_title(budget, reputation)
    if title == "Fired":
        print(f"You are FIRED, {name}: {reason}")
        print(f"Budget: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print("Final score:", score)
        print(f"{name}, your title: {title}")

    best, worst = best_and_worst(history)
    print(f'Best move:  day {best[1]}, "{best[2]}" ({best[0]:+d})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+d})')

    save_result(name, budget, reputation, title)
    print("Saved in", RESULTS_FILE)


# --- Start the game; Ctrl+C or a closed input ends it politely instead of crashing
if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped. See you next quarter.")