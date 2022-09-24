#dictionaries consist of key-value pairs and every key should be unique

#key can be any number or string

from calendar import month


monthConversions = {
  "Jan":"January",
  "Feb":"February",
  "Mar":"March",
  "Apr":"April",
  "May":"May",
  "Jun":"June",
  "Jul":"July"
}

print(monthConversions["Mar"])

print(monthConversions.get("May"))

#we may assign values to the keys while using "get"

print(monthConversions.get("Hah","not a valid key :("))