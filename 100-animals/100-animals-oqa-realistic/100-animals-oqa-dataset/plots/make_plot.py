import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("100_animals_entropy_summary.csv")

legend_order = ["GPT 5", "Gemini 2.5 Pro", "Claude Sonnet 4.5", "Grok 4", "Oracle"]
present = list(df["model"].unique())
ordered = [m for m in legend_order if m in present] + [m for m in present if m not in legend_order]

plt.figure(figsize=(8, 5))
for model_name in ordered:
    g = df[df["model"] == model_name].sort_values("step").copy()
    x = g["step"].to_numpy()
    y = g["entropy_bits_mean"].to_numpy()
    std = g["entropy_bits_std"].to_numpy()
    lower = np.minimum(std, y)
    upper = std
    yerr = np.vstack([lower, upper])
    plt.errorbar(x, y, yerr=yerr, fmt="-o", capsize=3, label=model_name)

plt.xlabel("Step")
plt.ylabel("Entropy (bits)")
plt.title("100 Animals Dataset: Entropy Across Steps")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("100_animals_entropy_plot.png", dpi=160)
plt.close()
