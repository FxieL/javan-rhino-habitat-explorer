# Javan Rhino Habitat Explorer

An open-source GIS research project exploring what evidence is needed to assess Alas Purwo National Park, East Java, as a **potential** second wild habitat for the Javan rhinoceros (*Rhinoceros sondaicus*).

> **Research caution:** Ujung Kulon remains the Javan rhino's primary habitat. A second-habitat proposal is still under study. This project is an exploratory GIS prototype—not an official assessment, validated suitability model, survival-probability prediction, or translocation recommendation.

## MVP 0.1

The first version is a Streamlit web app with an interactive locator map showing two official park reference points: the Alas Purwo National Park Office and Rowobendo entrance. These points are for orientation only; they are not a park boundary or habitat-suitability result.

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
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

The map uses OpenStreetMap tiles and attribution. Reference coordinates are taken from the official Alas Purwo National Park website. Dataset sources, licenses, dates, CRS and processing steps will be documented before analytical use. Sensitive wildlife-location data will not be published.

## License

This project is released under the MIT License. Third-party datasets and basemaps retain their own licenses and attribution requirements.
