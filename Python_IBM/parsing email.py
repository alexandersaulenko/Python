import re

string = """The following is an automated response sent to you by the QRadar event custom rules engine:
 
Nov 14, 2020 1:21:43 PM MSK 
 
Rule Name: ABC-IWH_UKN.1-A2: Not categorized sec incidents (Unclassified)
Rule Description:
 
Source IP: 10.192.1.48
Source Port: 0
Source Username (from event): root
Source Network: Server_Network.Server_Network
 
Destination IP: 10.192.1.48
Destination Port: 0
Destination Username (from Asset Identity): hard
Destination Network: Server_Network.Server_Network
 
Protocol: other(255)
QID: 44251509
Event Name: Session Started for user
Event Description: Session Started for user
Category: Privilege Escalation Succeeded
Log Source ID: 7913
Log Source Name: Linux OS @ bis
Payload: <86>Nov 14 13:21:42 bis sudo: pam_unix(sudo:session): session opened for user root by alex(uid=0)"""

# Parsing Rule Name
rule_name_list =  re.findall("(?<=Rule\sName:\s).*", string)
rule_name_str = ''.join(rule_name_list)
#print(rule_name_str)

# Parsing Rule Description
rule_description_list =  re.findall("(?<=Rule\sDescription:).*", string)
rule_description_str = ''.join(rule_description_list)



# Parsing Source IP
source_ip_list = re.findall("(?<=Source\sIP:\s).*", string)
source_ip_str = ''.join(source_ip_list)

# Parsing Source Port
source_port_list = re.findall("(?<=Source\sPort:\s).*", string)
source_port_str = ''.join(source_port_list)

#Parsing Source Username (from event)
source_username_list = re.findall("(?<=Source\sUsername\s.from\sevent.:\s).*", string)
source_username_str= ''.join(source_username_list)

#Parsing Source Network
source_network_list = re.findall("(?<=Source\sNetwork:\s).*", string)
source_network_str= ''.join(source_network_list)



# Parsing Destination IP
destination_ip_list = re.findall("(?<=Destination\sIP:\s).*", string)
destination_ip_str = ''.join(destination_ip_list)

#Parsing Destination Port
destination_port_list = re.findall("(?<=Destination\sPort:\s).*", string)
destination_port_str = ''.join(destination_port_list)

# Parsing Destination Username (from Asset Identity)
destination_username_list = re.findall("(?<=Destination\sUsername\s.from\sAsset\sIdentity.:\s).*", string)
destination_username_str = ''.join(destination_username_list)

# Parsing Destination Network
destination_network_list = re.findall("(?<=Destination\sNetwork:\s).*", string)
destination_network_str= ''.join(destination_network_list)




# Parsing Protocol
protocol_list =  re.findall("(?<=Protocol:\s).*", string)
protocol_str = ''.join(protocol_list)

# Parsing QID
QID_list = re.findall("(?<=QID:\s)\d+", string)
QID_str = ''.join(QID_list)

# Parsing Event Name
event_name_list =  re.findall("(?<=Event\sName:\s).*", string)
event_name_str = ''.join(event_name_list)

# Parsing Event Description
event_description_list =  re.findall("(?<=Event\sDescription:\s).*", string)
event_description_str = ''.join(event_description_list)

# Parsing Category
category_list =  re.findall("(?<=Category:\s).*", string)
category_str = ''.join(category_list)

# Parsing Log Source ID
log_source_id_list = re.findall("(?<=Log\sSource\sID:\s).*", string)
log_source_id_str = ''.join(log_source_id_list)


# Parsing Log Source Name
log_source_name_list = re.findall("(?<=Log\sSource\sName:\s).*", string)
log_source_name_str = ''.join(log_source_name_list)

# Parsing Payload
payload_list =  re.findall("(?<=Payload:\s).*", string)
payload_str = ''.join(payload_list)
print(payload_str)







