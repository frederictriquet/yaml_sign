import yaml
import base64
import hashlib
import hmac
import sys, os

def compute_signature(string_to_sign, secret):
    decoded_secret = base64.b64decode(secret)
    encoded_string_to_sign = string_to_sign.encode('utf-8')
    hashed_bytes = hmac.digest(decoded_secret, encoded_string_to_sign, digest=hashlib.sha256)
    encoded_signature = base64.b64encode(hashed_bytes)
    signature = encoded_signature.decode('utf-8')
    return signature

def load_yaml_file(yaml_filename: str):
    with open(yaml_filename) as file:
        data = yaml.safe_load(file)
        return data

def save_yaml_file(yaml_filename: str, data):
    with open(yaml_filename, "w") as file:
        yaml.dump(data, stream=file,sort_keys=False)


if __name__ == "__main__":
    sign_key = os.environ['SIGNKEY']
    yaml_obj = load_yaml_file(sys.argv[1])
    if 'signature' not in yaml_obj:
        print("The file must have a `signature` field at the root level")
        sys.exit(1)
    yaml_obj['signature'] = ''
    data = yaml.dump(yaml_obj)
    secret = base64.b64encode(sign_key.encode())
    computed_signature = compute_signature(data,secret=secret)
    yaml_obj['signature'] = computed_signature
    save_yaml_file(sys.argv[2], yaml_obj)

