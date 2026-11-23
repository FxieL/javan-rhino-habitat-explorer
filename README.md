# Javan Rhino Habitat Explorer

An open-source GIS research project exploring what evidence is needed to assess Alas Purwo National Park, East Java, as a **potential** second wild habitat for the Javan rhinoceros (*Rhinoceros sondaicus*).

> **Research caution:** Ujung Kulon remains the Javan rhino's primary habitat. A second-habitat proposal is still under study. This project is an exploratory GIS prototype—not an official assessment, validated suitability model, survival-probability prediction, or translocation recommendation.

## MVP 0.2

The Streamlit app includes an interactive regional map with an ESA WorldCover 2021 v200 land-cover overlay (10 m nominal resolution), a class legend, and two official park reference points.

The land-cover overlay is for regional context only. It is not clipped to an authoritative Alas Purwo National Park boundary, and it must not be interpreted as a habitat-suitability result. The app does not calculate suitability scores or area statistics.

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Connect this GitHub repository to Streamlit Community Cloud.
2. Select the `feat/initial-explorer` branch while the first version is being developed.
3. Set the main file path to `app.py`.
4. Deploy. New commits to the selected branch can trigger app updates.

## Repository structure

```text
app.py                 Streamlit application and interactive map
requirements.txt       Python dependencies
src/                   Reusable GIS analysis code
data/README.md         Dataset provenance and data policy
docs/methodology.md    Research scope, evidence themes and caveats
```

## Planned research themes

- Habitat and forage
- Water and wallowing sites
- Usable space and movement
- Threats, safety and security
- Ecological interactions, including banteng
- Health, biosecurity and community engagement

See [docs/methodology.md](docs/methodology.md) for the current research approach and limitations.

## Data and attribution

The basemap uses OpenStreetMap tiles and attribution. The land-cover overlay uses ESA WorldCover 2021 v200 through Terrascope WMS. Include this attribution when using the layer in a map:

`© ESA WorldCover project 2021 / Contains modified Copernicus Sentinel data (2021) processed by ESA WorldCover consortium`

WorldCover is licensed under CC BY 4.0. Park reference coordinates are taken from the official Alas Purwo National Park website. Sensitive wildlife-location data will not be published.

## License

This project is released under the MIT License. Third-party datasets and basemaps retain their own licenses and attribution requirements.
