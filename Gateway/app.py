from mitmproxy import http
import itertools

# List of service URLs
service_urls = [
    "https://small-language-model-3001.apps.cluster.intel.sandbox1234.opentlc.com",
    "https://small-language-model-3000.apps.cluster.intel.sandbox1234.opentlc.com"
]

# Create a round-robin iterator
service_iterator = itertools.cycle(service_urls)

def request(flow: http.HTTPFlow) -> None:
    # Get the next service URL in the round-robin sequence
    service_url = next(service_iterator)
    # Construct the full URL to redirect to
    redirect_url = f"{service_url}{flow.request.path}"
    # Modify the request URL
    flow.request.url = redirect_url

# To run the proxy, use the following command:
# mitmdump -s ./Gateway/app.py -p 3000 --listen-host 0.0.0.0
