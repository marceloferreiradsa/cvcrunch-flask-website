import os
import base64
# random_bytes = os.urandom(32)
# base64_key = base64.b64encode(random_bytes).decode('utf-8')  # Convert bytes to a Base64 string
# print(base64_key)


# random_bytes = os.urandom(32)
# hex_key = random_bytes.hex()  # Convert bytes to a hexadecimal string
# print(hex_key)

print(os.environ.get('FLASK_SECRET_KEY'))