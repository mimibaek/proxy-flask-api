from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_from_foodsafety(entp_name, site_addr):
    api_url = "https://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
    params = {
        "serviceKey": "2e826ed6953145f789f5",
        "returnType": "json",
        "entpName": entp_name,
        "siteAddr": site_addr,
        "pageNo": 1,
        "numOfRows": 10
    }
    try:
        res = requests.get(api_url, params=params, timeout=10, verify=False)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

@app.route("/proxy/company-search")
def proxy():
    entp_name = request.args.get("name", default="서울우유")
    site_addr = request.args.get("addr", default="서울")
    result = fetch_from_foodsafety(entp_name, site_addr)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)