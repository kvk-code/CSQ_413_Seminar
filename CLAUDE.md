# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository manages the CSQ413 Seminar course for final year Computer Science & Engineering students at NSS College of Engineering under APJ Abdul Kalam Technological University. The seminar course involves student presentations on current technology topics with comprehensive evaluation and documentation.

## Key Data Architecture

### Core Files Structure
- **Course Documentation**: `CSQ413 Seminar Guidelines.md`, `CSQ413_Seminar_Syllabus.md`, `Rubrics for Seminar_21.07.2025.md`
- **Student Data**: CSV files containing student information, batch assignments, and evaluation sheets
- **Batch Organization**: Students divided into Monday (Groups 1-9, 36 students) and Friday (Groups 10-19, 37 students) batches

### CSV File Relationships
1. `Seminar_Batches.csv` - Master team list with guide allocations (19 teams total)
2. `CSE Seminar Title 2025-26_Fin.csv` - Finalized presentation titles with contact information and presentation dates (authoritative source)
3. `monday_batch_evaluation.csv` / `friday_batch_evaluation.csv` - Session-specific evaluation sheets
4. `complete_evaluation_sheet.csv` - Combined evaluation sheet for all groups
5. `class_roll_list.csv` - Complete student roster
6. `CSQ413_S7CSE_Seminar_Report_Hardcopy_Status_*.csv` - Tracks hardcopy report submission status (Copy 1, Copy 2, Guide signature, In-Charge signature)
7. `Pending_Submissions_Status_*.csv` - Extracted list of pending students with incomplete hardcopy submission procedures and detailed remarks
8. `Pending_Submissions_Summary_*.txt` - Human-readable summary report of pending submissions with guide-wise breakdown for follow-up coordination

### Data Flow
- Student titles from response sheet populate evaluation sheets
- Team assignments from batch file determine guide allocations
- Evaluation sheets track 4 components: Guide (20), Coordinator (20), Presentation (40), Report (20) = 100 marks total

## Common Tasks

### Working with Student Data
- **Finding student information**: Search across `class_roll_list.csv`, `Seminar_Batches.csv`, and response sheets
- **Batch assignments**: Monday groups 1-9, Friday groups 10-19 (defined in `Seminar_Batches.csv:1`)
- **Evaluation tracking**: Use batch-specific evaluation CSV files with pre-populated student names and titles

### Managing Evaluation Sheets
- Presentation titles should be populated from `CSE Seminar Title 2025-26_Fin.csv:5` (column E - Topic column)
- This is the authoritative source for all finalized seminar titles
- Each student has 4 evaluation components with specific mark allocations
- Guide assignments are consistent across all files and match team structures

### Message Drafting Context
- **Academic Year**: 2024-25
- **Course**: CSQ413 Seminar (2 credits, 100 marks CIE)
- **Institution**: NSS College of Engineering, CSE Department
- **Key Personnel**: Dr. Sruthy Manmadhan (Seminar In-Charge), Kiran V K (Coordinator)
- **Session Details**: 20 min presentation + 5 min Q&A, 6 students per session

## Git Workflow

### Version Control Policy
Since this is a Git repository, Claude Code should automatically commit and push changes to the remote repository after completing significant tasks. This ensures:
- Data integrity and backup of evaluation sheets
- Change history for student records
- Collaboration support across multiple users
- Recovery options in case of local data loss

### Commit Guidelines
- **Commit frequency**: After any significant changes including:
  - Updates to evaluation sheets (batch or complete)
  - Student data modifications (titles, contact info, batch assignments)
  - New documentation or guideline updates
  - Bulk data imports or synchronizations
- **Commit messages**: Use descriptive, conventional commit style (e.g., "feat:", "update:", "fix:", "docs:")
- **Push policy**: Always push to remote after committing unless explicitly instructed otherwise
- **Branch**: Work on the main branch unless specified otherwise for this project

## Evaluation Components
1. **Seminar Guide** (20 marks): Background Knowledge (10) + Topic Relevance (10)
2. **Seminar Coordinator** (20 marks): Seminar Diary (10) + Attendance (10)
3. **Presentation** (40 marks): Organization (10) + Clarity & Communication (10) + Q&A (10) + Overall Participation (10)
4. **Report** (20 marks): Technical content, format, references

## Data Transformation Operations

### Participation-Based Scaling (October 24, 2025)
**Objective**: Scale Friday batch Overall Participation marks while keeping Consolidated Total unchanged

**Operation Performed**:
1. **Source File**: `Evaluations/Boosted_Evaluations/Consolidated_Evaluation_Friday_Boosted.xlsx`
2. **Scaling Target**: Column "Avg Overall Participation (10)" only
3. **Method**: Linear scaling with minimum threshold
   - Formula: `scaled = 4 + (original - min_val) * 6 / (max_val - min_val)`
   - Original range: [1.00, 10.00]
   - Scaled range: [4.00, 10.00]
   - Blank entries: Assigned 4.00 (minimum)
4. **Results**:
   - 36/37 students received a boost (average +2.08 points)
   - Only unchanged: Anoop P (already at maximum 10.00)
   - Blank entry (Amrutha P): Assigned 4.00
   - Consolidated Total (40): Completely unchanged (+0.00)
5. **Output File**: `Consolidated_Evaluation_Friday_Scaled_Final.xlsx`
6. **Impact**: 
   - Mean participation increased from 3.77 to 5.80
   - Total batch participation increased by +78.78 points
   - Lowest performers received maximum boost (+3.00)
   - Highest performers received no boost (already at max)
   - All other columns remain identical to original

**Key Constraint**: ONLY the "Avg Overall Participation (10)" column was modified. The "Consolidated Total (40)" and all other fields remained completely unchanged.

**Files Generated**:
- `analyze_scaling_effect.py` - Analysis script showing impact on all 37 students
- `apply_scaling_final.py` - Implementation script with verification
- `FINAL_SCALING_REPORT.txt` - Comprehensive before-after report
- `Consolidated_Evaluation_Friday_Scaled_Final.xlsx` - Final output file with scaled participation marks

### Final Consolidated Marks Distribution (November 13, 2025)
**Objective**: Create a comprehensive single CSV file combining all 4 evaluation components with clear component-wise breakdown

**File Location**: `Evaluations/For_Display/FINAL_CONSOLIDATED_MARKS.csv`

**Column Structure (20 columns)** - Each total column shows its formula using short forms:

1. **Roll No** - Student roll number
2. **Student Name** - Full student name
3. **Background Knowledge - BK (10)** - Guide component (part 1)
4. **Topic Relevance - TR (10)** - Guide component (part 2)
5. **Guide Total (20) = BK + TR** - Sum of background knowledge and topic relevance
6. **Seminar Diary - SD (10)** - Coordinator component (part 1)
7. **Attendance - Att (10)** - Coordinator component (part 2) - **BLANK (data not available)**
8. **Coordinator Total (20) = SD + Att** - Seminar diary marks only (attendance component blank)
9. **Organization - Org (10)** - Presentation component (part 1)
10. **Clarity & Communication - C&C (10)** - Presentation component (part 2)
11. **Q&A (10)** - Presentation component (part 3)
12. **Overall Participation - OP (10)** - Presentation component (part 4)
13. **Presentation Total (40) = Org + C&C + Q&A + OP** - Sum of all presentation components
14. **Technical Content - TC (8)** - Report component (part 1)
15. **Overall Quality - OQ (5)** - Report component (part 2)
16. **Templates Followed - TF (4)** - Report component (part 3)
17. **Adequacy of References - AR (3)** - Report component (part 4)
18. **Report Total (20) = TC + OQ + TF + AR** - Sum of all report components
19. **GRAND TOTAL (100) = Guide(20) + Coordinator(20) + Presentation(40) + Report(20)** - Final total with decimal precision
20. **GRAND TOTAL Rounded Up (100)** - Ceiling function applied (rounds up only if fractional part exists)

**Rounding Logic (Column 20)**:
- Uses ceiling function: rounds UP to next higher integer only when fractional part exists
- Example: 78.83 → 79, 81.0 → 81, 88.5 → 89, 79.0 → 79
- Integers remain unchanged; decimals round up

**Data Composition**:
- All 73 students included (36 Monday batch + 37 Friday batch)
- Source data pulled from 4 separate For_Display files:
  - Guide marks from: `CSQ413_S7CSE_Seminar_Guide_Marks - Guide_Marks.csv`
  - Coordinator marks from: `CSQ413_S7CSE_Seminar_Coordinator_Marks - Seminar_Diary.csv`
  - Report marks from: `CSQ413_S7CSE_Seminar_Report_Marks_Consolidated - Seminar Report.csv`
  - Presentation marks from: `Combined_Consolidated_Evaluation.csv`

**Score Statistics**:
- Mean Total: 78.76/100
- Min Total: 68.0, Max Total: 88.5
- After rounding: Min 68, Max 89

**Key Features**:
- Crystal clear component hierarchy showing what composes each total
- Short forms (BK, TR, SD, Att, Org, C&C, OP, TC, OQ, TF, AR) used consistently
- Formulas displayed in column headers for transparency
- Attendance column visibly blank, indicating data not available
- Each component total immediately follows its sub-components
- Unambiguous structure for mark verification and display to students

**Generation Script**: `create_consolidated_marks_final.py`

## Important Constraints
- Minimum 50 marks required to pass
- Students must refer to 2-3 research papers (post-2022, indexed journals/tier-1 conferences)
- Maximum one review/survey paper per student
- Weekly seminar diary maintenance required
- Handout submission before presentation mandatory