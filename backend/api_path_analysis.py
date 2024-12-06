import requests

def run(url):
    try:
        # Define possible API paths
        api_paths = [
            "/api/",
            "/get",
            "/apiv1",
            "/v1/api",
            "/v2/api",
            "/api/v1",
            "/api/v2"
        ]
        
        results = []
        
        # Check each possible API path
        for path in api_paths:
            api_url = f"{url.rstrip('/')}{path}"
            response = requests.get(api_url)
            
            # If the response status code is 200, consider it as an API
            if response.status_code == 200:
                results.append(f"API detected at {api_url}: {response.text}")
            else:
                results.append(f"No API detected at {api_url}. Status Code: {response.status_code}")
        
        # Return the results of the API checks
        if results:
            return "\n".join(results)
        else:
            return f"No APIs detected for {url}."
        
    except Exception as e:
        return f"Error analyzing API paths for {url}: {e}"
