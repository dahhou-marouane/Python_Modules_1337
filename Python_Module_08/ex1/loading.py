def analyzing_data() -> None:
    out_put = "matrix_analysis.png"
    print("Analyzing Matrix data...")
    import numpy
    import pandas
    data = numpy.random.randn(1000)
    times = numpy.arange(1000)
    df = pandas.DataFrame({
        "time": times,
        "signal": data})

    print("Processing 1000 data points...")
    print("Generating visualization...")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    _, ax = plt.subplots()
    ax.plot(df["time"], df["signal"], alpha=0.5, label="Raw signal")
    ax.set_title("Matrix Signal")
    ax.legend()
    plt.tight_layout()
    plt.savefig(out_put)
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to:", out_put)


def missing() -> None:
    msg = [
        "\nDependencies are missing!",
        "Install with pip:",
        "pip install -r requirements.txt\n",
        "Install with Poetry:",
        "poetry install",
        "poetry run python loading.py"]
    for i in msg:
        print(i)


def check_installation() -> bool:
    import importlib.util
    from importlib.metadata import version
    print("Checking dependencies:")
    dependencies = [importlib.util.find_spec("numpy"),
                    importlib.util.find_spec("pandas"),
                    importlib.util.find_spec("matplotlib")]
    s = all(dependencies)
    if importlib.util.find_spec("pandas"):
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    else:
        print("[MISSING] pandas - Data manipulation ready")

    if importlib.util.find_spec("numpy"):
        print(f"[OK] numpy ({version('numpy')}) - Numerical computation ready")
    else:
        print("[MISSING] numpy - Numerical computation ready")
    if importlib.util.find_spec("matplotlib"):
        print(f"[OK] matplotlib ({version('matplotlib')}) "
              "- Visualization ready")
    else:
        print("[MISSING] matplotlib - Visualization ready")
    print()
    return s


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    if not check_installation():
        missing()
    else:
        analyzing_data()
