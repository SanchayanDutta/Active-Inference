# 100-Places OQA Dataset (Realistic)

- **Items**: 100
- **Equivalence classes**: 100. Runs can only resolve down to a class, not below.
- **Entropy definition**: `entropy_bits = log2(# of remaining candidates)` per run at each step.
- **Stopping rule**: dialogue stops when the remaining set is a single item or a single equivalence class.
- **Models**: GPT 5, Gemini 2.5 Pro, Claude Sonnet 4.5, Grok 4, Oracle.
- **Seeds**: 10 per model. Entropies in `*_seeds.csv` are exact `log2(k)` values. Summary means are true averages.
- **Error bars**: vertical ±1 std; when mean is very small, we clip the lower whisker at 0 on the plot.
- **Oracle rule**: nonzero std before the first step where mean ≤ 1; std = 0 from that step onward.

This dataset was generated to follow the overall shape of the provided example plot with slight, realistic deviations 
while updating model names. The plot is reproducible from `plots/make_plot.py`.
