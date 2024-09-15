import allure
from pydantic import ValidationError
from core.models.booking import BookingResponse
from pydantic import BaseModel


@allure.feature('Test create booking')
@allure.story('Test positiv create booking')
def test_create_booking(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.create_booking(booking_data)

    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


