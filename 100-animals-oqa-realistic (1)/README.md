# 100-animals-oqa-realistic

This dataset is a realistic, self-contained variant of the 100‑animals OQA game.

## Key assumptions
- Entropy at each step is computed as `log2(K)` where `K` is an integer count of the remaining viable candidates for that run.
- We simulate 10 independent runs per model. The per-step means and standard deviations are reported across runs.
- Because this 100‑animals set contains a small number of non-trivial equivalence classes, resolution often ends with either a single item (K=1 → 0 bits) or a small equivalence class (K=2 → 1 bit). A mix of these outcomes produces final mean entropy near 0.2 bits.

## Stopping behavior (as requested)
- **Oracle** reaches its final outcome by **Step 6** (mean ≈ 0.2 bits).
- **GPT 5** and **Gemini 2.5 Pro** finish by **Step 7** (mean ≈ 0.2 bits).
- **Grok 4** finishes by **Step 8** (mean ≈ 0.2 bits).
- **Claude Sonnet 4.5** finishes by **Step 9** (mean ≈ 0.2 bits).
- Oracle is information-theoretically optimal: at every step its mean entropy is less than or equal to every model's mean.

## Error bars
- The plot uses vertical error bars (`yerr`) with caps. When the lower bound would dip below 0, it is asymmetrically clipped at 0 so the graphic never shows negative entropy.

## Contents
- `csv/*_runs_entropy_bits.csv`: per-run entropies for each model (each value is exactly `log2` of an integer).
- `csv/summary_mean_std.csv`: per-step means and standard deviations for each model.
- `plots/100-animals-entropy-errorbars.png`: summary figure with vertical error bars.
- `source/100_Animals.json`: the object attribute file you provided.

