import requests

def run(url):
    try:
        api_url = f"{url.rstrip('/')}/api/"
        response = requests.get(api_url)
        if response.status_code == 200 and response.headers.get('Content-Type') == 'application/json':
            return f"API Detected for {url}: {response.json()}"
        else:
            return f"No API detected for {url}."
    except Exception as e:
        return f"Error analyzing API paths for {url}: {e}"
