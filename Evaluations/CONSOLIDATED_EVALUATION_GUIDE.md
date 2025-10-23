# Consolidated Evaluation Sheet - User Guide

## Overview

The **Consolidated_Evaluation.xlsx** workbook merges all evaluator scores from Monday and Friday batch CSV files into a comprehensive side-by-side comparison with automatic variance detection and statistical analysis.

---

## Generated Files

- **`Consolidated_Evaluation.xlsx`** - Main Excel workbook (20.7 KB)
- **`generate_consolidated_evaluation.py`** - Python generator script (reusable)

---

## Workbook Structure

### 1. **Monday Sheet** (36 students)
   - **Evaluators**: Kiran V K, Shilpa, Usha K
   - **Columns**:
     - Roll No, Student Name, Project Group, Presentation Title
     - For each criterion (Organization, Clarity & Communication, Q&A, Overall Participation):
       - Individual evaluator scores (e.g., `Organization (10) (Kiran V K)`)
       - Blank-aware average (`Avg Organization (10)`)
       - Variance (`Δ Organization (10)` = max - min)
     - Per-evaluator totals: `Total (40) (Evaluator Name)`
     - **Consolidated Total (40)** = sum of all average criteria
     - Guide Name, Flag, Data Issue, Match Quality
   - **Variance Flags**: 18 students flagged with "check variance" (Δ > 2)

### 2. **Friday Sheet** (37 students)
   - **Evaluators**: Kiran V K, Shankar, Usha K
   - Same structure as Monday sheet
   - **Variance Flags**: 18 students flagged

### 3. **Summary Sheet**
   - Batch-wise statistics:
     - Student count
     - Mean, Median, Min, Max of Consolidated Total (40)
     - Number of variance flags
   - Quick comparison between Monday and Friday batches

### 4. **README Sheet**
   - Files ingested and evaluator mapping
   - Column normalization rules
   - Data quality issues (if any)
   - Thresholds and blank-handling logic
   - Generation timestamp

---

## Key Features

### Blank-Aware Averaging
- **Blanks are NOT treated as zero**
- Average = mean of non-blank evaluator scores only
- If all evaluators have blanks for a criterion, average is also blank

### Variance Detection
- **Threshold**: Δ > 2 for any criterion (out of 10)
- Automatically highlighted in **yellow** in Excel
- Flag column shows "check variance" for easy filtering

### Data Normalization
- **Roll No**: Converted to integer format (e.g., `45.0` → `45`)
- **Student Name**: Title case, trimmed, whitespace collapsed
- **Blanks**: Empty strings, `-`, `NA`, `N/A`, `NaN` all treated as missing

### Conditional Formatting
- **Variance cells** (Δ > 2): Yellow background
- **Consolidated Total (40)**: (Could add color scale: red to green)

### Excel Features
- **Frozen header row** for easy scrolling
- **Auto-filter** enabled on all data columns
- **Proper column widths** for readability
- **Number formatting**: 1 decimal place for scores

---

## How to Use

### 1. **Review Variance Flags**
   - Filter by `Flag` column = "check variance"
   - Review students with high disagreement between evaluators
   - Check individual evaluator scores and Δ columns

### 2. **Analyze Consolidated Totals**
   - Sort by `Consolidated Total (40)` to identify top/bottom performers
   - Compare with per-evaluator totals to spot outliers

### 3. **Cross-Batch Comparison**
   - Use Summary sheet for quick batch statistics
   - Compare mean/median scores between Monday and Friday

### 4. **Data Quality Checks**
   - Review README sheet for any data issues
   - Check Match Quality column (should be `roll` for most students)

---

## Regenerating the Report

If evaluator CSV files are updated, simply rerun:

```bash
python generate_consolidated_evaluation.py
```

The script will:
- Read all 6 CSV files
- Rebuild the consolidated workbook from scratch
- Overwrite `Consolidated_Evaluation.xlsx`

**Note**: The script is idempotent (safe to run multiple times).

---

## Statistical Summary

### Monday Batch
- **Students**: 36
- **Evaluators**: 3 (Kiran V K, Shilpa, Usha K)
- **Variance Flags**: 18 (50%)

### Friday Batch
- **Students**: 37
- **Evaluators**: 3 (Kiran V K, Shankar, Usha K)
- **Variance Flags**: 18 (48.6%)

### Overall
- **Total Students**: 73
- **Total Variance Flags**: 36 (49.3%)

---

## Troubleshooting

### Missing Scores
- Check source CSV files for blank cells
- Blanks are intentional (student absent or not evaluated)
- Do NOT treat as zero in calculations

### High Variance
- Review original evaluation sheets for inconsistencies
- Consider re-evaluation or discussion among evaluators
- May indicate genuine disagreement on student performance

### Name Mismatches
- Check README sheet for logged data issues
- May require manual correction in source CSV files

---

## Technical Details

### Dependencies
- `pandas` - Data manipulation
- `numpy` - Statistical calculations
- `openpyxl` - Excel file generation with formatting

### Algorithm
1. Read all CSV files with evaluator attribution
2. Normalize Roll No (primary key) and Student Name (fallback)
3. Outer merge all evaluators on Roll No + Name
4. For each criterion:
   - Extract non-blank evaluator scores
   - Compute average (if at least 1 score)
   - Compute variance (if at least 2 scores)
   - Flag if variance > 2
5. Sum averages for Consolidated Total
6. Generate Excel with formatting and conditional highlighting

---

## Contact

For issues or questions about the consolidated evaluation sheet:
- **Coordinator**: Kiran V K
- **In-Charge**: Dr. Sruthy Manmadhan

---

*Generated: 2025-10-24 00:55*
*Version: 1.0*
