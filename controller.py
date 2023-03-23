import  model_calc as model
import view
from logger import result_logger as log

def button_click():
  oper_type = view.get_type()
  if oper_type == '1':
    value_a = view.get_value()
    value_b = view.get_value()
  if oper_type == '0':
    value_a = view.get_complex_value()
    value_b = view.get_complex_value()
  value_oper = view.get_oper()
  result = model.calc_block(value_a,value_oper,value_b)
  log(value_a,value_oper,value_b,result)
