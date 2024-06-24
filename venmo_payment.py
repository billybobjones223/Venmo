import requests
import os

def send_venmo_payment(access_token, user_id, amount, note):
    url = "https://api.venmo.com/v1/payments"
    payload = {
        "user_id": user_id,
        "amount": amount,
        "note": note
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    ACCESS_TOKEN = os.getenv("VENMO_ACCESS_TOKEN")
    USER_ID = os.getenv("VENMO_USER_ID")
    AMOUNT = os.getenv("VENMO_AMOUNT")
    NOTE = os.getenv("VENMO_NOTE")

    result = send_venmo_payment(ACCESS_TOKEN, USER_ID, AMOUNT, NOTE)
    if result:
        print("Payment successful:", result)
    else:
        print("Payment failed.")
