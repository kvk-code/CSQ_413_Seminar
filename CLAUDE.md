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

## Important Constraints
- Minimum 50 marks required to pass
- Students must refer to 2-3 research papers (post-2022, indexed journals/tier-1 conferences)
- Maximum one review/survey paper per student
- Weekly seminar diary maintenance required
- Handout submission before presentation mandatory