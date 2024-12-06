import ssl
import socket
import pprint

def run(url):
    try:
        # Extract hostname from URL
        hostname = url.replace('https://', '').replace('http://', '').split('/')[0]
        context = ssl.create_default_context()
        
        # Create a secure connection and retrieve certificate
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        
        # Format and display all certificate details
        cert_details = pprint.pformat(cert, indent=4)
        
        # Additional details: connection info, cipher, and protocol
        cipher = ssock.cipher()
        protocol = ssock.version()

        return f"SSL/TLS Fingerprint for {url}:\n" \
               f"Certificate Details:\n{cert_details}\n" \
               f"Cipher: {cipher}\n" \
               f"Protocol: {protocol}"
    
    except Exception as e:
        return f"Error analyzing SSL/TLS fingerprint for {url}: {e}"
