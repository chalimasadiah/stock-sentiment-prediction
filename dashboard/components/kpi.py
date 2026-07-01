import streamlit as st


def render_kpi():
    """
    Render 4 KPI cards.
    Uses st.columns + native st.metric to avoid HTML render issues.
    """

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """<div class="kpi-card"><div class="kpi-icon blue"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/></svg></div><div class="kpi-body"><div class="kpi-label">Dataset</div><div class="kpi-value">6,867</div><div class="kpi-sub">Articles</div></div></div>""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """<div class="kpi-card"><div class="kpi-icon purple"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#7C3AED" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></div><div class="kpi-body"><div class="kpi-label">Model</div><div class="kpi-value">Random Forest</div><div class="kpi-sub">Classifier</div></div></div>""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """<div class="kpi-card"><div class="kpi-icon green"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div><div class="kpi-body"><div class="kpi-label">Validation Accuracy</div><div class="kpi-value">75.0%</div><div class="kpi-sub">Accuracy Score</div></div></div>""",
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """<div class="kpi-card"><div class="kpi-icon amber"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg></div><div class="kpi-body"><div class="kpi-label">Forecast Horizon</div><div class="kpi-value">T+1</div><div class="kpi-sub">1 Trading Day</div></div></div>""",
            unsafe_allow_html=True
        )
