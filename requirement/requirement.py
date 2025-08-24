import importlib
import subprocess
import sys

try:
    # Built-in for Python 3.8+
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Fallback for older Python versions
    from pkg_resources import get_distribution, DistributionNotFound
    def version(package): return get_distribution(package).version
    PackageNotFoundError = DistributionNotFound


# === Your Required Libraries ===
REQUIREMENTS = {
    # Core
    "numpy": "1.24.6",
    "pandas": "2.1.0",
    "scipy": "1.11.1",

    # Data Fetching
    "yfinance": "0.2.27",
    "requests": "2.32.0",
    "python-dateutil": "2.9.4",

    # EDA & Visualization
    "matplotlib": "3.8.1",
    "seaborn": "0.12.2",
    "plotly": "6.2.1",
    "missingno": "0.5.2",
    "statsmodels": "0.14.1",

    # Classical & Econometric Models
    "arch": "6.2",
    "linearmodels": "5.0.10",

    # Machine Learning
    "scikit-learn": "1.3.2",
    "xgboost": "1.7.6",
    "lightgbm": "4.4.1",

    # Deep Learning
    "torch": "2.3.1",
    "torchvision": "0.18.1",
    "pytorch-lightning": "2.2.1",
    "transformers": "4.34.0",
    "tensorflow": "2.14.0",

    # Time Series Forecasting
    "prophet": "1.1.4",

    # Evaluation & Metrics
    "joblib": "1.3.2",

    # Optional / Utilities
    "tqdm": "4.66.1",
    "pandas-ta": "0.3.0b0",
}


def install_or_update(package: str, required_version: str):
    """Ensure package is installed and updated to the required version."""
    try:
        installed_version = version(package)
        if installed_version != required_version:
            print(f"[UPDATE] {package}: {installed_version} → {required_version}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}=={required_version}"])
        else:
            print(f"[OK] {package} is already at {required_version}")
    except PackageNotFoundError:
        print(f"[INSTALL] {package}=={required_version}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}=={required_version}"])


def ensure_requirements(auto_confirm: bool = False):
    """
    Ensure all required packages are installed/updated.

    Args:
        auto_confirm (bool): If True, installs without asking.
    """
    print("\n👋 Hello User!")
    print("🙏 Thank you for downloading FinTimePro.")
    print("📦 These are the most compatible Python library versions for this project:\n")

    for pkg, ver in REQUIREMENTS.items():
        print(f"  - {pkg}=={ver}")

    if not auto_confirm:
        choice = input("\n⚡ Do you want to install/update these dependencies? (y/n): ").strip().lower()
        if choice != "y":
            print("\n❌ Skipping installation. Make sure your environment has the required versions.")
            return

    print("\n🚀 Installing/Updating packages...\n")
    for package, version_str in REQUIREMENTS.items():
        install_or_update(package, version_str)

    print("\n✅ All requirements are installed and up-to-date!")


# Only run automatically if called directly
if __name__ == "__main__":
    ensure_requirements()
