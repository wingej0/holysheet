import re
from credentials.mongodb import cols_db


def aspire_plus_cols():
    cols = [
        'CompositeScaleScore',
        'CompositePredictedACTScore',
        'CompositePredictedACTScoreRangeLow',
        'CompositePredictedACTScoreRangeHigh',
        'ELAScaleScore',
        'ELAProficiencyLevel',
        'STEMScaleScore',
        'STEMProficiencyLevel',
        'EnglishScaleScore',
        'EnglishProficiencyLevel',
        'EnglishPredictedACTScore',
        'EnglishPredictedACTScoreRangeLow',
        'EnglishPredictedACTScoreRangeHigh',
        'ReadingScaleScore',
        'ReadingProficiencyLevel',
        'ReadingPredictedACTScore',
        'ReadingPredictedACTScoreRangeLow',
        'ReadingPredictedACTScoreRangeHigh',
        'MathScaleScore',
        'MathProficiencyLevel',
        'MathPredictedACTScore',
        'MathPredictedACTScoreRangeLow',
        'MathPredictedACTScoreRangeHigh',
        'ScienceScaleScore',
        'ScienceProficiencyLevel',
        'SciencePredictedACTScore',
        'SciencePredictedACTScoreRangeLow',
        'SciencePredictedACTScoreRangeHigh',
    ]

    formatted_cols = [re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', x) for x in cols]

    aspire_plus = {
        "aspire_plus" : formatted_cols
    }

    cols_db["aspire_plus"].insert_one(aspire_plus)