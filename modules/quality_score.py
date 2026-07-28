import pandas as pd


def calculate_quality_score(total_cells, missing_cells, duplicate_rows, total_rows):

    score = 100

    if total_cells > 0:
        score -= (missing_cells / total_cells) * 50

    if total_rows > 0:
        score -= (duplicate_rows / total_rows) * 50

    return max(0, round(score, 2))