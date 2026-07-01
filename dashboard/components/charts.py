import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# ── Shared Plotly theme ───────────────────────────────────────

CHART_LAYOUT = dict(
    template="plotly_white",
    font=dict(family="Inter, Segoe UI, sans-serif", size=12, color="#475569"),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=8, r=60, t=20, b=8),
    title_font=dict(size=14, color="#0F172A", family="Inter, sans-serif"),
    xaxis=dict(
        gridcolor="#F1F5F9",
        linecolor="#E2E8F0",
        tickfont=dict(size=11),
    ),
    yaxis=dict(
        gridcolor="#F1F5F9",
        linecolor="#E2E8F0",
        tickfont=dict(size=11),
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        borderwidth=0,
        font=dict(size=11),
    ),
)


def render_price_chart(price_df):
    """
    Display IHSG historical closing price trend.
    """

    st.markdown(
        """
        <p class="section-title">IHSG Historical Trend</p>
        <p class="section-desc">Closing price over the last 30 days in the dataset.</p>
        """,
        unsafe_allow_html=True
    )

    # Use last 30 rows if available
    df = price_df.tail(30).copy() if len(price_df) > 30 else price_df.copy()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["close"],
            mode="lines",
            name="Close",
            line=dict(color="#2563EB", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(37,99,235,0.06)",
            hovertemplate="<b>%{x}</b><br>Close: %{y:,.0f}<extra></extra>",
        )
    )

    layout = dict(CHART_LAYOUT)
    layout["title"] = "IHSG Closing Price"
    layout["xaxis"]["title"] = ""
    layout["yaxis"]["title"] = "Price (IDR)"
    layout["height"] = 280

    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True)


def render_sentiment_donut(news_df):
    """
    Display sentiment distribution donut chart.

    Parameters
    ----------
    news_df : pd.DataFrame
        Must contain a 'sentiment_label' column.
    """

    st.markdown(
        """
        <p class="section-title">Sentiment Distribution</p>
        <p class="section-desc">Distribution of sentiment in the news dataset.</p>
        """,
        unsafe_allow_html=True
    )

    if "sentiment_label" not in news_df.columns:
        st.info("Sentiment label column not found in dataset.")
        return

    counts = news_df["sentiment_label"].value_counts().reset_index()
    counts.columns = ["label", "count"]
    total = counts["count"].sum()

    color_map = {
        "Positive": "#2563EB",
        "Neutral":  "#60A5FA",
        "Negative": "#BFDBFE",
    }

    colors = [color_map.get(l, "#94A3B8") for l in counts["label"]]

    fig = go.Figure(
        go.Pie(
            labels=counts["label"],
            values=counts["count"],
            hole=0.6,
            domain=dict(
                x=[0.0, 0.75],
                y=[0.08, 0.92]
            ),
            marker=dict(colors=colors, line=dict(color="white", width=2)),
            textinfo="none",
            hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>%{percent}<extra></extra>",
        )
    )



    fig.update_layout(
        **{k: v for k, v in CHART_LAYOUT.items() if k not in ("xaxis", "yaxis", "legend")},
        height=400,
        title="",
        annotations=[
            dict(
                text=f"<b>{total:,}</b><br><span style='font-size:11px'>Total</span>",
                x=0.375, y=0.5,
                font=dict(size=16, color="#0F172A"),
                showarrow=False,
            )
        ],
        showlegend=True,
        legend=dict(
            orientation="v",
            x=0.82, y=0.5,
            xanchor="left",
            font=dict(size=12),
        ),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Annotation below chart
    for _, row in counts.iterrows():
        pct = row["count"] / total * 100
        st.markdown(
            f'<span style="font-size:12px;color:#475569;">'
            f'<b>{row["label"]}</b>: {pct:.1f}% ({row["count"]:,})'
            f'</span>  ',
            unsafe_allow_html=True
        )


def render_feature_importance(feature_df):
    """
    Display feature importance horizontal bar chart.
    """

    st.markdown(
        """
        <p class="section-title">Model Explainability</p>
        <p class="section-desc">
            The 10 most influential features identified by the Random Forest model
            during training. Higher importance = greater contribution to predictions.
        </p>
        """,
        unsafe_allow_html=True
    )

    top = feature_df.head(10).copy()

    fig = px.bar(
        top,
        x="importance",
        y="feature",
        orientation="h",
        color="importance",
        color_continuous_scale=["#BFDBFE", "#2563EB"],
    )

    layout = dict(CHART_LAYOUT)
    layout["title"] = "Top 10 Most Important Features"
    layout["yaxis"] = dict(categoryorder="total ascending", tickfont=dict(size=12))
    layout["xaxis"] = dict(title="Importance Score", tickfont=dict(size=11))
    layout["coloraxis_showscale"] = False
    layout["height"] = 340

    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Importance: %{x:.4f}<extra></extra>"
    )

    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Feature importance reflects relative contribution during Random Forest training. "
        "Higher importance does not imply a causal relationship with market movement."
    )

    st.info(
        "The forecasting model was trained using **19 engineered features** including "
        "historical IHSG prices, trading volume, technical indicators, and aggregated "
        "daily economic sentiment. The chart shows the **10 most influential** of these."
    )
