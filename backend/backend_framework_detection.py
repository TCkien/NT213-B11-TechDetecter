import requests

def run(url):
    try:
        # Ensure the URL has the correct scheme
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        
        # Fetch the website content and headers
        response = requests.get(url, timeout=10, allow_redirects=True)
        html = response.text.lower()
        headers = response.headers

        # Check for backend framework indicators
        if "asp.net" in headers.get("X-Powered-By", "").lower() or "asp.net" in html:
            return f"Detected Backend Framework: ASP.NET Core on {url}"
        elif "django" in headers.get("X-Powered-By", "").lower() or "django" in html:
            return f"Detected Backend Framework: Django on {url}"
        elif "laravel" in headers.get("X-Powered-By", "").lower() or "laravel" in html:
            return f"Detected Backend Framework: Laravel on {url}"
        elif "rails" in headers.get("X-Powered-By", "").lower() or "ruby on rails" in html or "rails" in html:
            return f"Detected Backend Framework: Ruby on Rails on {url}"
        elif "express" in headers.get("X-Powered-By", "").lower():
            return f"Detected Backend Framework: Express.js on {url}"
        elif "cakephp" in headers.get("X-Powered-By", "").lower() or "cakephp" in html:
            return f"Detected Backend Framework: CakePHP on {url}"
        elif "flask" in headers.get("X-Powered-By", "").lower() or "flask" in html:
            return f"Detected Backend Framework: Flask on {url}"
        elif "spring" in headers.get("X-Powered-By", "").lower() or "spring" in html:
            return f"Detected Backend Framework: Spring Boot on {url}"
        elif "koa" in headers.get("X-Powered-By", "").lower() or "koa" in html:
            return f"Detected Backend Framework: Koa on {url}"
        elif "phoenix" in headers.get("X-Powered-By", "").lower() or "phoenix" in html:
            return f"Detected Backend Framework: Phoenix on {url}"
        else:
            return f"No backend framework detected for {url}."
    
    except Exception as e:
        return f"Error detecting backend framework for {url}: {e}"
