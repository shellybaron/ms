import json

class MultipleSclerosis:
    def __init__(self, disease_type, diagnosis_ts, age_at_diagnosis, disease_duration_year, disease_duration_month):
        self.disease_type = disease_type
        self.diagnosis_ts = diagnosis_ts
        self.age_at_diagnosis = age_at_diagnosis
        self.disease_duration_year = disease_duration_year
        self.disease_duration_month = disease_duration_month

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


