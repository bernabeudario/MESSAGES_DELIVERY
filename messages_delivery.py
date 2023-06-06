import http.client
import sys

def messages_delivery(message):
    conn = http.client.HTTPSConnection("hooks.slack.com")
    payload = "{ 'text': '" + message + "' }"
    headers = {
      'Content-Type': 'text/plain; charset=utf-8'
    }
    conn.request("POST", "/services/TGAN596N6/B05BJ3CDDFS/DpmeZN8wnYkWoWYl9DOJWax2", payload.encode("utf-8"), headers)
    print(conn.getresponse().read().decode("utf-8"))

if __name__ == '__main__':
    messages_delivery(sys.argv[1])