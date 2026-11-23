import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Javan Rhino Habitat Explorer",
    page_icon="🦏",
    layout="wide",
    initial_sidebar_state="expanded",
)

PARK_OFFICE = (-8.233811153469162, 114.35162278378635)
ROWOBENDO_GATE = (-8.64253663116379, 114.35731680815084)

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
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🦏 Field notes")
    st.caption("Javan Rhino Habitat Explorer · MVP 0.1")
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
    st.checkbox("Park office reference", value=True, disabled=True)
    st.checkbox("Rowobendo entrance reference", value=True, disabled=True)
    st.caption("Environmental and habitat layers are not yet loaded.")

st.markdown('<div class="eyebrow">Open-source conservation GIS · Indonesia</div>', unsafe_allow_html=True)
st.markdown('<div class="hero">Javan Rhino<br>Habitat Explorer</div>', unsafe_allow_html=True)
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
    st.subheader("Study area locator")
    st.caption(
        "Two reference points are shown for orientation only. They are not a "
        "park boundary, habitat boundary, rhino sighting, or suitable-habitat result."
    )
    m = folium.Map(
        location=[-8.44, 114.355],
        zoom_start=10,
        tiles="OpenStreetMap",
        control_scale=True,
    )
    folium.Marker(
        PARK_OFFICE,
        tooltip="Alas Purwo National Park Office",
        popup="Official park-office reference point",
        icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(m)
    folium.Marker(
        ROWOBENDO_GATE,
        tooltip="Rowobendo Entrance",
        popup="Official Rowobendo entrance reference point",
        icon=folium.Icon(color="blue", icon="flag"),
    ).add_to(m)
    folium.LayerControl(collapsed=True).add_to(m)
    st_folium(m, use_container_width=True, height=520, returned_objects=[])

with right:
    st.subheader("What are we investigating?")
    st.markdown(
        """
        A credible habitat assessment needs more than a green-looking map.
        The next stages will investigate:

        - **Habitat & vegetation** — forest cover, structure and forage
        - **Water & wallowing** — availability and seasonal reliability
        - **Space & connectivity** — usable area, terrain and movement
        - **Threats & security** — roads, settlements, poaching risk and disturbance
        - **Ecological interactions** — including potential competition with banteng
        - **People & governance** — local communities and park management
        """
    )
    st.info(
        "No suitability score is calculated yet. We first need defensible, "
        "documented datasets and criteria."
    )

st.divider()
st.subheader("How to read this prototype")
a, b, c = st.columns(3)
a.markdown("**01 · Locate**\n\nUnderstand the study landscape and its reference locations.")
b.markdown("**02 · Gather evidence**\n\nAdd sourced spatial datasets with dates, resolution and licenses.")
c.markdown("**03 · Assess carefully**\n\nBuild transparent criteria and document uncertainty before any scoring.")

st.markdown(
    '<p class="small-muted">Basemap © OpenStreetMap contributors. '
    'Reference coordinates: official Alas Purwo National Park website. '
    'This prototype is independent and is not an official government product.</p>',
    unsafe_allow_html=True,
)
