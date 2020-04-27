"""
Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
def validIPAddress(IP):
    if "." in IP:
        subnet = IP.split(".")
        Iprange = list(set(map(lambda x: x < 255, subnet)))
        if len(Iprange) == 1 and Iprange[0]==True:
            return "IPv4"
        else:
            return "Neither"
    else:
        subnet = IP.split(":")
        Iprange = list(set(map(lambda x: x.isalnum(), subnet)))
        if len(Iprange) == 1 and Iprange[0]==True:
            return "IPv4"
        else:
            return "Neither"

IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
IP = "172.16.254.1"
print validIPAddress(IP)



