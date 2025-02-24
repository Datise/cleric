import urllib.error
import urllib.parse
import urllib.request
import json
import typing
def Send(data: dict):
    url = "http://127.0.0.1:8000/v1/agent/upload"
    method = "POST"
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(data).encode()

    httprequest = urllib.request.Request(
        url, data=data, headers=headers, method=method
    )

    try:
        with urllib.request.urlopen(httprequest) as httpresponse:
            response = Response(
                headers=httpresponse.headers,
                status=httpresponse.status,
                body=httpresponse.read().decode(
                    httpresponse.headers.get_content_charset("utf-8")
                ),
            )
    except urllib.error.HTTPError as e:
        response = Response(
            body=str(e.reason),
            headers=e.headers,
            status=e.code,
            error_count=error_count + 1,
        )

    print(response)
    return response

class Response(typing.NamedTuple):
    body: str
    headers: str
    status: int
    error_count: int = 0

    def json(self) -> typing.Any:
        """
        Decode body's JSON.

        Returns:
            Pythonic representation of the JSON object
        """
        try:
            output = json.loads(self.body)
        except json.JSONDecodeError:
            output = ""
        return output