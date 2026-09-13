# Bivariate Distribution Plot with Python and Seaborn

A reusable Python script that draws a **bivariate joint distribution** with the
Seaborn `jointplot` function: a central scatter plot of two variables together
with their marginal histograms, showing both the relationship between the
variables and the univariate spread of each.

The worked example uses morphometric data of the Mariana Trench (Pacific
Ocean), plotting igneous/volcanic rock area against sediment thickness.

## Script

- `bivariate_distribution.py` — loads the table with pandas, sets the Seaborn
  style and context, renders the joint plot and saves it to
  `plot_BivarDistr.png`.

## Data

- `Tab-Morph.csv` — morphometric variables (depth statistics, tangent/slope
  angle, tectonic-plate membership, igneous/volcanic area, sediment thickness,
  hillshade, aspect) sampled along 25 bathymetric profiles across the Mariana
  Trench.

## Method

Bivariate joint distribution: a scatter plot of two variables with marginal
histogram estimates of each variable's univariate distribution.

## Requirements

Python 3 with `pandas`, `seaborn` and `matplotlib`.

```
pip install pandas seaborn matplotlib
python bivariate_distribution.py
```

## Author

Polina Lemenkova — ORCID: https://orcid.org/0000-0002-5759-1089

Archived code: https://doi.org/10.13140/RG.2.2.11010.73922

## License

MIT — see the LICENSE file (Copyright Polina Lemenkova).
