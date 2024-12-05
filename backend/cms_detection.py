import requests

def run(url):
    try:
        # Ensure the URL has the correct scheme
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        # Make a GET request to fetch the content of the main page
        response = requests.get(url, timeout=10, allow_redirects=True)
        html = response.text.lower()
        headers = {k.lower(): v.lower() for k, v in response.headers.items()}  # Normalize headers for case-insensitivity

        # List of CMS identifiers
        cms_signatures = {
            'wordpress': ["wp-content", "wp-admin", "generator: wordpress", "x-powered-by: wordpress"],
            'joomla': ["joomla", "x-powered-by: joomla", "generator: joomla"],
            'drupal': ["sites/default", "x-drupal-cache", "generator: drupal"],
            'strapi': ["strapi", "x-powered-by: strapi"],
            'ghost': ["ghost", "x-powered-by: ghost", "generator: ghost"],
            'squarespace': ["squarespace", "server: squarespace"],
            'wix': ["wix", "wix.com", "server: wix"],
            'shopify': ["shopify", "x-shopify-stage", "x-powered-by: shopify"]
        }

        # Check for CMS-specific markers in the HTML content and headers
        for cms, signatures in cms_signatures.items():
            if any(signature in html or signature in str(headers.values()) for signature in signatures):
                return f"Detected CMS: {cms.capitalize()} on {url}"

        # Additional URL-specific checks
        # Check /sitemap.xml for CMS-specific markers
        sitemap_url = f"{url.rstrip('/')}/sitemap.xml"
        try:
            sitemap_response = requests.get(sitemap_url, timeout=5, allow_redirects=True)
            if sitemap_response.status_code == 200:
                if "wordpress" in sitemap_response.text.lower():
                    return f"Detected CMS: WordPress on {url} (via sitemap.xml)"
                elif "joomla" in sitemap_response.text.lower():
                    return f"Detected CMS: Joomla on {url} (via sitemap.xml)"
                elif "drupal" in sitemap_response.text.lower():
                    return f"Detected CMS: Drupal on {url} (via sitemap.xml)"
        except requests.exceptions.RequestException:
            pass  # Ignore sitemap errors

        # Check /ghost for Ghost-specific markers
        ghost_url = f"{url.rstrip('/')}/ghost"
        try:
            ghost_response = requests.get(ghost_url, timeout=5, allow_redirects=True)
            if ghost_response.status_code == 200:
                if "ghost" in ghost_response.text.lower():
                    return f"Detected CMS: Ghost on {url} (via /ghost)"
        except requests.exceptions.RequestException:
            pass  # Ignore ghost path errors

        return f"No CMS detected for {url}."
    
    except requests.exceptions.RequestException as e:
        return f"Error detecting CMS for {url}: {e}"
