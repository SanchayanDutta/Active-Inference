# Auto-generated: plot with legend order and std error bars
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "25_animals_entropy_summary.csv"
df = pd.read_csv(csv_path)

legend_order = ["GPT 4.1", "Gemini 2.0 Flash", "Claude Haiku 4.5", "Oracle"]

plt.figure(figsize=(8, 5))
for model_name in legend_order:
    g = df[df["model"] == model_name].sort_values("step")
    if g.empty:
        continue
    x = g["step"].to_numpy()
    y = g["entropy_bits_mean"].to_numpy()
    yerr = g["entropy_bits_std"].to_numpy()
    plt.errorbar(x, y, yerr=yerr, fmt='-o', capsize=3, label=model_name)

plt.xlabel("Step")
plt.ylabel("Entropy (bits)")
plt.title("Average entropy by step (25 animals OQA)")
plt.legend()
plt.tight_layout()
plt.savefig("25_animals_entropy_plot.png", dpi=160)
plt.close()
