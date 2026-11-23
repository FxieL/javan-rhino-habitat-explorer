# Research approach and methodology

## Working question

What publicly available spatial and ecological evidence would be needed to evaluate whether Alas Purwo National Park could support a second wild population of the Javan rhinoceros (*Rhinoceros sondaicus*)?

## Scope and scientific caution

This project is an independent, exploratory GIS learning and research prototype. It is **not** an official assessment, a validated habitat-suitability model, a survival-probability prediction, or a recommendation to translocate rhinos.

Ujung Kulon remains the species' primary habitat. Government and research communications in November 2026 describe the second-habitat effort as an ongoing study, with no final site or technical translocation plan established. Alas Purwo is a candidate for further consideration, not a confirmed suitable site.

Alas Purwo also requires its own independent assessment. It should not be assumed suitable simply because other locations have been studied previously.

## Evidence themes to investigate

The following are candidate evidence themes, not yet operational model variables:

1. **Habitat and forage** — vegetation composition, forest structure, browse availability and seasonal variation.
2. **Water and wallowing** — perennial water availability, wetlands, wallows and dry-season reliability.
3. **Space and movement** — usable habitat area, terrain, connectivity and potential home-range requirements.
4. **Safety and threats** — poaching exposure, human access, roads, disturbance, fire and other relevant hazards.
5. **Ecological interactions** — sympatric large herbivores, including banteng, and potential resource competition.
6. **Health and biosecurity** — disease surveillance, veterinary feasibility and risks associated with moving animals.
7. **People and governance** — community engagement, land use, park capacity and long-term management.

## Planned analytical workflow

1. Define the study boundary from an authoritative protected-area dataset. Do not infer a boundary from map markers.
2. Build a source register and inspect each dataset's license, date, resolution, CRS and known limitations.
3. Harmonize layers in an appropriate projected CRS and document all preprocessing.
4. Explore each evidence theme independently before combining anything into a model.
5. Co-design transparent criteria, weights and exclusion rules with domain experts and relevant authorities.
6. Test sensitivity to assumptions and communicate uncertainty. Avoid false precision.
7. Treat field validation, ecological expertise and community consultation as essential; remote sensing alone cannot establish habitat suitability.

## Current MVP 0.2 — land-cover context

The app now includes an interactive regional land-cover overlay using **ESA WorldCover 2021 v200**:

- Publisher: ESA WorldCover consortium
- Reference year: 2021
- Nominal spatial resolution: 10 m
- Input satellite missions: Sentinel-1 and Sentinel-2
- Classification: 11 discrete land-cover classes
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Access in the app: Terrascope WMS layer `WORLDCOVER_2021_MAP`
- Dataset DOI: https://doi.org/10.5281/zenodo.7254221
- Official data access and attribution: https://esa-worldcover.org/en/data-access

The WMS is used for visualization only. ESA notes that WMS images are RGB representations and are not suitable for spatial analysis. For analysis, obtain the underlying classified raster data and document the processing workflow.

### WorldCover class codes and display colors

The legend follows the ESA WorldCover 2021 palette:

| Code | Class | Hex color |
|---:|---|---|
| 10 | Tree cover | `#006400` |
| 20 | Shrubland | `#FFBB22` |
| 30 | Grassland | `#FFFF4C` |
| 40 | Cropland | `#F096FF` |
| 50 | Built-up | `#FA0000` |
| 60 | Bare / sparse vegetation | `#B4B4B4` |
| 70 | Snow and ice | `#F0F0F0` |
| 80 | Permanent water bodies | `#0064C8` |
| 90 | Herbaceous wetland | `#0096A0` |
| 95 | Mangroves | `#00CF75` |
| 100 | Moss and lichen | `#FAE6A0` |

### Interpretation limits

- The 2021 layer is a historical snapshot, not a live land-cover feed.
- ESA reports a **global overall accuracy of 76.7%** for WorldCover 2021 v200. This is not a local accuracy estimate for Alas Purwo; class-specific accuracy varies.
- The current map is a regional context view and is **not clipped to an authoritative Alas Purwo park boundary**.
- Land-cover classes do not directly measure forage species, browse availability, forest structure, seasonal water, carrying capacity or rhino habitat suitability.
- A tree-cover pixel is not automatically suitable rhino habitat, and an open-cover class is not automatically unsuitable.
- Do not derive park area statistics or suitability scores from the current display layer.

## Current map reference points

The app also displays two official park reference points for orientation:

- Alas Purwo National Park Office: approximately 8.233811° S, 114.351623° E
- Rowobendo entrance: approximately 8.642537° S, 114.357317° E

These are point references only. They do not represent park boundaries, rhino occurrence, habitat extent or suitability.

## Initial references

- Ministry of Forestry (19 November 2026), *Menhut Raja Antoni Tegaskan Ujung Kulon Tetap Habitat Utama Badak Jawa*.
- BRIN (17 November 2026), *Securing the Future of the Javan Rhino: Lessons from Two Decades of Second Habitat Studies*.
- ESA WorldCover data access: https://esa-worldcover.org/en/data-access
- Zanaga et al. (2022), *ESA WorldCover 10 m 2021 v200*: https://doi.org/10.5281/zenodo.7254221
- Alas Purwo National Park official website: https://tnalaspurwo.ksdae.kehutanan.go.id/

Reference statements should be revisited as new official studies and datasets become available.
