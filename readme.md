# Data Retrieval Service

This Flask-based microservice allows end-users to retrieve various datasets related to bookings, guests, bills, room pricing, and rooms.

## Endpoints

- **Get bookings dataset**

    - **URL**: `/dataset/bookings`
    - **Method**: `GET`
    - **Description**: Retrieves the bookings dataset and saves it as a CSV file.
    - **Response**:
        - `200 OK`: File downloaded successfully.
        - `400 Bad Request`: Could not get the data.

- **Get guests dataset**

    - **URL**: `/dataset/guests`
    - **Method**: `GET`
    - **Description**: Retrieves the guests dataset and saves it as a CSV file.
    - **Response**:
        - `200 OK`: File downloaded successfully.
        - `400 Bad Request`: Could not get the data.

- **Get bills dataset**

    - **URL**: `/dataset/bills`
    - **Method**: `GET`
    - **Description**: Retrieves the bills dataset and saves it as a CSV file.
    - **Response**:
        - `200 OK`: File downloaded successfully.
        - `400 Bad Request`: Could not get the data.

- **Get room pricing dataset**

    - **URL**: `/dataset/room-pricing`
    - **Method**: `GET`
    - **Description**: Retrieves the room pricing dataset and saves it as a CSV file.
    - **Response**:
        - `200 OK`: File downloaded successfully.
        - `400 Bad Request`: Could not get the data.

- **Get rooms dataset**

    - **URL**: `/dataset/rooms`
    - **Method**: `GET`
    - **Description**: Retrieves the rooms dataset and saves it as a CSV file.
    - **Response**:
        - `200 OK`: File downloaded successfully.
        - `400 Bad Request`: Could not get the data.
