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

## Current MVP 0.1

The app currently displays two official park reference points for map orientation:

- Alas Purwo National Park Office: approximately 8.233811° S, 114.351623° E
- Rowobendo entrance: approximately 8.642537° S, 114.357317° E

These are point references only. They do not represent park boundaries, rhino occurrence, habitat extent or suitability.

## Initial references

- Ministry of Forestry (19 November 2026), *Menhut Raja Antoni Tegaskan Ujung Kulon Tetap Habitat Utama Badak Jawa*.
- BRIN (17 November 2026), *Securing the Future of the Javan Rhino: Lessons from Two Decades of Second Habitat Studies*.
- Alas Purwo National Park official website: https://tnalaspurwo.ksdae.kehutanan.go.id/

Reference statements should be revisited as new official studies and datasets become available.
