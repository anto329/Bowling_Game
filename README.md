#  Bowling Game Score Calculator

##  Problem Statement
This project implements a Python module to calculate the total score of a single **ten-pin bowling game** based on standard bowling rules.

The input is a string representing all rolls in a game, and the output is the final score after **exactly 10 frames**.

---

##  Bowling Rules (Summary)

- A bowling game consists of **10 frames**

### Frames 1–9
- Up to **2 rolls per frame**
- Maximum **10 pins per frame**

### Frame 10
- Always has **at least 2 rolls**
- A **strike or spare grants bonus roll(s)**
- Maximum **3 rolls** allowed in the 10th frame

---

##  Scoring Rules

- **Open frame** → Sum of pins in the frame  
- **Spare (`/`)** → `10 + pins from the next roll`  
- **Strike (`X`)** → `10 + pins from the next two rolls`

---

##  Input Format

The bowling game is provided as a **single string** using standard notation:

| Symbol | Meaning |
|------|--------|
| `0–9` | Pins knocked down |
| `X` | Strike |
| `/` | Spare |
| `-` | Miss (0 pins) |

### Example Inputs & Outputs

- "9-9-9-9-9-9-9-9-9-9-" → 90
- "XXXXXXXXXXXX" → 300
- "5/5/5/5/5/5/5/5/5/5/5" → 150


---

##  How the Solution Works

- The input string is converted into a list of numeric roll values
- Frames are evaluated sequentially
- Strike and spare bonuses are computed using **look-ahead rolls**
- Scoring stops after **10 frames**, even if bonus rolls exist

The solution uses a **roll-based approach**, which simplifies strike and spare handling.

---

##  Algorithm Explanation

### Phase 1: Parse Notation → Numbers

Bowling symbols are converted into numeric pin counts.

Input: "X7/9-"

Output: [10, 7, 3, 9, 0]


Conversion logic:
- `X` → 10
- `/` → 10 − previous roll
- `-` → 0
- `0–9` → same numeric value

---

### Phase 2: Calculate Score

The algorithm processes **exactly 10 frames** using a roll index pointer.

---

### Frames 1–9: Standard Frames

####  Strike (`X`)
- All 10 pins knocked down on the first roll  
- **Score = 10 + next 2 rolls**

Example:
X, 7, 2 = 10 + 7 + 2 = 19 points


####  Spare (`number + /`)
- All 10 pins knocked down using two rolls  
- **Score = 10 + next 1 roll**

Example:
7/, 5 = 10 + 5 = 15 points

####  Open Frame
- Less than 10 pins total  
- **Score = sum of both rolls**

Example:
7, 2 = 9 points

---

###  Frame 10: Special Rules

The 10th frame can have **up to 3 rolls**:

- **Strike on 1st roll** → 2 bonus rolls

X X X = 30 points

- **Spare on 1st + 2nd rolls** → 1 bonus roll  


7 / 5 = 15 points

- **Open frame** → Only 2 rolls  


7 2 = 9 points


 Bonus rolls in the 10th frame **do not create extra frames**.

---

##  Algorithm Steps (Summary)

1. Convert bowling notation into numeric roll values  
2. Use a roll index pointer to traverse rolls  
3. Loop exactly **10 times** (one iteration per frame)  
4. Apply strike and spare bonus rules using look-ahead  
5. Accumulate and return the final score  

---

##  How to Run

### Option 1: Run directly
- python bowling.py

### Option 2: Import and use the function
- from main import bowling_game
- bowling_game("X7/9-X-88/-6XXX81")

---

## Test Cases
### Test Case 1: All Open Frames
Input: 9-9-9-9-9-9-9-9-9-9-

Expected Output: 90

Description: Each frame knocks down 9 pins with no strike or spare bonuses


### Test Case 2: All Misses
Input: --------------------

Expected Output: 0

Description: No pins are knocked down in any frame


### Test Case 3: All Strikes (Perfect Game)
Input: XXXXXXXXXXXX

Expected Output: 300

Description: 12 consecutive strikes, maximum possible score


### Test Case 4: All Spares
Input: 5/5/5/5/5/5/5/5/5/5/5

Expected Output: 150

Description: Consecutive spares with constant bonus


### Test Case 5: Strike Followed by Open Frames
Input: X9-9-9-9-9-9-9-9-9-

Expected Output: 100

Description: First frame is a strike with bonus rolls, remaining frames are open


### Test Case 6: Spare Followed by Open Frames
Input: 9/9-9-9-9-9-9-9-9-9-

Expected Output: 100

Description: First frame is a spare followed by open frames


### Test Case 7: Mixed Game
Input: X5/34----------------

Expected Output: 40

Description: Combination of strike, spare, and open frames


### Test Case 8: Spares with Zero Bonus
Input: 5/-5/-5/-5/-5/-5/-5/-5/-5/-5/-

Expected Output: 100

Description: Each spare is followed by a miss, resulting in no bonus pins


### Test Case 9: Strike in the 10th Frame
Input: 9-9-9-9-9-9-9-9-9-X34

Expected Output: 98

Description: Nine open frames followed by a strike in the 10th frame with two bonus rolls


### Test Case 10: Spare in the 10th Frame
Input: 9-9-9-9-9-9-9-9-9-5/5

Expected Output: 95

Description: Spare in the 10th frame grants one bonus roll



