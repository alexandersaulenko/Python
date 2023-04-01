import re
msg = "Ваша заявка зарегестрирована  {123}   {234234234}"

uuids = re.search('Ваша заявка зарегестрирована', msg)

print(uuids)
