import re
import unicodedata
from indic_transliteration.sanscript import transliterate
from indic_transliteration import sanscript

# Malayalam keyword → Manglish
keyword_map = {
    "എഴുതി": "ezhuthi",         # PRINT
    "വായിക്കുക": "vaayikkuka",   # INPUT
    "വായിക": "vaayika",         # INPUT 
    "സത്യമെങ്കിൽ": "sathyamenkil",  # IF
    "കലമെങ്കിൽ": "kalamenkil",     # ELSE
    "എത്രകാലം": "ethrakaalam",    # WHILE
    "പൂർണ്ണസംഖ്യ": "poornnasankhya",  # INT
    "ദശാംശം": "dashamsham",     # FLOAT
    "സത്യമായ": "sathyamaaya",   # BOOL
    "സത്യം": "sathyam",          # BOOL 
    "വാചകം": "vaachakam"        # STR
}


reserved = set(keyword_map.values())


def ascii_sanitize(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')


def convert_line(line):

    parts = re.split(r'(".*?")', line)
    for i in range(len(parts)):
        if i % 2 == 0: 
            words = re.findall(r'[\u0D00-\u0D7F]+|\w+', parts[i])
            for word in words:
                if word in keyword_map:
                    parts[i] = parts[i].replace(word, keyword_map[word])
                elif re.search(r'[\u0D00-\u0D7F]', word):
                    manglish = transliterate(word, sanscript.MALAYALAM, sanscript.ITRANS)
                    safe_id = ascii_sanitize(manglish.lower()).replace("~n", "n").replace(".h", "h")
                    parts[i] = parts[i].replace(word, safe_id)
    return ''.join(parts)

def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    converted = [convert_line(line) for line in lines]
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(converted)
