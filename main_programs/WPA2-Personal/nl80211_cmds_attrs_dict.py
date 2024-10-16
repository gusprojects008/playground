import re

nl80211 = "/usr/include/linux/nl80211.h"

def nl80211_enums_analiser(nl80211_Cfile):
    nl80211_Cfile_lines = nl80211_Cfile.strip().split(',')
    nl80211_dict = {}
    for index, line in enumerate(nl80211_Cfile_lines): # Loop for key(cmd or attr) index(Is the value from function enumerate, a number which will be used as index for each key)
        key = line.strip().split("=")[0].strip()
        if key.startswith("NL80211_"):
           nl80211_dict[key] = hex(index)
    return nl80211_dict

with open(nl80211, "r") as nl80211_enum:
     nl80211_enum_content = nl80211_enum.read()

nl80211_enum_content = re.sub(r"/\*.*?\*/|//.*", "", nl80211_enum_content, re.DOTALL)

nl80211_cmds_match = re.search(r"enum nl80211_commands\s*{([^}]*)};", nl80211_enum_content, re.DOTALL)
nl80211_attrs_match = re.search(r"enum nl80211_attrs\s*{([^}]*)};", nl80211_enum_content, re.DOTALL)

nl80211_cmds = nl80211_enums_analiser(nl80211_cmds_match.group(1)) if nl80211_cmds_match else {}
nl80211_attrs = nl80211_enums_analiser(nl80211_attrs_match.group(1)) if nl80211_attrs_match else {}

print(nl80211_cmds)
print()
print(nl80211_attrs)
