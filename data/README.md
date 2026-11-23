# Data directory

This directory is reserved for source datasets and derived GIS outputs.

## Data policy

Before a dataset is used, record:

- Dataset title and publisher
- Original download or landing-page URL
- Publication/update date and access date
- Spatial and temporal resolution
- Coordinate reference system (CRS)
- License and attribution requirements
- Processing steps and any known limitations

Do not commit large raw datasets or sensitive wildlife-location data to this repository. Prefer documented download instructions, public APIs, or small derived samples where licensing permits.

## Current map service

The app visualizes ESA WorldCover 2021 v200 through the Terrascope WMS service `https://titiler.terrascope.be/wms`:

- Layer: `esa-worldcover-map-10m-2021-v2_map`
- Reference year: 2021
- Nominal resolution: 10 m
- License: CC BY 4.0
- Data access: https://esa-worldcover.org/en/data-access
- Dataset DOI: https://doi.org/10.5281/zenodo.7254221
- Required map attribution: © ESA WorldCover project 2021 / Contains modified Copernicus Sentinel data (2021) processed by ESA WorldCover consortium

The WMS provides rendered map images for visualization, not analysis-ready raster values. For raster analysis, download the underlying classified data from the official data access channels. The current app layer is a regional view and is not clipped to a park boundary.

## Planned data themes

- Protected-area boundaries and management zones
- Land cover, vegetation and forest change
- Elevation, slope and terrain
- Rivers, water sources and potential wallowing areas
- Roads, settlements and human-access indicators
- Biodiversity records, subject to sensitivity and data-sharing restrictions

No habitat-suitability dataset is included in this project.
