import json

class Patient():
    def __init__(self, code, gender, birth_date, birth_date_ts, multiple_sclerosis, left_eye, right_eye):
      self.code = code
      self.gender = gender
      self.birth_date = birth_date
      self.birth_date_ts = birth_date_ts
      self.multiple_sclerosis = multiple_sclerosis
      self.left_eye = left_eye
      self.right_eye = right_eye

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
