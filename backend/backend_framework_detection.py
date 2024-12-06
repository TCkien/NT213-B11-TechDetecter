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
        cookies = response.cookies.get_dict()

        # Backend framework detection
        # ASP.NET Core: Check for specific cookies
        if "arraffinity" in cookies or "arraffinitysamesite" in cookies:
            return f"Detected Backend Framework: ASP.NET Core on {url}"

        # Django: Check for /admin path or forms with csrfmiddlewaretoken
        admin_url = f"{url.rstrip('/')}/admin"
        try:
            # Check /admin path
            admin_response = requests.get(admin_url, timeout=5, allow_redirects=True)
            if admin_response.status_code == 200:
                return f"Detected Backend Framework: Django on {url} (via /admin path)"
        except requests.exceptions.RequestException:
            pass

        # Check for forms with csrfmiddlewaretoken in HTML
        if "<form" in html and "csrfmiddlewaretoken" in html:
            return f"Detected Backend Framework: Django on {url} (via CSRF token)"

        # Laravel: Check for forms with _token in HTML
        if "<form" in html and "_token" in html:
            return f"Detected Backend Framework: Laravel on {url}"

        # Ruby on Rails: Check for forms with authenticity_token
        if "<form" in html and "authenticity_token" in html:
            return f"Detected Backend Framework: Ruby on Rails on {url}"

        # Express.js: Check for specific cookies
        if "connect.sid" in cookies:
            return f"Detected Backend Framework: Express.js on {url}"

        # CakePHP: Check for /app/webroot/ path
        webroot_url = f"{url.rstrip('/')}/app/webroot/"
        try:
            webroot_response = requests.get(webroot_url, timeout=5, allow_redirects=True)
            if webroot_response.status_code == 200:
                return f"Detected Backend Framework: CakePHP on {url} (via /app/webroot/ path)"
        except requests.exceptions.RequestException:
            pass

        # Flask: Check for Werkzeug header or set-cookie: session
        if "werkzeug" in headers.get("server", "").lower() or "session" in headers.get("set-cookie", "").lower():
            return f"Detected Backend Framework: Flask on {url}"

        return f"No backend framework detected for {url}."
    
    except Exception as e:
        return f"Error detecting backend framework for {url}: {e}"
