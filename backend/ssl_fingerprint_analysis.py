import ssl
import socket

def run(url):
    try:
        hostname = url.replace('https://', '').replace('http://', '').split('/')[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return f"SSL/TLS Fingerprint for {url}: {cert['subject']}"
    except Exception as e:
        return f"Error analyzing SSL/TLS fingerprint for {url}: {e}"
