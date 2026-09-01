import matplotlib.pyplot as plt

FONTSIZE = 20

_RCPARAMS = {
    "pdf.fonttype": 42,
    "font.family": "serif",
    "figure.labelsize": FONTSIZE,
    "figure.titlesize": FONTSIZE,
    "axes.labelsize": FONTSIZE,
    "axes.titlesize": FONTSIZE,
    "xtick.labelsize": FONTSIZE,
    "ytick.labelsize": FONTSIZE,
    "legend.fontsize": FONTSIZE,
    "legend.title_fontsize": FONTSIZE,
    "legend.frameon": False,
}


def use_report_style():
    """Apply the project-wide matplotlib defaults."""
    plt.rcParams.update(_RCPARAMS)
