# birth_date = date_to_ts("8/18/76", "%m/%d/%y")
    # on = OpticNeuritis(date_to_ts("29/08/2016", "%d/%m/%Y"))
    # now = int(time.time() * 1000)
    # diagnosis_ts = date_to_ts("8/1/96", "%m/%d/%y")
    # age_at_diagnosis = mill_to_years(diagnosis_ts - birth_date)
    # disease_duration_year = mill_to_years(now - diagnosis_ts)
    # disease_duration_month = mill_to_month(now - diagnosis_ts)
    #
    # ms = MultipleSclerosis("Relapsing-remitting", diagnosis_ts, age_at_diagnosis, disease_duration_year, disease_duration_month)
    # p = Patient("55989", "Female", birth_date, ms, on)
    # print(p.toJSON())