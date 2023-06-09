import hl7
import json

# Create a new HL7 message
hl7_message = hl7.message.Message()

# Set values for MSH segment
hl7_message.msh.msh_1 = "|"
hl7_message.msh.msh_2 = "^~\\&"
hl7_message.msh.msh_3 = "SendingApp"
hl7_message.msh.msh_4 = "SendingFac"
hl7_message.msh.msh_5 = "ReceivingApp"
hl7_message.msh.msh_6 = "ReceivingFac"
hl7_message.msh.msh_7 = "20230607120000"
hl7_message.msh.msh_9 = "ADT^A04"
hl7_message.msh.msh_10 = "MSG00001"
hl7_message.msh.msh_11 = "P"
hl7_message.msh.msh_12 = "2.4"

# Set values for PID segment
pid_segment = hl7_message.add_segment()
pid_segment.pid_1 = "1"
pid_segment.pid_3 = "12345"
pid_segment.pid_5 = "Doe^John"
pid_segment.pid_7 = "19700101"
pid_segment.pid_8 = "M"
pid_segment.pid_11 = "123 Main St^^Los Angeles^CA^90001"
pid_segment.pid_13 = "(123)456-7890"

# Convert HL7 message to JSON
hl7_json = hl7_message.to_json()

# Print the generated JSON
print(json.dumps(hl7_json, indent=2))
