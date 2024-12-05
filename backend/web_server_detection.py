import requests

def run(url):
    try:
        response = requests.get(url)
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.header.get('X-Powered-By', 'Unknown')
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
        if "nginx" in response.text.lower():
            detected.append("HTML suggests: nginx")
        if "apache" in response.text.lower():
            detected.append("HTML suggests: Apache")
        if "iis" in response.text.lower():
            detected.append("HTML suggests: Microsoft IIS")
        
        # Return the result
        if detected:
            return f"Web Server(s) Detected for {url}: {', '.join(detected)}"
        else:
            return f"No detailed server information could be detected for {url}."
    except Exception as e:
        return f"Error detecting web server for {url}: {e}"
