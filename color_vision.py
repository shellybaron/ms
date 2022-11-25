class ColorVision:
  def __init__(self, test_date, test_ts, test_method, eye_tested, general_section_num,
               general_section_total, general_section_success_rate,
               tritan_section_num, tritan_section_total, tritan_section_success_rate,
               protan_section_num, protan_section_total, protan_section_success_rate,
               deutan_section_num, deutan_section_total, deutan_section_success_rate,
               test_result):
      self.test_date = test_date
      self.test_ts = test_ts
      self.test_method = test_method
      self.eye_tested = eye_tested
      self.general_section_num = general_section_num
      self.general_section_total = general_section_total
      self.general_section_success_rate = general_section_success_rate
      self.tritan_section_num = tritan_section_num
      self.tritan_section_total = tritan_section_total
      self.tritan_section_success_rate = tritan_section_success_rate
      self.protan_section_num = protan_section_num
      self.protan_section_total = protan_section_total
      self.protan_section_success_rate = protan_section_success_rate
      self.deutan_section_num = deutan_section_num
      self.deutan_section_total = deutan_section_total
      self.deutan_section_success_rate = deutan_section_success_rate
      self.test_result = test_result
