# WORKFLOW.md

# Quant Finance Portfolio - Development Workflow

This document describes the end-to-end workflow for expanding this repository in a professional, recruiter-friendly way.

The objective is not simply to write code.

The objective is to build a public portfolio demonstrating skills relevant for:

- Quantitative Support Analyst
- Investment Analyst
- Portfolio Analyst
- Trading Data Analyst
- Financial Data Scientist

---

# Core Principle

Every project should answer:

1. What question am I trying to answer?
2. How did I analyze it?
3. What did I find?
4. Why does it matter?
5. What are the limitations?

The goal is not prediction.

The goal is investment research, portfolio analytics, risk analysis and clear communication.

---

# Overall Workflow

```text
Issue
↓
Branch
↓
Development
↓
Testing
↓
Commit
↓
Push
↓
Pull Request
↓
Review
↓
Merge
↓
Close Issue
```

---

# Repository Setup (One Time Only)

Clone repository:

```bash
git clone https://github.com/cephu-research/quant-support-analyst-portfolio.git
```

Open folder:

```bash
cd quant-support-analyst-portfolio
```

Open in VS Code:

```bash
code .
```

Verify status:

```bash
git status
```

Expected:

```text
On branch main
nothing to commit, working tree clean
```

---

# Weekly Work Rhythm

## Monday

Choose ONE issue.

Move issue to:

```text
In Progress
```

Review requirements.

Define expected deliverable.

---

## Wednesday

Create branch.

Use Claude Code to generate first implementation.

Review output.

Run notebook.

Fix issues.

---

## Saturday

Polish notebook.

Improve explanations.

Add screenshots if relevant.

Commit.

Push.

Create Pull Request.

Merge.

Move issue to:

```text
Published
```

---

# Start Working on an Issue

Always start from latest main branch.

```bash
git switch main
git pull origin main
```

Create dedicated branch.

Example:

```bash
git switch -c feature/issue-3-etf-portfolio-analyzer
```

Branch naming convention:

```text
feature/issue-number-short-description
```

Examples:

```bash
feature/issue-1-improve-readme
feature/issue-2-add-screenshots
feature/issue-3-etf-portfolio-analyzer
feature/issue-6-covered-call-simulator
feature/issue-9-market-regime-classifier
```

---

# Workflow with Claude Code

Open Claude Code inside repository.

Provide issue number and requirements.

Example:

```text
Implement GitHub Issue #3.

Build notebook:

notebooks/09_personal_etf_portfolio_analyzer.ipynb

Requirements:

- Download ETF data using yfinance
- IWDA
- QQQ
- SMH
- GLD
- TLT
- SPY

Calculate:

- Daily returns
- Monthly returns
- CAGR
- Annualized volatility
- Sharpe Ratio
- Max Drawdown

Create:

- Cumulative returns chart
- Correlation matrix
- Drawdown chart
- Risk summary dashboard

Notebook structure:

- Research Question
- Data Source
- Methodology
- Analysis
- Results
- Interpretation
- Limitations

Style:

- Recruiter friendly
- Professional
- Clear markdown explanations
- No investment advice
```

Your role:

Review everything.

Claude writes code.

You validate:

- Logic
- Financial interpretation
- Clarity
- Readability

---

# Testing Checklist

Before committing:

```text
□ Notebook runs from top to bottom
□ No broken cells
□ No missing imports
□ Charts render correctly
□ Results are realistic
□ Markdown sections completed
□ No personal portfolio data
□ No hardcoded local paths
□ No syntax errors
```

Launch Jupyter:

```bash
jupyter notebook
```

or use VS Code Notebook interface.

---

# Reviewing Changes

Check Git status:

```bash
git status
```

Review changes:

```bash
git diff
```

Verify only relevant files changed.

Examples:

```text
notebooks/09_personal_etf_portfolio_analyzer.ipynb
src/performance_metrics.py
README.md
requirements.txt
assets/chart.png
```

---

# Stage Changes

Add files:

```bash
git add .
```

Verify:

```bash
git status
```

Expected:

```text
Changes to be committed
```

---

# Commit Changes

Examples:

```bash
git commit -m "Improve recruiter positioning in README"
```

```bash
git commit -m "Add ETF portfolio analyzer notebook"
```

```bash
git commit -m "Add covered call income simulator"
```

```bash
git commit -m "Add market regime classifier"
```

Guideline:

Commit message should explain what was added.

---

# Push Branch

Push to GitHub:

```bash
git push origin feature/issue-3-etf-portfolio-analyzer
```

First push:

```bash
git push --set-upstream origin feature/issue-3-etf-portfolio-analyzer
```

---

# Create Pull Request

Go to GitHub.

Click:

```text
Compare & Pull Request
```

PR Title:

```text
Add ETF portfolio analyzer notebook
```

PR Description Template:

```markdown
## Summary

Closes #3

This PR adds the Personal ETF Portfolio Analyzer notebook.

## Implemented

- ETF data download
- CAGR calculations
- Volatility calculations
- Sharpe Ratio calculations
- Drawdown analysis
- Correlation matrix
- Investment interpretation
- Limitations section

## Checklist

- [ ] Notebook runs successfully
- [ ] Charts render correctly
- [ ] Results checked
- [ ] Documentation updated
- [ ] No personal data included

## Notes

For educational purposes only.
Not investment advice.
```

Important:

```markdown
Closes #3
```

automatically closes the issue after merge.

---

# Pull Request Review Checklist

Before merging:

```text
□ Files changed are correct
□ No unrelated changes
□ Notebook runs
□ Charts look professional
□ Markdown is clear
□ README updated if required
□ No overclaiming
□ Limitations included
□ No personal account information
```

---

# Merge Pull Request

On GitHub:

```text
Merge Pull Request
↓
Confirm Merge
↓
Delete Branch
```

---

# Update Local Repository After Merge

Switch to main:

```bash
git switch main
```

Pull latest version:

```bash
git pull origin main
```

Verify:

```bash
git status
```

Expected:

```text
nothing to commit
working tree clean
```

---

# Move Issue in Project

After merge:

```text
In Progress
↓
Published
```

Issue should be closed automatically if:

```markdown
Closes #IssueNumber
```

was included.

---

# Recommended Development Order

Priority order:

```text
1. Improve README
2. Add screenshots
3. Personal ETF Portfolio Analyzer
4. QQQ vs IWDA vs SMH Analysis
5. Covered Call Income Simulator
6. Market Regime Classifier
7. ETF Momentum Rotation Model
8. Research Notes
9. Refactor reusable functions into src
10. Dashboard improvements
```

---

# Notebook Standard Template

Every notebook should follow:

```markdown
# Project Title

## Research Question

What am I trying to answer?

## Why It Matters

Why should an investor, trader or analyst care?

## Data Source

Describe source and limitations.

## Methodology

Explain calculations and logic.

## Analysis

Python implementation.

## Results

Key outputs.

## Interpretation

Translate results into plain English.

## Limitations

What are the weaknesses?

## Next Steps

How can this be improved later?

## Disclaimer

Educational purposes only.
Not investment advice.
```

---

# Notebook Quality Checklist

Before publishing:

```text
□ Clear title
□ Research question included
□ Data source documented
□ Clean imports
□ Charts have titles
□ Charts readable
□ Conclusions included
□ Limitations included
□ Next steps included
□ Disclaimer included
□ No broken cells
□ No unused code
```

---

# Reusable Claude Code Prompt

```text
You are helping me build a professional public portfolio for quantitative finance and investment research.

Implement GitHub Issue #[NUMBER].

Requirements:
[PASTE ISSUE DESCRIPTION]

Repository Goal:
Build a recruiter-friendly portfolio for:

- Quantitative Support Analyst
- Investment Analyst
- Portfolio Analyst
- Trading Data Analyst
- Financial Data Scientist

Guidelines:

- Use Python
- Use yfinance where applicable
- Use clean readable code
- Add markdown explanations
- Include business interpretation
- Include limitations
- Avoid overfitting claims
- Avoid black-box predictions
- Not investment advice

Deliverables:

- Notebook
- Supporting functions in src if useful
- Documentation updates where relevant
```

---

# Git Commands Cheat Sheet

Current branch:

```bash
git branch
```

Current status:

```bash
git status
```

Update main:

```bash
git switch main
git pull origin main
```

Create branch:

```bash
git switch -c feature/issue-description
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Description"
```

Push:

```bash
git push
```

Push first time:

```bash
git push --set-upstream origin branch-name
```

View commit history:

```bash
git log --oneline
```

---

# Emergency Procedure

If something looks wrong:

Check:

```bash
git status
```

Check:

```bash
git branch
```

Do not use these commands unless absolutely necessary:

```bash
git reset --hard
git push --force
git rebase
```

Instead ask:

```text
I am on this branch and this is my git status.

What should I do next?
```

Paste:

```bash
git status
git branch
```

---

# Portfolio Positioning Statement

This repository is not a code dump.

The objective is to demonstrate:

- Finance knowledge
- Python skills
- Investment research
- Portfolio analytics
- Risk management
- Clear communication
- Data science fundamentals

Professional positioning:

"Finance professional using Python to analyze markets, portfolios, risk and options strategies."

---

# Final Rule

Focus on consistency.

A finished notebook is better than a perfect unfinished framework.

Target pace:

```text
1 completed issue per week
4 projects per month
12 portfolio projects in 3 months
```

Build evidence.

Publish regularly.

Think like an Investment Analyst with Python, not like a student doing coding exercises.
