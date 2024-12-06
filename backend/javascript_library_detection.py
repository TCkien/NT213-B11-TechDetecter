import requests
from bs4 import BeautifulSoup

def run(url):
    try:
        # Fetch the URL content
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = response.text.lower()

        # Check for JavaScript libraries in script tags
        scripts = soup.find_all('script')
        libraries = set()

        for script in scripts:
            if script.get('src'):
                src = script['src'].lower()
                if "jquery" in src:
                    libraries.add("jQuery")
                elif "angular" in src:
                    libraries.add("AngularJS")
                elif "react" in src:
                    libraries.add("ReactJS")
                elif "vue" in src:
                    libraries.add("VueJS")

        # Check for JavaScript libraries in the HTML content
        if "react" in html_content:
            libraries.add("ReactJS")
        if "ng-" in html_content:
            libraries.add("AngularJS")
        if "vue" in html_content:
            libraries.add("VueJS")
        if "jquery" in html_content:
            libraries.add("jQuery")
        # Return detected libraries
        if libraries:
            return f"Detected JavaScript Libraries for {url}: {', '.join(libraries)}"
        else:
            return f"No JavaScript libraries detected for {url}."
    except Exception as e:
        return f"Error detecting JavaScript libraries for {url}: {e}"
