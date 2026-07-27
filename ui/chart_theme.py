import plotly.graph_objects as go


def apply_theme(fig):

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Segoe UI",
            size=14,
            color="#374151"
        ),

        title=dict(
            font=dict(
                size=22,
                color="#111827"
            ),
            x=0.02
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=1.08,
            x=1,
            xanchor="right"
        ),

        hoverlabel=dict(
            font_size=14
        )

    )

    return fig