import csv
import time

from color_vision import ColorVision
from eye import Eye
from multiple_sclerosis import MultipleSclerosis
from optic_neuritis import OpticNeuritis
from patient import Patient
from utils import date_to_ts, mill_to_years, mill_to_month


def main():
    patients = {}
    now = int(time.time() * 1000)
    with open('ms.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            code = row["code"]
            if code not in patients:
                gender = row["gender"]
                birth_date = row["Birth_date"]
                birth_date_ts = date_to_ts(row["Birth_date"], "%m/%d/%y")

                # ms
                ms = ms_data(birth_date_ts, now, row)

                # eyes
                left_eye = Eye("left")
                right_eye = Eye("right")

                # missing data
                optic_neuritis_infected_eye = "Right"
                color_tested_eye = row["EyeTested"]

                # on
                optic_neuritis = optic_neuritis_data(row)
                if (optic_neuritis_infected_eye == "Right"):
                    right_eye.setOpticNeuritis(optic_neuritis)
                else:
                    left_eye.setOpticNeuritis(optic_neuritis)

                # color vision
                color_vision = color_vision_data(row)
                if (color_tested_eye == "Right"):
                    right_eye.setColorVision(color_vision)
                else:
                    left_eye.setColorVision(color_vision)

                p = Patient(code, gender, birth_date, birth_date_ts, ms, left_eye, right_eye)
                patients[code] = p

                print(p.toJSON())


def ms_data(birth_date_ts, now, row):
    disease_type = row["last_disease_type"]
    diagnosis_ts = date_to_ts(row["Disease_occurance_date"], "%m/%d/%y")
    age_at_diagnosis = mill_to_years(diagnosis_ts - birth_date_ts)
    disease_duration_year = mill_to_years(now - diagnosis_ts)
    disease_duration_month = mill_to_month(now - diagnosis_ts)
    ms = MultipleSclerosis(disease_type, diagnosis_ts, age_at_diagnosis, disease_duration_year, disease_duration_month)
    return ms

def optic_neuritis_data(row):
    return OpticNeuritis(row["diag_date"], date_to_ts(row["diag_date"], "%d/%m/%Y"))

def color_vision_data(row):
    test_date = row["Date"]
    test_ts = date_to_ts(row["Date"], "%m/%d/%y")
    test_method = row["Method"]
    eye_tested = row["EyeTested"]
    general_section_num = row["GeneralSectionNum"]
    general_section_total = row["GeneralSectionTotal"]
    general_section_success_rate = row["GeneralSection_Index"]
    tritan_section_num = row["TritanSectionNum"]
    tritan_section_total = row["TritanSectionTotal"]
    tritan_section_success_rate = row["TritanSection_Index"]
    protan_section_num = row["ProtanSectionNum"]
    protan_section_total = row["ProtanSectionTotal"]
    protan_section_success_rate = row["ProtanSection_Index"]
    deutan_section_num = row["DeutanSectionNum"]
    deutan_section_total = row["DeutanSectionTotal"]
    deutan_section_success_rate = row["DeutanSection_Index"]
    test_result = row["calculated"]
    color_vision = ColorVision(test_date, test_ts, test_method, eye_tested, general_section_num,
                               general_section_total, general_section_success_rate,
                               tritan_section_num, tritan_section_total, tritan_section_success_rate,
                               protan_section_num, protan_section_total, protan_section_success_rate,
                               deutan_section_num, deutan_section_total, deutan_section_success_rate,
                               test_result)
    return color_vision

main()



