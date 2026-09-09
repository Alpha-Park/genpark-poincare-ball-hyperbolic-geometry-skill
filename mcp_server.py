import sys
import json
from client import PoincareBallGeometry

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "distance":
        p = PoincareBallGeometry()
        return p.distance(params.get("u", [0, 0]), params.get("v", [0.1, 0.1]))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
