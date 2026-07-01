import streamlit as st


def render_dataset_information(news_df, forecasting_df):
    """
    Display dataset summary.
    No emoji.
    """

    st.markdown(
        """
        <p class="section-title">Dataset Overview</p>
        <p class="section-desc">
            The forecasting model was developed by combining economic news sentiment
            with historical IHSG market data.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div class="kpi-label">Economic News</div>
                <div class="kpi-value" style="font-size:28px;">{len(news_df):,}</div>
                <div class="kpi-sub">Articles</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div class="kpi-label">Forecasting Records</div>
                <div class="kpi-value" style="font-size:28px;">{len(forecasting_df):,}</div>
                <div class="kpi-sub">Daily rows</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div class="kpi-label">News Features</div>
                <div class="kpi-value" style="font-size:28px;">{news_df.shape[1]}</div>
                <div class="kpi-sub">Columns</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div class="kpi-label">Forecast Features</div>
                <div class="kpi-value" style="font-size:28px;">{forecasting_df.shape[1]}</div>
                <div class="kpi-sub">Engineered</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    st.divider()
    
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Dataset Description</span>
                </div>
                <div class="insight-card-body">
                    The forecasting dataset combines historical IHSG trading data
                    with daily aggregated economic news sentiment.<br><br>
                    Instead of using individual news articles, the model learns
                    from daily sentiment statistics together with technical indicators.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_right:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Data Sources</span>
                </div>
                <div class="insight-card-body">
                    <b>Huggingface.co</b> — Economic news articles<br><br>
                    <b>Yahoo Finance</b> — IHSG historical prices<br><br>
                    Daily aggregated sentiment features<br><br>
                    Engineered technical indicators
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    st.markdown(
        '<p class="section-title" style="margin-bottom:12px;">Data Processing Pipeline</p>',
        unsafe_allow_html=True
    )

    st.code(
        """
Economic News Articles
        |
        v
Rule-based Sentiment Analysis
        |
        v
Daily Sentiment Aggregation
        |
        v
Feature Engineering
        |
        +-------------+
        v             v
Historical IHSG     Technical Indicators
Market Data
        |             |
        +------+------+
               v
   Forecasting Dataset
               |
               v
   Random Forest Model
               |
               v
Next-Day IHSG Direction
        """,
        language=None
    )
