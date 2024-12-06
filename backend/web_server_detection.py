import requests

def run(url):
    try:
        # Ensure URL has the proper scheme
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        
        # Send the GET request
        response = requests.get(url, timeout=10)
        
        # Extract relevant headers
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        via = response.headers.get('Via', 'Unknown')
        
        # Build the result message
        detected = []
        if server != 'Unknown':
            detected.append(f"Server: {server}")
        if powered_by != 'Unknown':
            detected.append(f"X-Powered-By: {powered_by}")
        if via != 'Unknown':
            detected.append(f"Via: {via}")
        
        # Analyze HTML for potential server markers
        html_lower = response.text.lower()
        if "nginx" in html_lower:
            detected.append("HTML suggests: nginx")
        if "apache" in html_lower:
            detected.append("HTML suggests: Apache HTTP Server")
        if "lighttpd" in html_lower or "lighty" in html_lower:
            detected.append("HTML suggests: Lighttpd")
        if "iis" in html_lower:
            detected.append("HTML suggests: Microsoft IIS")
        
        # Additional checks for specific headers or server behaviors
        if 'lighttpd' in server.lower():
            detected.append("Server header indicates: Lighttpd")
        if 'apache' in server.lower():
            detected.append("Server header indicates: Apache HTTP Server")
        
        # Return the result
        if detected:
            return f"Web Server(s) Detected for {url}: {', '.join(detected)}"
        else:
            return f"No detailed server information could be detected for {url}."
    
    except Exception as e:
        return f"Error detecting web server for {url}: {e}"
