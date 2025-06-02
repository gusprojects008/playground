import base64

text = "test"

print(base64.standard_b64encode(text.encode("utf-8")).decode())
