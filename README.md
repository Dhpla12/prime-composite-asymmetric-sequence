# Prime-Composite Asymmetric Sequence

An experimental integer sequence defined by the least positive integer \(k\) such that:

- \(n-k\) is prime  
- \(n+k\) is composite  

for each integer \(n \ge 3\).

This repository contains code, computational data, visualizations, and manuscript files related to the sequence.

---

## Definition

Let \(a(n)\) denote the least positive integer \(k\) satisfying:

\[
a(n)=\min \{k \ge 1 : n-k \text{ is prime and } n+k \text{ is composite}\}
\]

for all integers \(n \ge 3\).

---

## Initial Terms

For \(n=3,4,5,\dots\):


1,2,3,3,2,1,6,5,4,9,2,1,10,5,4,7,2,1,4,3,4,1,2,7,8,5,6,19,...


---

## Computational Results (up to 100000)

| Statistic          | Value   |
| ------------------ | ------- |
| Mean               | 11.0621 |
| Median             | 8       |
| Minimum            | 1       |
| Maximum            | 134     |
| Standard Deviation | 10.2241 |

No exceptions were found for (3 $\\le$ n $\\le$ 100000).

---

## Repository Contents

* `main.py` — Python implementation
* `sequence_results_100000.csv` — computed values
* `plots/` — scatter plot and histogram
* `paper.tex` — LaTeX manuscript
* `paper.pdf` — compiled manuscript

---

## Visualizations

### Scatter Plot

Shows values of (a(n)) for tested integers.

### Histogram

Shows empirical distribution of computed values.

---

## Possible Questions

* Does (a(n)) exist for every (n $\\ge$ 3)?
* Is the sequence unbounded?
* What is the average growth rate?
* How often does (a(n)=1)?

---

## OEIS Status

At the time of writing, searches using initial terms returned no exact OEIS match.

---

## Author

**Aradhya Haldikar**

Independent student researcher interested in mathematics, programming, and computational exploration.

