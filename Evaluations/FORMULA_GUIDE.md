# Consolidated Evaluation Excel Files - Formula Guide

## Overview

Two Excel files have been generated with **live auto-calculating formulas**:
- `Consolidated_Evaluation_Monday.xlsx` (36 students, 3 evaluators)
- `Consolidated_Evaluation_Friday.xlsx` (37 students, 3 evaluators)

---

## File Structure

### Column Layout (Example for Monday Batch)

| Column | Field | Type | Description |
|--------|-------|------|-------------|
| A | Roll No | Static | Student roll number |
| B | Student Name | Static | Student name |
| C | Project Group | Static | Group assignment |
| D | Presentation Title | Static | Seminar topic |
| E-G | Organization (10) (Evaluator 1-3) | **Input** | Individual scores (0-10) |
| H | Avg Organization (10) | **Formula** | Auto-calculates average |
| I | Δ Organization (10) | **Formula** | Auto-calculates variance |
| J-L | Clarity & Communication (10) (Evaluator 1-3) | **Input** | Individual scores (0-10) |
| M | Avg Clarity & Communication (10) | **Formula** | Auto-calculates average |
| N | Δ Clarity & Communication (10) | **Formula** | Auto-calculates variance |
| O-Q | Q&A (10) (Evaluator 1-3) | **Input** | Individual scores (0-10) |
| R | Avg Q&A (10) | **Formula** | Auto-calculates average |
| S | Δ Q&A (10) | **Formula** | Auto-calculates variance |
| T-V | Overall Participation (10) (Evaluator 1-3) | **Input** | Individual scores (0-10) |
| W | Avg Overall Participation (10) | **Formula** | Auto-calculates average |
| X | Δ Overall Participation (10) | **Formula** | Auto-calculates variance |
| Y-AA | Total (40) (Evaluator 1-3) | Static | Per-evaluator totals from source |
| AB | Consolidated Total (40) | **Formula** | Sum of all avg criteria |
| AC | Guide Name | Static | Faculty guide name |
| AD | Flag | **Formula** | "check variance" if any Δ > 2 |
| AE | Match Quality | Static | How student was matched (roll/name) |

---

## Formula Details

### 1. Average Columns (Blank-Aware)

**Purpose**: Calculate the average score from all evaluators, ignoring blank cells.

**Example** (for Organization in row 2, evaluators in columns E, F, G):
```excel
=IF(COUNTA(E2,F2,G2)=0,"",AVERAGE(E2,F2,G2))
```

**How it works**:
- `COUNTA(E2,F2,G2)` counts how many evaluators provided scores
- If count is 0 (all blank), returns blank `""`
- Otherwise, calculates `AVERAGE(E2,F2,G2)` excluding blanks
- **Blanks are NOT treated as zero**

**What happens when you add values**:
- Initially blank cells: Average recalculates automatically
- Partial data (e.g., 2 of 3 evaluators): Average uses only available scores
- All evaluators filled: Average uses all 3 values

---

### 2. Variance (Δ) Columns

**Purpose**: Show the disagreement between evaluators (max score - min score).

**Example** (for Organization in row 2, evaluators in columns E, F, G):
```excel
=IF(COUNTA(E2,F2,G2)<2,"",MAX(E2,F2,G2)-MIN(E2,F2,G2))
```

**How it works**:
- `COUNTA(E2,F2,G2)<2` checks if fewer than 2 evaluators scored
- If less than 2 scores, returns blank (can't calculate variance)
- Otherwise, calculates `MAX - MIN` to show spread

**Interpretation**:
- Δ = 0: Perfect agreement among evaluators
- Δ = 1-2: Acceptable variance
- **Δ > 2**: High disagreement - flagged for review

---

### 3. Consolidated Total (40)

**Purpose**: Sum all four average criteria to get overall score out of 40.

**Example** (in row 2, avg columns are H, M, R, W):
```excel
=SUM(H2,M2,R2,W2)
```

**How it works**:
- Adds: Avg Organization + Avg Clarity + Avg Q&A + Avg Participation
- Automatically updates when any average changes
- If any average is blank, treats it as 0 in the sum

---

### 4. Flag Column (Auto-Detection)

**Purpose**: Automatically flag students with high evaluator disagreement.

**Example** (in row 2, delta columns are I, N, S, X):
```excel
=IF(OR(I2>2,N2>2,S2>2,X2>2),"check variance","")
```

**How it works**:
- Checks if ANY of the 4 delta values exceed 2
- If yes, displays `"check variance"`
- If no, displays blank `""`

**Use case**: Filter by this column to quickly find students needing review.

---

## How to Use the Formulas

### Scenario 1: Filling in Missing Evaluator Scores

**Current state**: Student has scores from 2 evaluators, 3rd is blank
```
Organization (Kiran V K): 8
Organization (Shilpa): 9
Organization (Usha K): [BLANK]
Avg Organization: 8.5 (calculated from 8 and 9)
```

**You add**: Enter `7` in the blank cell

**Auto-updates**:
```
Avg Organization: 8.0 (now calculated from 8, 9, 7)
Δ Organization: 2.0 (max 9 - min 7)
Consolidated Total: Updates to include new average
Flag: Stays blank (Δ = 2 is at threshold)
```

---

### Scenario 2: Correcting an Evaluator Score

**Current state**:
```
Q&A (Kiran V K): 5
Q&A (Shilpa): 9
Q&A (Usha K): 8
Avg Q&A: 7.33
Δ Q&A: 4.0
Flag: "check variance"
```

**You change**: Correct Kiran's score from `5` to `8`

**Auto-updates**:
```
Avg Q&A: 8.33 (recalculated from 8, 9, 8)
Δ Q&A: 1.0 (max 9 - min 8)
Consolidated Total: Increases by ~1 point
Flag: Clears (no more variance > 2)
```

---

### Scenario 3: Adding All Scores for a Student

**Current state**: All evaluator cells are blank
```
All Organization scores: [BLANK]
Avg Organization: [BLANK]
Δ Organization: [BLANK]
```

**You add**: Fill in all three evaluator scores (9, 8, 9)

**Auto-updates**:
```
Avg Organization: 8.67
Δ Organization: 1.0
(Repeat for all 4 criteria)
Consolidated Total: Sum of all 4 averages (e.g., 35.5)
Flag: Blank or "check variance" depending on all deltas
```

---

## Formula Advantages

### ✓ No Manual Calculation
- Just enter evaluator scores, everything else auto-calculates
- Reduces human error in averaging and variance checking

### ✓ Blank-Aware Logic
- Handles missing evaluator scores gracefully
- Doesn't penalize students for missing evaluations

### ✓ Real-Time Validation
- Flag column instantly alerts you to disagreements
- Variance tracking helps identify evaluation inconsistencies

### ✓ Audit Trail
- All individual evaluator scores preserved
- Can see exactly where disagreements occur
- Easy to trace back to source evaluation sheets

---

## Best Practices

### 1. Input Values Only in Evaluator Columns
- **DO**: Enter scores in columns like "Organization (10) (Kiran V K)"
- **DON'T**: Manually edit Avg, Δ, Total, or Flag columns (formulas will overwrite)

### 2. Use Blank for Missing Scores
- **DO**: Leave cell empty if evaluator didn't score
- **DON'T**: Enter 0 or "-" (will affect averages incorrectly)

### 3. Review Flagged Students
- Filter by Flag = "check variance"
- Compare evaluator scores side-by-side
- Discuss discrepancies with evaluation team

### 4. Export to CSV for AI Processing
When ready for AI analysis:
1. File → Save As → CSV (values will be frozen)
2. All formulas become static calculated values
3. AI agents can parse the CSV easily

---

## Regenerating Files

If source CSV files are updated (e.g., evaluators add more scores):

```bash
python generate_consolidated_with_formulas.py
```

**What happens**:
- Reads latest evaluator CSV files
- Regenerates Excel files with fresh formulas
- Overwrites existing consolidated files

**Important**: Any manual edits in the consolidated Excel will be lost. If you've made corrections, save them elsewhere first.

---

## Troubleshooting

### Formula shows "#VALUE!" error
**Cause**: Non-numeric value in evaluator column (e.g., text like "absent")
**Fix**: Clear the cell or enter a numeric value

### Average doesn't update when I add a score
**Cause**: Cell might have text formatting
**Fix**: Check cell format (should be "Number"), re-enter the value

### Consolidated Total shows wrong value
**Cause**: One or more average columns is blank
**Fix**: Ensure all 4 criteria have at least one evaluator score

### Flag doesn't appear when variance is high
**Cause**: Delta columns might be blank (less than 2 evaluators)
**Fix**: Need at least 2 evaluator scores for variance calculation

---

## Technical Specifications

### Monday Batch
- **File**: `Consolidated_Evaluation_Monday.xlsx`
- **Students**: 36
- **Evaluators**: Kiran V K, Shilpa, Usha K
- **Formulas per row**: 13 (4 averages + 4 deltas + 1 total + 1 flag + 3 static)
- **Total formulas**: ~468 (36 students × 13)

### Friday Batch
- **File**: `Consolidated_Evaluation_Friday.xlsx`
- **Students**: 37
- **Evaluators**: Kiran V K, Shankar, Usha K
- **Formulas per row**: 13
- **Total formulas**: ~481 (37 students × 13)

---

## Example Workflow

### Step 1: Open Excel File
Open `Consolidated_Evaluation_Monday.xlsx` or `Consolidated_Evaluation_Friday.xlsx`

### Step 2: Review Current State
- Scroll through to see which cells have values
- Note students with blank evaluator scores

### Step 3: Add Missing Scores
- Find cells with missing evaluator data
- Enter scores (0-10 scale)
- Watch formulas auto-update in real-time

### Step 4: Review Variance Flags
- Filter by Flag column = "check variance"
- Review students with Δ > 2 in any criterion
- Compare side-by-side evaluator scores

### Step 5: Resolve Discrepancies
- Discuss with evaluation team
- Correct any obvious data entry errors
- Document reasoning for legitimate disagreements

### Step 6: Export for AI Processing (Optional)
- File → Save As → CSV
- Provides AI agents with calculated values
- Preserves all evaluator scores and metadata

---

## Contact & Support

For questions about formulas or evaluation process:
- **Coordinator**: Kiran V K
- **Seminar In-Charge**: Dr. Sruthy Manmadhan

---

*Generated: 2025-10-24 01:10*
*Script: generate_consolidated_with_formulas.py*
*Version: 1.0*
