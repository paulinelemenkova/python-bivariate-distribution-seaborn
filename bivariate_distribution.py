#!/usr/bin/env python
# coding: utf-8
"""Bivariate distribution plot (Seaborn jointplot).

Draws a bivariate joint distribution: a central scatter plot of two
variables combined with their marginal histograms, showing both the
relationship between the variables and the univariate spread of each.

The example uses morphometric data of the Mariana Trench (Pacific Ocean),
plotting igneous/volcanic rock area against sediment thickness.

Data:    Tab-Morph.csv - morphometric variables sampled along 25
         bathymetric profiles across the Mariana Trench.

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.11010.73922
License: MIT
"""
import os

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

sb.set_style('white')
sb.set_context('paper')

dfM = pd.read_csv(os.path.join(HERE, 'Tab-Morph.csv'))

sb.jointplot(x='igneous_volc', y='sedim_thick', data=dfM)

plt.tight_layout()
plt.savefig(os.path.join(HERE, 'plot_BivarDistr.png'), dpi=300)
plt.show()
