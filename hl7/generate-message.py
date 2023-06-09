'''
Working with python hl7 module: https://python-hl7.readthedocs.io/en/latest/
'''
# https://towardsdatascience.com/parsing-hl7-with-python-961e19c4d962
import hl7
import json

## sample message
message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'

# Parsing into json
hl7_json = hl7.parse(message)
print(json.dumps(hl7_json, indent=2))

# Checking the length of the message to make sure it was parsed as expected
# print(len(hl7_json))

## get patient name
# print(hl7_json[2][5])
# [[['Doe'], ['John'], ['R']]]

## get only first name
# print(hl7_json[2][5][0][1][0])
# 'John'