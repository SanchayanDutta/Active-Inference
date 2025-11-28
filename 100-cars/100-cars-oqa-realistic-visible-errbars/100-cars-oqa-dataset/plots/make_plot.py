import pandas as pd, numpy as np
import matplotlib.pyplot as plt
legend = ["GPT 5","Gemini 2.5 Pro","Claude Sonnet 4.5","Grok 4","Oracle"]
df = pd.read_csv("100_cars_entropy_summary.csv")
plt.figure(figsize=(9,5))
for m in legend:
    g = df[df["model"]==m].sort_values("step").copy()
    x = g["step"].to_numpy(); y = g["entropy_bits_mean"].to_numpy(); std = g["entropy_bits_std"].to_numpy()
    lower = np.minimum(std, y); upper = std
    yerr = np.vstack([lower, upper])
    plt.errorbar(x, y, yerr=yerr, fmt='-o', capsize=3, label=m)
plt.title("100 Cars Dataset: Entropy (bits) Across Steps — Visible error bars")
plt.xlabel("Step"); plt.ylabel("Entropy = log2(# remaining options)")
plt.legend(); plt.grid(True, alpha=0.2)
plt.tight_layout(); plt.savefig("100_cars_entropy_plot.png", dpi=160); plt.close()