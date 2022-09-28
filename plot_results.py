import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")
plt.rcParams['text.usetex'] = True
plt.rcParams["axes.grid"] = False

fns = [
    "results_ETKDG.txt",
    "results_GeoMol.txt",
    "results_TorsionDiff.txt",
]

for fn in fns:
    with open(fn, "r") as f:
        lines = f.readlines()
    coverages = [float(line.split("=")[1].split(",")[0].strip()) for line in lines if "Recall Coverage" in line]
    thresholds = [float(line.split("threshold")[1].strip()) for line in lines if "threshold" in line]

    plt.plot(thresholds, coverages, label=fn.split("_")[1].split(".")[0].strip())
plt.legend()
plt.savefig("results.png")