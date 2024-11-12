import subprocess
from django.http import HttpResponse
from django.utils.timezone import now
import os
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the System Monitor</h1><p>Go to <a href='/htop'>/htop</a> to view system information.</p>")

def htop_view(request):
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Server time in IST
    server_time = now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    # HTML content for display
    html_content = f"""
    <html>
        <head><title>System Monitor</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> Your_Full_Name</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre><strong>TOP output:</strong>\n{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")
