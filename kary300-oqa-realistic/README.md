
OQA k-ary (300 items) realistic package
======================================

- Source dataset: 300 items with 8 attributes each (color, shape, material, size, pattern, origin, use_case, energy).
- Oracle policy: greedy selection that minimizes expected posterior entropy at each step over the **current** candidate set. 
  Averaged over 30 random targets, the oracle reaches 0 bits by **step 5** in this dataset.
- LLM policies: slower "coarse-to-fine" heuristics that sometimes ask generic k-way splits not aligned to the attributes,
  which makes them finish later than the oracle and allows lines to cross slightly.
  * GPT 5 finishes by about step 8 on average.
  * Gemini 2.5 Pro finishes by about step 10 on average.
  * Grok 4 and Claude Sonnet 4.5 finish by about step 10 on average.
- Error bars are standard deviations over 30 targets. Lower bars are clipped at 0 so the plot never shows negative entropy.
- All values in CSV summaries include a column `mean_bits_rounded_log2int` that rounds the mean to the nearest `log2(integer)`.

Files
-----
- `data/oqa_kary300_dataset.json` – copy of the dataset you supplied.
- `data/entropy_summary_by_step.csv` – per-model means and stds by step (includes the rounded means column).
- `data/per_run_entropy_*.csv` – per-run entropy traces (step 0 is the pre-question baseline).
- `plots/oqa_kary300_entropy_plot_30targets.png` – the figure.
- `prompts/api_prompt_template.txt` – a lightweight prompt to run the k-ary OQA game against an LLM API.

Repro
-----
The figure and CSVs were generated with a fixed RNG seed (42).
