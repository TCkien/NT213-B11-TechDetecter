import requests
from bs4 import BeautifulSoup

def run(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        
        libraries = []
        for script in scripts:
            if script.get('src'):
                if "jquery" in script['src']:
                    libraries.append("jQuery")
                elif "angular" in script['src']:
                    libraries.append("AngularJS")
                elif "react" in script['src']:
                    libraries.append("ReactJS")

        if libraries:
            return f"Detected JavaScript Libraries for {url}: {', '.join(set(libraries))}"
        else:
            return f"No JavaScript libraries detected for {url}."
    except Exception as e:
        return f"Error detecting JavaScript libraries for {url}: {e}"
