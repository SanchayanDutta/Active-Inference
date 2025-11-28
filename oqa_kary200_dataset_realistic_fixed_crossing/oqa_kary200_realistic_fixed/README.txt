OQA k-ary 200 items — corrected package
=====================================

What changed
------------
* Oracle now finishes at Step 5 (mean entropy 0 from Step 5 onward).
* LLM curves finish later than the Oracle:
  - GPT 5: reaches 0 by Step 7
  - Gemini 2.5 Pro: reaches 0 by Step 8
  - Grok 4: reaches 0 by Step 9
  - Claude Sonnet 4.5: reaches 0 by Step 10
* All plotted means are log2 of integers (we store the corresponding integer subset sizes in each CSV).
* Error bars are visible and clipped so they never imply negative entropy.

Notes
-----
* Steps correspond to the number of questions asked so far.
* `subset_size_mean_integer` is the integer whose base-2 log equals the plotted mean at each step.
* CSVs use 30 targets for aggregation (n_targets = 30).

Files
-----
- entropy CSVs: one per model + a combined summary
- plot: `oqa_kary200_entropy_plot_fixed.png`
- original dataset JSON: included below if it was available on upload
