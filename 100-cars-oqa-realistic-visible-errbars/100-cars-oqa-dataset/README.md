# 100-Cars OQA Dataset (Realistic)

- **Items**: 100
- **Equivalence classes**: 100. A run can resolve to a single item or a single class.
- **Entropy definition**: `entropy_bits = log2(# of remaining candidates)` per seed at each step.
- **Stopping rule**: stop when the set is a single item or a single equivalence class.
- **Models**: GPT 5, Gemini 2.5 Pro, Claude Sonnet 4.5, Grok 4, Oracle.
- **Seeds**: 10 per model. Entropies in `*_seeds.csv` are exact `log2(k)` values. Summary means are true averages.
- **Error bars**: vertical ±1 std; lower whiskers are clipped at 0 in the plot for readability.
- **Oracle rule**: nonzero std before the first step where mean ≤ 1; std = 0 from that step onward.

This dataset follows the overall shape of the provided example plot with slight, realistic deviations 
while updating model names. The plot is reproducible with `plots/make_plot.py`.
