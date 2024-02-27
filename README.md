# setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# sign
```bash
export SIGNKEY=S0m3key
python3 sign.py a.yaml b.yaml
```
Computes signature for a.yaml and write a signed version in b.yaml

# check
```bash
export SIGNKEY=S0m3key
python3 check.py b.yaml
```
Check if the signature is ok


