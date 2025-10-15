import requests
from requests.exceptions import RequestException, HTTPError, Timeout, ConnectionError

def call_api(method, url, headers=None, params=None, data=None, json=None, timeout=10):
    """
    Hàm gọi API tổng quát bằng requests
    :param method: GET, POST, PUT, DELETE
    :param url: Endpoint API
    :param headers: dict - Header gửi kèm
    :param params: dict - Query string (?key=value)
    :param data: dict - Form data
    :param json: dict - JSON body
    :param timeout: Thời gian chờ tối đa (giây)
    :return: dict - Response JSON hoặc thông báo lỗi
    """
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            timeout=timeout
        )

        # Kiểm tra mã HTTP
        response.raise_for_status()

        # Nếu server trả về JSON
        try:
            return response.json()
        except ValueError:
            return {"message": "Response is not valid JSON", "raw_text": response.text}

    except HTTPError as e:
        return {"error": f"HTTP error occurred: {e}", "status_code": response.status_code}
    except ConnectionError:
        return {"error": "Connection error occurred"}
    except Timeout:
        return {"error": "Request timed out"}
    except RequestException as e:
        return {"error": f"Unexpected error: {e}"}