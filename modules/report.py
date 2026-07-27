from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.enums import TA_CENTER

from reportlab.lib.units import inch

from datetime import datetime

from streamlit import table

from modules import summary


def generate_report(
    summary,
    quality_score,
    missing_df,
    duplicate_df,
    insights,
    memory_usage,
    filename
):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER

    heading = styles["Heading1"]

    body = styles["BodyText"]

    story = []

   # =========================================
    # Cover Page
    # =========================================

    story.append(Spacer(1, 1 * inch))

    story.append(
        Paragraph(
            "<font color='#2563EB' size=28><b>DataLens AI</b></font>",
            title
        )
    )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            "<b>Intelligent Data Quality Audit Platform</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,30))

    story.append(
        Paragraph(
            "<font size=18>Professional Data Quality Assessment Report</font>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,40))

    cover_table = Table(
        [
            ["Rows", f"{summary['Rows']:,}"],
            ["Columns", summary["Columns"]],
            ["Quality Score", f"{quality_score}/100"],
            ["Generated", datetime.now().strftime("%d %B %Y %I:%M %p")]
        ],
        colWidths=[170,250]
    )

    cover_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#2563EB")),
        ("TEXTCOLOR",(0,0),(0,-1),colors.white),
        ("BACKGROUND",(1,0),(1,-1),colors.whitesmoke),
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
        ("BOTTOMPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),10),
        ("ALIGN",(0,0),(-1,-1),"CENTER")
    ]))

    story.append(cover_table)

    story.append(Spacer(1,180))

    story.append(
        Paragraph(
            "<font color='grey'><i>Generated using DataLens AI</i></font>",
            styles["Italic"]
        )
    )

    story.append(PageBreak())

    # =========================================
    # Executive Summary
    # =========================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading
        )
    )

    story.append(Spacer(1, 20))

    missing_percent = (
        summary["Missing Values"]
        / (summary["Rows"] * summary["Columns"])
    ) * 100

    duplicate_percent = (
        summary["Duplicate Rows"]
        / summary["Rows"]
    ) * 100

    table_data = [

        ["Metric", "Value"],

        ["Rows", f"{summary['Rows']:,}"],

        ["Columns", summary["Columns"]],

        ["Missing Values", f"{summary['Missing Values']:,} ({missing_percent:.2f}%)"],

        ["Duplicate Rows", f"{summary['Duplicate Rows']:,} ({duplicate_percent:.2f}%)"],

        ["Numeric Columns", summary["Numeric Columns"]],

        ["Categorical Columns", summary["Categorical Columns"]],

        ["Quality Score", f"{quality_score}/100"]

    ]

    table = Table(
        table_data,
        colWidths=[200, 240]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2563EB")),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.grey),

            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0,0), (-1,0), 12),

            ("ALIGN", (0,0), (-1,-1), "CENTER"),

            ("TOPPADDING", (0,0), (-1,-1), 10),

            ("BOTTOMPADDING", (0,0), (-1,-1), 10),

            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),

        ])

    )

    story.append(table)

    story.append(Spacer(1, 30))

    # =========================================
    # Quality Assessment
    # =========================================

    story.append(
        Paragraph(
            "Overall Quality Assessment",
            heading
        )
    )

    story.append(Spacer(1, 20))

    if quality_score >= 90:

        status = "Excellent"

    elif quality_score >= 75:

        status = "Good"

    elif quality_score >= 60:

        status = "Fair"

    else:

        status = "Poor"

    story.append(

        Paragraph(

            f"""
<b>Quality Score :</b> {quality_score}/100

<br/><br/>

<b>Status :</b> {status}

<br/><br/>

The dataset was automatically audited using
DataLens AI.
""",

            body

        )

    )

    story.append(Spacer(1, 30))

    # =========================================
    # Missing Value Analysis
    # =========================================

    story.append(PageBreak())

    story.append(
        Paragraph(
            "Missing Value Analysis",
            heading
        )
    )

    story.append(Spacer(1,20))

    missing_table = [

        ["Column", "Missing Count", "Missing Percentage"]

    ]
    for _, row in missing_df.head(25).iterrows():

        if row["Missing Count"] > 0:

            missing_table.append([
                row["Column"],
                row["Missing Count"],
                f"{row['Missing Percentage']}%"
            ])
    table = Table(

        missing_table,

        colWidths=[200,120,120]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2563EB")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10)

        ])

    )

    story.append(table)
    story.append(Spacer(1, 10))

    if len(missing_df) > 25:

        story.append(
            Paragraph(
                f"<i>Showing first 25 of {len(missing_df)} columns.</i>",
                body    
            )
        )

    # =========================================
    # Duplicate Analysis
    # =========================================

    story.append(PageBreak())

    story.append(
        Paragraph(
            "Duplicate Analysis",
            heading
        )
    )

    story.append(Spacer(1, 20))

    duplicate_percent = (
        summary["Duplicate Rows"] / summary["Rows"] * 100
    )

    duplicate_table = [

        ["Metric", "Value"],

        ["Duplicate Rows", summary["Duplicate Rows"]],

        ["Duplicate Percentage", f"{duplicate_percent:.2f}%"]
    ]

    table = Table(
        duplicate_table,
        colWidths=[220, 220]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2563EB")),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    story.append(table)

    story.append(Spacer(1,25))   

    if summary["Duplicate Rows"] == 0:
        duplicate_status = "Excellent ✅"
        recommendation = "No duplicate records were detected."

    elif duplicate_percent < 5:
        duplicate_status = "Good 👍"
        recommendation = "Only a small number of duplicate records were found."

    else:
        duplicate_status = "Needs Cleaning ⚠"
        recommendation = "A high number of duplicate records were detected. Remove them before analysis."

    story.append(
        Paragraph(
            f"""
    <b>Status :</b> {duplicate_status}

    <br/><br/>

    <b>Recommendation :</b>

    {recommendation}
    """,
            body
        )
    )

    story.append(Spacer(1,30))

    # =========================================
    # AI Insights
    # =========================================

    story.append(PageBreak())

    story.append(
        Paragraph(
            "AI Insights",
            heading
        )
    )

    story.append(Spacer(1, 20))

    if insights:

        for insight in insights:

            story.append(
                Paragraph(
                    f"• {insight}",
                    body
                )
            )

            story.append(Spacer(1, 10))

    else:

        story.append(
            Paragraph(
                "No AI insights were generated.",
                body
            )
        )

    story.append(Spacer(1, 25))

    story.append(
        Paragraph(
            """
    <b>AI Summary</b>

    <br/><br/>

    DataLens AI analyzed the uploaded dataset and generated
    the above insights based on missing values, duplicates,
    column types and overall data quality.
    """,
            body
        )
    )

    story.append(Spacer(1, 30))
    # =========================================
    # Recommendations
    # =========================================

    story.append(
        Paragraph(
            "Recommendations",
            heading
        )
    )

    story.append(Spacer(1, 15))

    recommendations = [

        "Remove duplicate rows before analysis.",

        "Handle missing values using suitable imputation methods.",

        "Validate important columns such as Email and Date fields.",

        "Perform exploratory data analysis before machine learning.",

        "Maintain consistent data quality checks in future datasets."

    ]

    for rec in recommendations:

        story.append(
            Paragraph(
                f"• {rec}",
                body
            )
        )

        story.append(Spacer(1, 8))

    story.append(Spacer(1, 40))

    story.append(
        Paragraph(
            "<font color='grey'><i>End of Report</i></font>",
            styles["Italic"]
        )
    )

    doc.build(story)