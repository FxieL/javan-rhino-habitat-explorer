import streamlit as st
import folium
import requests
import xml.etree.ElementTree as ET
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Javan Rhino Habitat Explorer",
    page_icon="🦏",
    layout="wide",
    initial_sidebar_state="expanded",
)

PARK_OFFICE = (-8.233811153469162, 114.35162278378635)
ROWOBENDO_GATE = (-8.64253663116379, 114.35731680815084)

LAND_COVER_CLASSES = [
    (10, "Tree cover", "#006400"),
    (20, "Shrubland", "#ffbb22"),
    (30, "Grassland", "#ffff4c"),
    (40, "Cropland", "#f096ff"),
    (50, "Built-up", "#fa0000"),
    (60, "Bare / sparse vegetation", "#b4b4b4"),
    (70, "Snow and ice", "#f0f0f0"),
    (80, "Permanent water bodies", "#0064c8"),
    (90, "Herbaceous wetland", "#0096a0"),
    (95, "Mangroves", "#00cf75"),
    (100, "Moss and lichen", "#fae6a0"),
]

WORLDCOVER_WMS_URL = "https://titiler.terrascope.be/wms"
WORLDCOVER_LAYER = "esa-worldcover-map-10m-2021-v2_map"
WORLDCOVER_ATTRIBUTION = (
    "© ESA WorldCover project 2021 / Contains modified Copernicus Sentinel data "
    "(2021) processed by ESA WorldCover consortium"
)

st.markdown(
    """
    <style>
      .block-container {padding-top: 2.2rem; padding-bottom: 3rem;}
      .eyebrow {text-transform: uppercase; letter-spacing: .13em; font-size: .72rem;
                font-weight: 700; color: #39836b;}
      .hero {font-size: clamp(2rem, 4vw, 3.3rem); line-height: 1.05;
             font-weight: 800; margin: .25rem 0 .65rem 0;}
      .subhero {font-size: 1.08rem; color: #64748b; max-width: 850px;}
      .note {border-left: 4px solid #d69e36; padding: .8rem 1rem;
             background: rgba(214,158,54,.09); border-radius: 0 .5rem .5rem 0;}
      .small-muted {font-size: .82rem; color: #64748b;}
      .legend-grid {display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: .42rem .8rem; margin-top: .5rem;}
      .legend-item {display: flex; align-items: center; gap: .5rem;
                    font-size: .84rem; line-height: 1.25;}
      .legend-swatch {width: 17px; height: 17px; min-width: 17px;
                      border: 1px solid rgba(0,0,0,.18); border-radius: 3px;}
      @media (max-width: 640px) {
        .legend-grid {grid-template-columns: 1fr;}
      }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🦏 Field notes")
    st.caption("Javan Rhino Habitat Explorer · MVP 0.2")
    st.divider()
    st.markdown("**Study area**")
    st.write("Alas Purwo National Park")
    st.write("East Java, Indonesia")
    st.divider()
    st.markdown("**Project stage**")
    st.info("Exploratory screening")
    st.caption(
        "This is a research and learning prototype. It is not an official "
        "habitat assessment or a translocation recommendation."
    )
    st.divider()
    st.markdown("**Map layers**")
    st.write("🟩 ESA WorldCover 2021 · 10 m")
    st.write("📍 Park reference points")
    st.caption(
        "Use the map's layer control to show or hide the land-cover overlay "
        "and reference markers."
    )

st.markdown(
    '<div class="eyebrow">Open-source conservation GIS · Indonesia</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="hero">Javan Rhino<br>Habitat Explorer</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subhero">An exploratory GIS project asking what we need to know '
    'before Alas Purwo could be evaluated as a potential second wild habitat '
    'for the Javan rhinoceros (<i>Rhinoceros sondaicus</i>).</div>',
    unsafe_allow_html=True,
)

st.write("")
c1, c2, c3 = st.columns(3)
c1.metric("Species", "Javan rhinoceros", "Rhinoceros sondaicus")
c2.metric("Study landscape", "Alas Purwo", "East Java")
c3.metric("Assessment status", "Not assessed", "Candidate under discussion")

st.markdown(
    '<div class="note"><strong>Important context.</strong> Ujung Kulon remains '
    'the Javan rhino’s primary habitat. A second-habitat proposal is still under '
    'study; this project does not imply that Alas Purwo has been approved or '
    'confirmed as suitable.</div>',
    unsafe_allow_html=True,
)

st.write("")
left, right = st.columns([1.65, 1], gap="large")

with left:
    st.subheader("Land-cover map")
    st.caption(
        "ESA WorldCover 2021 is displayed as a regional land-cover layer. "
        "The map view is not a park boundary and is not clipped to the official "
        "Alas Purwo National Park polygon."
    )

    m = folium.Map(
        location=[-8.44, 114.355],
        zoom_start=10,
        tiles="OpenStreetMap",
        control_scale=True,
    )

    folium.raster_layers.WmsTileLayer(
        url=WORLDCOVER_WMS_URL,
        layers=WORLDCOVER_LAYER,
        name="ESA WorldCover 2021",
        fmt="image/png",
        transparent=True,
        version="1.3.0",
        attr=WORLDCOVER_ATTRIBUTION,
        overlay=True,
        control=True,
        show=True,
    ).add_to(m)

    reference_points = folium.FeatureGroup(
        name="Park reference points",
        show=True,
    )
    folium.Marker(
        PARK_OFFICE,
        tooltip="Alas Purwo National Park Office",
        popup="Official park-office reference point; not a habitat boundary.",
        icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(reference_points)
    folium.Marker(
        ROWOBENDO_GATE,
        tooltip="Rowobendo Entrance",
        popup="Official entrance reference point; not a habitat boundary.",
        icon=folium.Icon(color="blue", icon="flag"),
    ).add_to(reference_points)
    reference_points.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)
    st_folium(m, use_container_width=True, height=560, returned_objects=[])

    st.markdown("**Legend · ESA WorldCover 2021**")
    legend_items = "".join(
        f'<div class="legend-item"><span class="legend-swatch" '
        f'style="background:{color};"></span><span>{label}</span></div>'
        for _, label, color in LAND_COVER_CLASSES
    )
    st.markdown(
        f'<div class="legend-grid">{legend_items}</div>',
        unsafe_allow_html=True,
    )
    st.caption(
        "Class colors follow the official ESA WorldCover 2021 v200 palette. "
        "The legend describes mapped land-cover classes, not habitat quality."
    )

    with st.expander("🔧 Troubleshooting · Test map service"):
        st.write(
            "Run a server-side check from the Streamlit app environment. "
            "The test follows Terrascope's documented WMS endpoint syntax, "
            "checks the advertised layer, then requests a sample image."
        )
        if st.button("Test ESA WorldCover connection", key="test_worldcover"):
            try:
                # Terrascope documents this canonical GetCapabilities request
                # without an explicit VERSION parameter.
                cap_response = requests.get(
                    WORLDCOVER_WMS_URL,
                    params={
                        "service": "WMS",
                        "request": "GetCapabilities",
                    },
                    timeout=30,
                )
                st.write(f"GetCapabilities HTTP status: **{cap_response.status_code}**")
                st.write(
                    f"Response content type: "
                    f"`{cap_response.headers.get('Content-Type', 'unknown')}`"
                )
                if not cap_response.ok:
                    st.error("Terrascope rejected the GetCapabilities request.")
                    st.code(cap_response.text[:2000] or "(empty response)")
                    st.stop()

                root = ET.fromstring(cap_response.content)
                layer_names = [
                    node.text.strip()
                    for node in root.findall(".//{*}Layer/{*}Name")
                    if node.text
                ]
                matching_layers = [
                    name for name in layer_names
                    if "worldcover" in name.lower()
                ]
                layer_found = WORLDCOVER_LAYER in layer_names
                if layer_found:
                    st.success(f"Layer found: {WORLDCOVER_LAYER}")
                else:
                    st.error(f"Expected layer not found: {WORLDCOVER_LAYER}")
                if matching_layers:
                    st.write("WorldCover layers advertised by this service:")
                    st.code("\\n".join(matching_layers[:30]))
                else:
                    st.warning("No layer name containing 'worldcover' was found.")

                # WMS 1.3.0 uses CRS (not SRS). For EPSG:4326 its BBOX
                # axis order is latitude, longitude.
                map_response = requests.get(
                    WORLDCOVER_WMS_URL,
                    params={
                        "service": "WMS",
                        "request": "GetMap",
                        "version": "1.3.0",
                        "layers": WORLDCOVER_LAYER,
                        "styles": "",
                        "crs": "EPSG:4326",
                        "bbox": "-8.70,114.20,-8.10,114.50",
                        "width": "512",
                        "height": "512",
                        "format": "image/png",
                        "transparent": "TRUE",
                    },
                    timeout=45,
                )
                st.write(f"GetMap HTTP status: **{map_response.status_code}**")
                st.write(
                    f"Map response content type: "
                    f"`{map_response.headers.get('Content-Type', 'unknown')}`"
                )
                if map_response.ok and "image" in map_response.headers.get("Content-Type", "").lower():
                    st.success("The WMS returned an image successfully.")
                    st.image(map_response.content, caption="WMS diagnostic sample around Alas Purwo")
                else:
                    st.error("The WMS did not return an image. Response preview:")
                    st.code(map_response.text[:2000] or "(empty response)")
            except requests.RequestException as exc:
                st.error(f"Network request failed: {exc}")
            except ET.ParseError:
                st.error("The service response was not valid WMS XML.")
            except Exception as exc:
                st.error(f"Diagnostic failed: {type(exc).__name__}: {exc}")

    st.markdown(
        f'<p class="small-muted">{WORLDCOVER_ATTRIBUTION}. '
        'Source: <a href="https://esa-worldcover.org/en/data-access" '
        'target="_blank">ESA WorldCover data access</a>.</p>',
        unsafe_allow_html=True,
    )

with right:
    st.subheader("What does the map tell us?")
    st.markdown(
        """
        The layer gives us a first look at the **land-cover pattern** around
        the Alas Purwo landscape:

        - **Tree cover** — broad woody vegetation cover
        - **Shrubland & grassland** — open vegetation classes
        - **Wetlands & water** — mapped wetland and permanent-water classes
        - **Cropland & built-up** — human-modified land-cover classes
        - **Mangroves** — a distinct coastal vegetation class
        """
    )
    st.info(
        "Land cover is only one evidence layer. It cannot tell us by itself "
        "whether forage is suitable, water is reliable year-round, or the "
        "landscape can support a Javan rhino population."
    )

    st.subheader("Dataset notes")
    st.markdown(
        """
        | Property | Details |
        |---|---|
        | Publisher | ESA WorldCover Consortium |
        | Product | WorldCover 2021 v200 |
        | Reference year | 2021 |
        | Pixel resolution | 10 m |
        | Source imagery | Sentinel-1 & Sentinel-2 |
        | Classes | 11 |
        | License | CC BY 4.0 |
        """
    )
    st.caption(
        "The 2021 map is a historical snapshot, not a live land-cover feed. "
        "Its global overall accuracy is reported as 76.7%; local class accuracy "
        "may differ."
    )

st.divider()
st.subheader("What are we investigating next?")
a, b, c = st.columns(3)
a.markdown(
    "**01 · Habitat & forage**\n\n"
    "Land-cover patterns are a starting point; vegetation composition and "
    "actual browse availability need separate evidence."
)
b.markdown(
    "**02 · Water & wallowing**\n\n"
    "Map rivers, wetlands and seasonal water availability using suitable "
    "hydrological datasets."
)
c.markdown(
    "**03 · Space & safety**\n\n"
    "Add an authoritative park boundary, terrain, access and threat layers "
    "before any spatial assessment."
)

st.markdown(
    '<p class="small-muted">Basemap © OpenStreetMap contributors. '
    'Park reference coordinates: official Alas Purwo National Park website. '
    'This independent prototype is not an official government product.</p>',
    unsafe_allow_html=True,
)
