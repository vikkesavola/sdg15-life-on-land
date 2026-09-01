# Data

Three small files are in this folder. The two big ones are not, because they are 155 MB and
4.3 GB.

Every notebook is saved with its outputs, so the figures can be read without downloading
anything. You only need the downloads if you want to re-run notebooks 02, 03, 04 or 06.

## In the repo

`tree_data.csv` (notebook 01) is from Brandt, J., Ertel, J., Spore, J. et al, *The extent of
trees in the tropics* (2022), [doi:10.21203/rs.3.rs-2109093/v1](https://doi.org/10.21203/rs.3.rs-2109093/v1),
table 1 of the supplementary index.

`un_sdg15.csv` (notebook 05) is from the [OECD Data Explorer](https://data-explorer.oecd.org/vis?lc=en&tm=sdg%252015),
SDG 15 indicators.

`protected_percents.csv` (notebook 07) is World Bank indicator `ER.LND.PTLD.ZS`, terrestrial
protected areas as a percentage of land area.

## Not in the repo

### protected_areas.csv, 155 MB

Needed by notebooks 02, 03 and 06. It is the WDPA export: one row per protected area, with the
size, designation year, country and realm.

Download the full WDPA + WD-OECM export in CSV format from
[protectedplanet.net](https://www.protectedplanet.net/en/thematic-areas/wdpa), unzip it and put
the combined CSV here as `protected_areas.csv`.

Note that it is a register of protected areas rather than a statistics product, so the country
totals it gives are approximate. Notebook 06 goes into this.

### trade_database/, 4.3 GB

Needed by notebook 04. This is the full CITES trade database, version 2025.1, compiled by
UNEP-WCMC for the CITES Secretariat.

Get the full database download (not a filtered query) from [trade.cites.org](https://trade.cites.org/)
and unzip it into `data/trade_database/`, keeping the files named `trade_db_1.csv` to
`trade_db_56.csv`. Notebook 04 globs that folder and reads six columns from each file. Reading
all of the columns will run you out of memory.
