# Excel & Financial Modeling — Study Notes

**Owner:** Muhammed Ashnad  
**Tutor:** Claude  
**Purpose:** Cumulative textbook — every concept taught, every example used, every practice question with answers. Use this to revise without needing the chat history.  
**Last Updated:** 2026-08-24  
**Rule:** Updated every session during or immediately after teaching. No exceptions.

---

## How to Use This

- Read the **Concept** section first — understand the *why* before the *how*
- Study the **Syntax** and **Example** sections — know what each argument does
- Work through **Practice Questions** without looking at answers first
- Check your answers only after you've attempted every question
- If you got something wrong, re-read the concept and try a variant yourself

---

## Chapter 1: SUMIFS

### Concept

SUMIFS answers the question: *"Give me the total of a column, but only for rows that match these specific conditions."*

In FP&A you use this constantly:
- Total revenue for Dubai, Q2 only
- Total salaries for the Sales department in January
- Total commissions where commission > AED 10,000

The difference from a plain SUM: SUMIFS can filter by multiple conditions at once. You're not summing a whole column — you're summing a precise slice of it.

### Syntax

```
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2, ...)
```

| Argument | What it means |
|---|---|
| `sum_range` | The column of numbers you want to add up |
| `criteria_range1` | The column to check the first condition against |
| `criteria1` | The value that must match in criteria_range1 |
| More pairs | Add as many criteria range/value pairs as you need |

**Key rule:** Every argument after `sum_range` comes in pairs — range, then value. Always.

### Example

Data: monthly spend by Region, Department, Category.

```
=SUMIFS(F5:F34, C5:C34, "Dubai", D5:D34, "Sales", A5:A34, "Jan")
```

Reads as: *Sum column F (Amount), but only where column C is "Dubai" AND column D is "Sales" AND column A is "Jan".*

### Operators in criteria

You can use comparison operators inside quotes:

```
=SUMIFS(F5:F34, F5:F34, ">10000")      ← sum amounts that are greater than 10,000
=SUMIFS(F5:F34, F5:F34, "<>"&"")       ← sum non-blank amounts
=SUMIFS(F5:F34, A5:A34, ">="&DATE(2025,1,1))  ← sum amounts from Jan 2025 onwards
```

### Practice Questions

**Dataset:** Zara & Co. UAE — `01_SUMIFS_practice.xlsx`  
Columns: Month | Quarter | Region | Department | Category | Amount (AED)  
30 rows: Jan–Jun 2025, Dubai and Abu Dhabi, Sales/Marketing/Finance departments.

---

**Q1.** Total Commission paid across ALL months.  
**Answer:** 60,000  
**Formula:** `=SUMIFS(F5:F34, E5:E34, "Commission")`

---

**Q2.** Total spend in Abu Dhabi across ALL months and departments.  
**Answer:** 237,500  
**Formula:** `=SUMIFS(F5:F34, C5:C34, "Abu Dhabi")`

---

**Q3.** Total Salaries paid in Q1 (all regions, all departments).  
**Answer:** 510,000  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q1", E5:E34, "Salaries")`

---

**Q4.** Total Commission for Dubai Sales in February.  
**Answer:** 12,000  
**Formula:** `=SUMIFS(F5:F34, E5:E34, "Commission", C5:C34, "Dubai", A5:A34, "Feb")`

---

**Q5.** Total Advertising spend in Q2 (all regions).  
**Answer:** 27,500  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q2", E5:E34, "Advertising")`

---

**Q6.** Total Finance Salaries in Q1.  
**Answer:** 84,000  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q1", D5:D34, "Finance", E5:E34, "Salaries")`

---

**Q7.** Total Sales spend (all categories) in Abu Dhabi for March.  
**Answer:** 38,000  
**Formula:** `=SUMIFS(F5:F34, C5:C34, "Abu Dhabi", D5:D34, "Sales", A5:A34, "Mar")`

---

**Q8.** Total Salaries in Dubai Sales department in Q2.  
**Answer:** 168,000  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q2", C5:C34, "Dubai", D5:D34, "Sales", E5:E34, "Salaries")`

---

**Q9.** Total Marketing Advertising spend in Abu Dhabi for Q1.  
**Answer:** 55,000  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q1", C5:C34, "Abu Dhabi", D5:D34, "Marketing", E5:E34, "Advertising")`

---

**Q10.** Total Commission in Dubai in months where commission > AED 10,000.  
**Answer:** 33,000  
**Formula:** `=SUMIFS(F5:F34, C5:C34, "Dubai", E5:E34, "Commission", F5:F34, ">10000")`

---

**Q11.** Which quarter had higher total spend — Q1 or Q2? Prove it with SUMIFS.  
**Answer:** Q1 = 583,500 | Q2 = 297,000 → Q1 higher  
**Formula:** `=SUMIFS(F5:F34, B5:B34, "Q1")` and `=SUMIFS(F5:F34, B5:B34, "Q2")`

---

**Q12.** What percentage of total spend is Dubai vs Abu Dhabi? Use SUMIFS + division.  
**Answer:** Dubai ≈ 71% | Abu Dhabi ≈ 29%  
**Formula:** `=SUMIFS(F5:F34, C5:C34, "Dubai") / SUM(F5:F34)` → format as %

---

### Common Mistakes

- **Wrong argument order:** Always `sum_range` first, then criteria pairs. Swapping them gives wrong results or errors.
- **Missing the closing pair:** If you open a criteria range, you must immediately follow with the criteria value. An odd number of arguments after `sum_range` = error.
- **Text criteria without quotes:** `"Dubai"` not `Dubai`. Numbers and operators also go in quotes when used as text: `">10000"`.

---

## Chapter 2: VLOOKUP

### Concept

VLOOKUP answers: *"Look up this value in a table, and return something from a column to its right."*

Classic FP&A use:
- Look up a product code and return its price
- Look up an employee ID and return their department
- Look up a month name and return the budget for that month

The limitation (important): VLOOKUP can only look **right** — the lookup column must be the leftmost column in your range. If you need to look left, use INDEX-MATCH (Chapter 3).

### Syntax

```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

| Argument | What it means |
|---|---|
| `lookup_value` | The value you're searching for (a cell reference or text) |
| `table_array` | The entire table to search (always lock with $ when filling down) |
| `col_index_num` | Which column number to return (1 = first column, 2 = second, etc.) |
| `[range_lookup]` | FALSE = exact match (always use FALSE in finance) |

**Non-negotiable habit:** Always use `FALSE` as the fourth argument. `TRUE` (approximate match) gives unpredictable results and has no use in financial data.

### Example

Lookup table in columns A–C: Product Code | Product Name | Unit Price

```
=VLOOKUP(E2, $A$2:$C$50, 3, FALSE)
```

Reads as: *Find the value in E2 within column A of the range A2:C50. Return column 3 (Unit Price) of the matching row. Exact match only.*

**Why lock with $:** When you fill the formula down, the table range must not shift. `$A$2:$C$50` stays fixed; `E2` moves down correctly to `E3`, `E4`, etc.

### Practice Questions

**Dataset:** `02_vlookup_practice.xlsx` — UAE retail transaction data with a separate lookup table.

---

**Q1.** You have a transaction list with Product Codes. Use VLOOKUP to return the Product Name for each transaction.  
*(Single lookup, leftmost column → one column right)*

---

**Q2.** Return the Unit Price for each transaction from the lookup table.  
*(Single lookup, leftmost column → two columns right)*

---

**Q3.** A new product code appears that doesn't exist in the lookup table. What does VLOOKUP return? How do you handle it?  
**Answer:** Returns `#N/A`. Wrap with IFERROR: `=IFERROR(VLOOKUP(...), "Not found")`

---

**Q4.** You're filling the VLOOKUP formula down 40 rows. After row 5 the results go wrong — all returning the same wrong value. What's the likely cause?  
**Answer:** The table_array range was not locked with $. Fix: `$A$2:$C$50` not `A2:C50`.

---

**Q5.** Return the Category for each product. The Category column is 4 columns to the right of the Product Code column.  
*(Practice counting col_index_num correctly)*

---

### Common Mistakes

- **Forgetting FALSE:** Default is approximate match — silently returns wrong results on unsorted data.
- **Unlocked table_array:** Formula drifts when filled down.
- **Col_index_num off by one:** Count from column 1 (the lookup column), not from column A.
- **VLOOKUP for left lookups:** Cannot look left. If your return column is to the left of your lookup column, use INDEX-MATCH.

---

## Chapter 3: INDEX-MATCH & IFERROR

### Concept — INDEX-MATCH

INDEX-MATCH is two functions used together to replace VLOOKUP — and it's more powerful because it can look in any direction.

**INDEX:** Returns the value at a specific row and column in a range.  
**MATCH:** Returns the position (row number) of a value within a range.

Combined: MATCH finds the row. INDEX returns the value at that row.

**Why it beats VLOOKUP:**
1. Can look left (return a column that's to the *left* of the lookup column)
2. Doesn't break when you insert columns (VLOOKUP's col_index_num is a hardcoded number — if you insert a column, it's wrong)
3. Slightly faster on large datasets

### Syntax

```
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

| Part | What it does |
|---|---|
| `return_range` | The column you want to return values from |
| `lookup_value` | What you're searching for |
| `lookup_range` | The column to search in |
| `0` | Exact match (always 0 in finance — same as FALSE in VLOOKUP) |

### Example

Lookup table: Column A = Employee ID, Column B = Employee Name, Column C = Department.

VLOOKUP can return Name (col 2) or Department (col 3) given an ID.  
But if you want to return the Employee ID given a Name, VLOOKUP fails — ID is *left* of Name.

INDEX-MATCH handles it:

```
=INDEX(A2:A50, MATCH("Ahmed Al Rashid", B2:B50, 0))
```

Reads as: *Find "Ahmed Al Rashid" in column B. Return the value in column A at that same row.*

### Concept — IFERROR

IFERROR wraps any formula and returns a custom value if the formula produces an error.

```
=IFERROR(formula, value_if_error)
```

**Why it matters:** Models with `#N/A` or `#REF!` errors look unprofessional and break downstream calculations. IFERROR keeps the model clean.

**Usage in finance:**
```
=IFERROR(INDEX(A2:A50, MATCH(E2, B2:B50, 0)), "Employee not found")
=IFERROR(D2/C2, 0)        ← handles divide-by-zero in margin calculations
=IFERROR(VLOOKUP(...), 0) ← returns 0 instead of #N/A when no match
```

### Practice Questions

**Dataset:** `04_index_match_practice.xlsx` — Zara & Co. Finance Team (fictional)  
**Sheet:** Data (rows 6–35)  
**Columns:** A = Employee_ID | B = Name | C = Department | D = Role | E = Salary (AED) | F = Location  
**30 employees** across Finance, FP&A, Treasury, Accounting, Internal Audit  
**Important:** Data is intentionally NOT sorted by Employee ID — MATCH must actually search.

---

**Q1 (Level 1).** Employee ID E-008. Return their full Name.  
*(Right lookup — same direction as VLOOKUP, but use INDEX-MATCH syntax.)*  
**Answer:** Aisha Al Hamdan  
**Formula:** `=INDEX(Data!B6:B35, MATCH("E-008", Data!A6:A35, 0))`

---

**Q2 (Level 1).** Return the Department for Employee ID E-015.  
**Answer:** Finance  
**Formula:** `=INDEX(Data!C6:C35, MATCH("E-015", Data!A6:A35, 0))`

---

**Q3 (Level 1).** Return the Salary (AED) for Employee ID E-022.  
**Answer:** 16,000  
**Formula:** `=INDEX(Data!E6:E35, MATCH("E-022", Data!A6:A35, 0))`

---

**Q4 (Level 2 ★ — Left lookup).** You know the name is "Omar Hassan Al Farsi". Return their Employee ID.  
Employee ID is in column A — to the LEFT of the Name column. VLOOKUP cannot do this.  
**Answer:** E-003  
**Formula:** `=INDEX(Data!A6:A35, MATCH("Omar Hassan Al Farsi", Data!B6:B35, 0))`

*This is the key question that proves INDEX-MATCH > VLOOKUP. The lookup column (Name, col B) is to the right of the return column (ID, col A). VLOOKUP requires the lookup column to be leftmost — so it fails here. INDEX-MATCH doesn't care about direction.*

---

**Q5 (Level 2 ★).** Given the name "Priya Nair", return their Role.  
**Answer:** Senior Analyst  
**Formula:** `=INDEX(Data!D6:D35, MATCH("Priya Nair", Data!B6:B35, 0))`

---

**Q6 (Level 2 ★).** Given the name "James Mitchell", return their Location.  
**Answer:** Abu Dhabi  
**Formula:** `=INDEX(Data!F6:F35, MATCH("James Mitchell", Data!B6:B35, 0))`

---

**Q7 (Level 3 — IFERROR).** Employee ID "E-099" does not exist. Write INDEX-MATCH wrapped in IFERROR to return "Employee not found" instead of #N/A.  
**Answer:** Employee not found  
**Formula:** `=IFERROR(INDEX(Data!B6:B35, MATCH("E-099", Data!A6:A35, 0)), "Employee not found")`

---

**Q8 (Level 3 — IFERROR).** Return the Salary for "Khalid Al Suwaidi". Wrap in IFERROR so that if the name is mistyped and not found, the cell shows 0 instead of an error.  
**Answer:** 25,000 (or 0 if name wrong)  
**Formula:** `=IFERROR(INDEX(Data!E6:E35, MATCH("Khalid Al Suwaidi", Data!B6:B35, 0)), 0)`

---

**Q9 (Level 4 ★★).** Find the NAME of the highest-paid employee in the entire company.  
*Hint: combine INDEX-MATCH with MAX().*  
**Answer:** Shaikha Al Muhairi (45,000 AED)  
**Formula:** `=INDEX(Data!B6:B35, MATCH(MAX(Data!E6:E35), Data!E6:E35, 0))`

*How it works: MAX(Data!E6:E35) returns 45,000. MATCH finds which row has 45,000 in the Salary column. INDEX returns the Name at that row.*

---

**Q10 (Level 4 ★★).** Find the NAME of the highest-paid employee in the FP&A department only.  
**Answer:** Patrick O'Brien (42,000 AED)  
**Formula:** `=INDEX(Data!B6:B35, MATCH(MAXIFS(Data!E6:E35, Data!C6:C35, "FP&A"), Data!E6:E35, 0))`

*MAXIFS is like SUMIFS but returns the maximum instead of a sum. It finds the highest salary where Department = "FP&A", then MATCH+INDEX returns the name for that salary.*

---

**Q11 (Level 4 ★★).** How many employees are in each department? Use COUNTIF for each of the 5 departments. Then use INDEX-MATCH to look up the count for any department name typed in a cell.  
**Answer:** Finance=7, FP&A=6, Treasury=6, Accounting=6, Internal Audit=5  
**Formula (COUNTIF):** `=COUNTIF(Data!C6:C35, "Finance")` — repeat for each department  
**Formula (INDEX-MATCH on summary table):** Build a 2-column summary (Department | Count), then `=INDEX(summary_count_col, MATCH(lookup_dept, summary_dept_col, 0))`

---

**When to use IFERROR:**
- Any lookup where the lookup value might not exist in the table
- Division formulas where the denominator might be zero: `=IFERROR(D2/C2, 0)`
- Any formula that could return `#N/A`, `#REF!`, `#DIV/0!`, `#VALUE!`
- In financial models: always. A model with visible errors is unprofessional and breaks downstream calculations.

---

## Chapter 4: Power Query

### Concept

Power Query is Excel's built-in data import and transformation engine. Instead of manually cleaning data (copy-paste, find-replace, delete columns), you record the steps once. When the source data updates, you click **Refresh** and Excel reruns all your steps automatically.

**Why finance uses it:**
- Raw data from ERPs (Odoo, SAP, Oracle) is never clean — wrong column names, merged cells, totals rows mixed in, dates stored as text
- Power Query cleans it once, reproducibly
- Monthly reporting: swap the source file, hit refresh, model updates in seconds

**Where to find it:** Data tab → Get Data → From File → From Text/CSV (or From Workbook)

### The Standard Workflow

Every Power Query session follows the same sequence:

```
1. Connect to source (CSV, Excel, SharePoint, database)
2. Promote first row as headers
3. Filter out junk rows (blank rows, TOTAL rows, headers repeated mid-file)
4. Remove unnecessary columns
5. Rename columns to clean names
6. Fix data types (dates as dates, numbers as numbers — not text)
7. Unpivot if needed (turn wide monthly columns into tall rows)
8. Load to Excel table
```

### Key Operations

**Promote headers:** The first row of data contains the column names. Right-click the top-left icon → Use First Row as Headers.

**Filter junk rows:** Click the dropdown on any column → Text Filters → Does Not Equal → type "TOTAL" or blank. Repeat for any other junk.

**Remove columns:** Select columns to remove → Right-click → Remove Columns. Or: select columns to *keep* → Right-click → Remove Other Columns.

**Rename columns:** Double-click the column header in the query editor.

**Fix data types:** Click the data type icon (ABC for text, 123 for numbers, calendar for dates) on each column header → select correct type.

**Unpivot:** Select the columns you want to unpivot → Right-click → Unpivot Columns. Turns this:

| Outlet | Jan | Feb | Mar |
|---|---|---|---|
| Dubai | 50,000 | 48,000 | 55,000 |

Into this:

| Outlet | Month | Revenue |
|---|---|---|
| Dubai | Jan | 50,000 |
| Dubai | Feb | 48,000 |
| Dubai | Mar | 55,000 |

The "tall" format is what Pivot Tables and SUMIFS need.

**Load to table:** Close & Load → Close & Load To → Table → specify cell.

### Critical Rule

**Never open a source CSV in Excel before importing it via Power Query.**

When Excel opens a CSV, it auto-converts some values. Column headers that look like dates (Jan-25, Feb-25) get converted to date serial numbers (45657, etc.). Power Query then reads corrupted headers. Always use a plain text editor (TextEdit, VS Code, Notepad) to inspect CSVs, never Excel.

### Refresh

When source data changes:
- Data tab → Refresh All (refreshes all queries in the workbook)
- Or right-click the output table → Refresh

### Practice Workflow

**Dataset:** `03_powerquery_raw.csv` — UAE retail revenue data, wide format (monthly columns, mixed junk rows).

**Task:** Import the CSV, clean it, unpivot the monthly columns, load to a table.

**Expected output:** 54 rows × 4 columns: Outlet | Category | Month | Revenue

**Steps you completed without guidance:**
1. Data → Get Data → From File → From Text/CSV → selected 03_powerquery_raw.csv
2. Promoted headers
3. Filtered out blank rows and TOTAL rows
4. Removed unnecessary columns
5. Renamed headers to clean names
6. Fixed data types
7. Selected the 6 monthly columns → Unpivot Columns
8. Loaded to table — output: 54 rows × 4 columns ✅

---

## Chapter 5: Pivot Tables

### Concept

A Pivot Table is a summary tool that lets you aggregate, group, and slice data without writing formulas. You drag fields into rows, columns, and values — Excel calculates the totals.

**Why finance uses it:**
- Instant revenue by outlet, by month, by category
- Quick variance analysis without building formulas
- Slicers make reports filterable without touching the data
- Calculated fields add custom metrics (e.g. Gross Margin %) directly in the Pivot

**The input must be a proper table:** One header row, no blank rows, no merged cells, no total rows in the middle. Power Query output is perfect for this.

### Building a Pivot Table

1. Click anywhere in your data table
2. Insert → PivotTable → New Worksheet (or Existing Worksheet)
3. In the Field List panel on the right: drag fields into Rows, Columns, Values, Filters
4. Values default to SUM for numbers, COUNT for text — change by clicking the field → Value Field Settings

### Key Operations

**Slicers:** Insert → Slicer → select a field. Click values on the slicer to filter the Pivot. Hold Ctrl to select multiple values.

**Date grouping:** Drag a date field into Rows → Right-click any date value → Group → select Month, Quarter, or Year (can select multiple). Excel creates automatic grouping levels.

**Calculated field:** PivotTable Analyze tab → Fields, Items & Sets → Calculated Field → give it a name (e.g. "Gross Margin %") → write the formula using field names: `= (Revenue - COGS) / Revenue` → OK. Format the new field as a percentage.

**Refresh Pivot:** When source data changes, right-click inside the Pivot → Refresh (or Data → Refresh All).

### Practice Questions

**Dataset:** `05_pivottable_practice.xlsx` — UAE retail transactions, Jan–Jun 2025  
Columns: Date | Outlet | Category | Product | Units_Sold | Unit_Price | Revenue | COGS  
108 rows, 3 outlets (Dubai Mall, Marina Mall, Online), 3 categories (Apparel, Accessories, Footwear)

---

**Q1.** Build a Pivot Table showing total Revenue by Outlet (one outlet per row, Revenue in Values). What is the total for all outlets combined?  
*(Build from scratch, no guidance)*

---

**Q2.** Add a Category slicer to the Pivot Table. Filter to Dubai Mall and Marina Mall only (deselect Online). Read the combined total.  
**Answer:** 301,110 *(exact value from the session — your practice file)*

---

**Q3.** Remove the slicer filter. Drag Date into Rows. Group the dates by Quarter and Month. What does the Pivot now show?  
**Answer:** Each quarter expands into months. Revenue is subtotalled by quarter, then totalled at bottom.

---

**Q4.** Add a Calculated Field called "Gross Margin %" with the formula `= (Revenue - COGS) / Revenue`. Format it as a percentage. What is the gross margin for Accessories?  
*(Hint: PivotTable Analyze → Fields, Items & Sets → Calculated Field)*

---

**Q5. Full build (no guidance):** Build a complete Pivot Table from scratch with:
- Rows: Quarter, then Month (grouped)
- Columns: Outlet (Dubai Mall | Marina Mall | Online)
- Values: Revenue AND Gross Margin %
- Category slicer

Can you reproduce this without any hints?  
**Answer from session:** You rebuilt this correctly from scratch — all layout correct, slicer functional, GM% formatted as %. ✅

---

## Chapter 6: Charts for Finance

### Concept

Finance charts have one job: communicate a number clearly. Not impress people visually. Every chart element should earn its place — if it doesn't add information, remove it.

**The two most important chart types in FP&A:**
1. **Column chart** — comparing values across categories (Budget vs Actual by outlet)
2. **Waterfall chart** — showing how components add up to a total (Budget → variances → Actual)

### Column Chart (Budget vs Actual)

**When to use:** Comparing two or more values for the same categories side by side.

**How to build:**
1. Set up a table with Outlet | Budget | Actual (3 rows of data, 3 outlets)
2. Select the table → Insert → Bar/Column Chart → Clustered Column
3. Format:
   - Remove gridlines (click gridlines → Delete)
   - Add data labels (right-click bars → Add Data Labels → format as comma, no decimals)
   - Change Budget bars to grey (`#808080`) — Budget is reference, not the hero
   - Change Actual bars to dark blue (`#1e3a5f`) — the main story
   - Remove legend if the colour makes it obvious from the chart title
   - Title: "Budget vs Actual Revenue by Outlet (AED)"

**Professional rule:** Budget is always grey or lighter. Actual is the darker/bolder colour. The eye should land on Actual first.

### Waterfall Chart (Variance Bridge)

**When to use:** Showing how you get from one total to another via a series of increases and decreases. Classic use: Budget → [outlet variances] → Actual.

**How to build:**
1. Set up a table: Label | Value
   - Budget | 540,000 (the starting total)
   - Dubai Mall | 70,000 (positive variance — increased actual vs budget)
   - Marina Mall | -40,000 (negative variance)
   - Online | 30,000 (positive variance)
   - Actual | 600,000 (the ending total)
2. Select the table → Insert → Waterfall Chart
3. **Critical step:** Right-click the Budget bar → Set as Total. Right-click the Actual bar → Set as Total.
   - Without this: Excel treats Budget and Actual as chain steps, not anchors. The chart will be wrong.
4. Format:
   - Remove gridlines
   - Add data labels (comma format)
   - Colour: increases green, decreases red (Excel does this automatically)
   - Title: "Revenue Variance Bridge: Budget to Actual (AED)"

**Why "Set as Total":** Budget and Actual are anchor bars — absolute values, not movements. The outlet values are movements (how much each outlet moved the total). Set as Total tells Excel: "start the chain fresh here" and "land here at the end."

### Practice (Session 13 — built both charts)

**Column chart:** 3 outlets × Budget vs Actual. Formatted: no gridlines, comma labels, grey Budget / dark blue Actual. ✅

**Waterfall chart:** Budget (540,000) → Dubai Mall (+70k) → Marina Mall (-40k) → Online (+30k) → Actual (600,000). Set as Total on Budget and Actual. Green/red fills. ✅

---

## Chapter 7: Modeling Best Practices

### Concept

A financial model is a tool someone else needs to trust. That means they must be able to:
1. **Audit it** — trace every number back to a source
2. **Update it** — change one input and have everything recalculate correctly
3. **Hand it to someone else** — another analyst can maintain it without asking you questions

None of that works if numbers are hardcoded inside formulas, scattered across tabs, or unlabelled.

**The core rule:**

> Every hardcoded number lives in exactly one place. Everything else is a formula pointing to that place.

### The Three-Tab Structure

This is the standard architecture for any FP&A model:

| Tab | What it contains | Rule |
|---|---|---|
| **Assumptions** | All inputs — growth rates, margins, costs, volumes | The only place you type numbers. One number, one cell. |
| **Calculations** | All formulas that reference Assumptions | Never type a number here. Every cell is a formula. |
| **Output / Summary** | Clean results for reading and presenting | Never type anything here. Reads from Calculations. |

**Why this matters:** If the growth rate changes from 10% to 12%, you change one cell in Assumptions. Every formula across every tab recalculates automatically. If you'd hardcoded 1.10 in 30 formulas, you'd need to find all 30.

### Color Coding Convention

Standard across professional FP&A teams in UAE and globally:

| Color | Meaning | Where |
|---|---|---|
| **Blue font** | Hardcoded input — you typed this number | Assumptions tab only |
| **Black font** | Formula — calculated, never type here | Calculations and Output tabs |
| **Green font** | Linked from another sheet — formula referencing a different tab | Any tab |

When you open a model and see a blue cell, you know: this is an input, this is what drives the model. When you see black, you know: don't touch, it's a formula.

### Named Ranges

Instead of writing:

```
=Assumptions!B4 * (1 + Assumptions!B5)
```

You name the cells:
- `Assumptions!B4` → name it `Base_Revenue`
- `Assumptions!B5` → name it `Growth_Rate`

Now the formula reads:

```
=Base_Revenue * (1 + Growth_Rate)
```

This is auditable, readable, and won't break if you move the cell.

**How to create a named range:**
1. Click the cell you want to name
2. Click the Name Box (top-left, normally shows the cell address like B4)
3. Type your name — no spaces, use underscores: `Growth_Rate`
4. Press Enter

**Naming conventions:**
- No spaces (use underscores)
- Descriptive: `FY2025_Revenue_Budget` not `Rev`
- Consistent: if you prefix with year, do it everywhere

### Structured Table References

When data is in an Excel Table (Insert → Table), you can reference columns by name:

```
=SUM(RevenueTable[Revenue])        ← expands automatically as rows are added
```

vs.

```
=SUM(A2:A100)                      ← breaks when you insert rows or extend data
```

In FP&A models with refreshing data (Power Query output), always use table references — they never go stale.

### The "Never Hardcode in a Formula" Rule

**Bad:**
```
=B4 * 1.15     ← where did 1.15 come from? What does it mean?
```

**Good:**
```
=B4 * (1 + Growth_Rate)    ← Growth_Rate is defined in Assumptions, documented, changeable
```

Even for something as simple as VAT (5%): put it in Assumptions as `VAT_Rate = 5%`, then reference it everywhere. When UAE changes the VAT rate, you change one cell.

### Practice Build — 3-Tab Skeleton

**File:** `06_Model_Structure_practice.xlsx` (to be created this session)

**Build instructions:**

**Tab 1 — Assumptions** (blue font for all input values)

| | A | B |
|---|---|---|
| 1 | **Assumptions** | |
| 2 | Base Revenue (AED) | 1,000,000 |
| 3 | Growth Rate | 10% |
| 4 | Profit Margin | 20% |

Name the cells: B2 = `Base_Revenue`, B3 = `Growth_Rate`, B4 = `Profit_Margin`

**Tab 2 — Calculations** (black font — formulas only, no hardcoded numbers)

| | A | B | C | D |
|---|---|---|---|---|
| 1 | | Year 1 | Year 2 | Year 3 |
| 2 | Revenue | `=Base_Revenue` | `=B2*(1+Growth_Rate)` | `=C2*(1+Growth_Rate)` |
| 3 | Profit | `=B2*Profit_Margin` | `=C2*Profit_Margin` | `=D2*Profit_Margin` |

**Tab 3 — Output** (links from Calculations — reads, never calculates)

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Summary** | Year 1 | Year 2 | Year 3 |
| 2 | Revenue (AED) | `=Calculations!B2` | `=Calculations!C2` | `=Calculations!D2` |
| 3 | Profit (AED) | `=Calculations!B3` | `=Calculations!C3` | `=Calculations!D3` |
| 4 | Profit Margin % | `=B3/B2` | `=C3/C2` | `=D3/D2` |

**Test:** Change Growth_Rate in Assumptions from 10% to 15%. Revenue in Year 2, Year 3, and all Output cells should update automatically without touching any other cell.

---

---

## Chapter 8: Conditional Formatting

### Concept

Conditional Formatting (CF) changes how a cell looks based on its value — automatically. You set the rules once; Excel updates the colours every time the data changes.

In FP&A this is not decoration. It is a signal layer on top of your numbers:
- A variance table where red/green updates live as actuals come in
- An entire row lighting up when a line item breaches a threshold
- Traffic lights that tell a CFO which KPIs need attention without reading every number

The skill is not clicking the menu — it's knowing which of the four rule types to use and when.

### The Four Types

| Type | What it does | When to use |
|---|---|---|
| **Highlight Cell Rules** | Colour individual cells — less than, greater than, equal to, between, text contains | Single-column variance colouring |
| **Data Bars** | Horizontal bar inside the cell — length proportional to value | Comparing budget sizes at a glance |
| **Icon Sets** | Traffic lights, arrows, flags based on thresholds you set | KPI dashboards, variance % status |
| **Custom Formula Rule** | Evaluate any formula — colour whatever range the formula returns TRUE for | Highlighting entire rows, cross-column logic |

### Important: Always Edit the Default Thresholds for Icon Sets

Excel defaults to percentile-based splits (33rd, 67th percentile of the selected data). This is almost always wrong for finance. The default depends on your data range, so it changes every time data changes.

**Always change to Number:**
- Manage Rules → Edit Rule → change "Percent" dropdowns to "Number"
- Type your actual thresholds (e.g. 0 and -0.05 for a ±5% rule)

### The $ Anchor Rule for Custom Formula Rules

**Why CF needs $ when a normal formula doesn't:**

When you write a formula in one cell, Excel evaluates it once. When CF applies a custom formula rule to a **multi-column range** (e.g. A5:E12), it re-evaluates the formula for every cell individually — shifting the reference exactly like fill-right does.

**Without $ column lock — what goes wrong:**

Formula: `=E5<-0.10` applied to A5:E12

| CF evaluates cell... | Formula shifts to... | Result |
|---|---|---|
| A5 | `=E5<-0.10` | Checks E5 ✓ |
| B5 | `=F5<-0.10` | Checks F5 — wrong column ✗ |
| C5 | `=G5<-0.10` | Checks G5 — wrong column ✗ |

**With $ column lock — correct:**

Formula: `=$E5<-0.10` applied to A5:E12

| CF evaluates cell... | Formula becomes... | Result |
|---|---|---|
| A5 | `=$E5<-0.10` | Checks E5 ✓ |
| B5 | `=$E5<-0.10` | Still checks E5 ✓ |
| C5 | `=$E5<-0.10` | Still checks E5 ✓ |

The column E is locked. The row is NOT locked — as CF moves down rows, `=$E5` becomes `=$E6`, `=$E7`, etc., checking the right row each time.

**The rule:**
> Lock the column you're checking (`$E`). Never lock the row. If you lock both (`$E$5`), every row checks the same cell — either all rows light up or none do.

### Practice — File: `07_conditional_formatting_practice.xlsx`

**Data:** Zara & Co. P&L Variance, Jan 2025 — 8 rows (Revenue through EBITDA), columns: Line Item / Budget / Actual / Variance AED / Variance %

Formulas already in place:
- Column D: `=C-B` (Variance AED = Actual − Budget)
- Column E: `=IFERROR(D/B, 0)` (Variance %)

---

**Task 1 — Highlight Cell Rules on D5:D12**

Apply three rules to the Variance (AED) column:

| Condition | Fill | Font |
|---|---|---|
| `< 0` (negative) | Red `#FFC7CE` | Dark red `#9C0006` |
| `> 0` (positive) | Green `#C6EFCE` | Dark green `#276221` |
| `= 0` (zero) | Yellow `#FFEB9C` | Dark yellow `#9C6500` |

**Steps:** Select D5:D12 → Home → Conditional Formatting → Highlight Cells Rules → Less Than / Greater Than / Equal To → Custom Format for each.

**Expected result:**

| Row | Variance AED | Colour |
|---|---|---|
| Revenue | -20,000 | Red |
| COGS | +25,000 | Green |
| Gross Profit | -45,000 | Red |
| Salaries | -2,000 | Red |
| Marketing | +21,000 | Green |
| Rent | 0 | Yellow |
| Other OpEx | +11,000 | Green |
| EBITDA | -64,000 | Red |

---

**Task 2 — Data Bars on B5:B12**

Select B5:B12 → Conditional Formatting → Data Bars → Blue Data Bar.

Revenue (500,000) gets the longest bar. Other OpEx and EBITDA (20,000 each) get the shortest. No formula needed — Excel scales automatically.

---

**Task 3 — Icon Sets on E5:E12 (Variance %)**

Apply 3 Traffic Light icons, then edit the thresholds:

| Icon | Threshold |
|---|---|
| Green circle | >= `0` |
| Yellow circle | >= `-0.05` |
| Red circle | everything below (automatic) |

**Critical step:** After applying, go to Manage Rules → Edit Rule → change both dropdowns from "Percent" to **"Number"** → type `0` and `-0.05`.

**Expected result:**

| Row | Variance % | Icon |
|---|---|---|
| Revenue | -4.0% | Yellow (between -5% and 0%) |
| COGS | 12.5% | Green |
| Gross Profit | -15.0% | Red |
| Salaries | -1.3% | Yellow |
| Marketing | 42.0% | Green |
| Rent | 0.0% | Green |
| Other OpEx | 55.0% | Green |
| EBITDA | -320.0% | Red |

---

**Task 4 ★ — Custom Formula Rule on A5:E12 (entire row)**

If Variance % (column E) is worse than -10%, highlight the **entire row** light red.

**Steps:**
1. Select A5:E12
2. Conditional Formatting → New Rule → "Use a formula to determine which cells to format"
3. Formula: `=$E5<-0.10`
4. Format → Fill → light red `#FFD7D7`

**Expected result:** Gross Profit row (-15%) and EBITDA row (-320%) highlighted light red across all 5 columns. Revenue (-4%) does NOT trigger — it's only -4%, above the -10% threshold.

**Common mistakes:**

| Formula used | What happens | Why wrong |
|---|---|---|
| `=E5<-0.10` | Columns B, C, D, E check wrong columns | No $ — reference shifts right as CF scans across columns |
| `=$E$5<-0.10` | Either all rows light up or none | Both locked — every row checks row 5 only |
| `=$E5<-0.10` | Correct | Column locked, row moves — checks E5, E6, E7... per row |

---

*Next: Day 14 Sign-off Check → CHECKPOINT 2A-4 (Phase 2A Complete)*
