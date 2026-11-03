import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_booking_happy_path_and_negative_cases():
    # 1. Get auth token
    auth_response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=20
    )
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]
    assert token

    # 2. Create a booking
    booking_payload = {
        "firstname": "Srinivas",
        "lastname": "Rao",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-10", "checkout": "2026-11-15"},
        "additionalneeds": "Breakfast"
    }
    create_response = requests.post(
        f"{BASE_URL}/booking", json=booking_payload, timeout=20
    )
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]
    assert booking_id

    # 3. Read booking and verify important fields
    read_response = requests.get(f"{BASE_URL}/booking/{booking_id}", timeout=20)
    assert read_response.status_code == 200
    assert read_response.json()["firstname"] == "Srinivas"
    assert read_response.json()["totalprice"] == 250

    # 4. Negative: update without a token
    no_token_update = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=booking_payload,
        headers={"Accept": "application/json"},
        timeout=20
    )
    assert no_token_update.status_code in (401, 403)

    # 5. Update with token
    updated_payload = {**booking_payload, "totalprice": 300}
    update_response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=updated_payload,
        headers={
            "Cookie": f"token={token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        timeout=20
    )
    assert update_response.status_code == 200
    assert update_response.json()["totalprice"] == 300

    # 6. Negative: fetch an id that should not exist
    missing_response = requests.get(f"{BASE_URL}/booking/999999999", timeout=20)
    assert missing_response.status_code == 404

    # 7. Delete booking
    delete_response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers={"Cookie": f"token={token}", "Accept": "application/json"},
        timeout=20
    )
    assert delete_response.status_code in (201, 200)

    # 8. Negative: fetch deleted booking again
    deleted_read = requests.get(f"{BASE_URL}/booking/{booking_id}", timeout=20)
    assert deleted_read.status_code == 404
