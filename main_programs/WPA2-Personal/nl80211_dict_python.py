import re

nl80211 = "/usr/include/linux/nl80211.h"
        
def nl80211_enums_analiser(nl80211_Cfile):
    nl80211_Cfile_lines = nl80211_Cfile.strip().split(',')
    nl80211_dict = {}
    index = 0

    for line in nl80211_Cfile_lines: # Loop for key(cmd or attr) index(Is the value from function enumerate, a number which will be used as index for each key)
        clean_line = re.sub(r'[\n\t]+', '', line.strip())
        if clean_line in nl80211_dict: # Verify if line already exist
           continue # Skinp the iteration index and continue the for loop
        nl80211_dict[clean_line] = index
        if '=' in clean_line:
           key_split = clean_line.split('=')
           key_value = eval(key_split[1].strip(), {}, nl80211_dict)
           nl80211_dict.update({clean_line: key_value})
        else:  
            index += 1
    return {key: hex(index) for key, index in nl80211_dict.items()} # for "key:" the hex() function go iterate over index(iterable) in nl80211_dict.items()

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
print()
print(nl80211_cmds["NL80211_CMD_TRIGGER_SCAN"])

