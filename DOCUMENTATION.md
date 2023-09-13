# Simple Flask API Documentation

This documentation provides information about a simple Flask API with two endpoints: `/api` and `/api/<user_id>`. The API supports various HTTP methods to interact with user data.

## Table of Contents

- [API Endpoints](#api-endpoints)
  - [GET /api](#get-api)
  - [POST /api](#post-api)
  - [GET /api/<user_id>](#get-apiuser_id)
  - [PUT /api/<user_id>](#put-apiuser_id)
  - [DELETE /api/<user_id>](#delete-apiuser_id)

---

## API Endpoints

### GET /api

#### Description

This endpoint retrieves a list of all users in the database.

#### Request

- **Method**: GET
- **URL**: `/api`
- **Headers**: None

#### Response

- **Status Code**: 200 OK
- **Response Body**: JSON array containing a list of user objects.

#### Example

```http
GET /api
``````
#### Response example

```json
    [{
        "id": 1,
        "name": "Mark Essien"
    },
    {
        "id": 2,
        "name": "Stephanie Albert"
    }]
``` 

### POST /api

#### Description

This endpoint creates a user in the database.

#### Request

- **Method**: POST
- **URL**: `/api`
- **Headers**: None

#### Response

- **Status Code**: 201 CREATED
- **Response Body**: Message 

#### Example

```http
POST /api
Content-Type: application/json

{
    "name": "Mark Essien"
}
``````
#### Response example

```json
    {
    "message": "user Mark Essien has been created successfully."
    }
``` 

### GET /api/<user_id>

#### Description

This endpoint fetches a user info.

#### Request

- **Method**: GET
- **URL**: `/api/<user_id>`
- **Headers**: None

#### Response

- **Status Code**: 200 OK
- **Response Body**: JSON object 

#### Example

```http
GET /api/1
``````
#### Response example

```json
    {
    "message": "success",
    "user": {
        "id": 1,
        "name": "Mark Essien"
    }
}
``` 

### PUT /api/<user_id>

#### Description

This endpoint updates a user info.

#### Request

- **Method**: PUT
- **URL**: `/api/<user_id>`
- **Headers**: None

#### Response

- **Status Code**: 200 OK
- **Response Body**: JSON object 

#### Example

```http
PUT /api/1
``````
#### Response example

```json
  {
    "message": "user Mark Essien successfully updated"
  }   
``` 

### DELETE /api/<user_id>

#### Description

This endpoint deletes a user.

#### Request

- **Method**: DELETE
- **URL**: `/api/<user_id>`
- **Headers**: None

#### Response

- **Status Code**: 200 OK
- **Response Body**: JSON object

#### Example

```http
DELETE /api/1
``````
#### Response example

```json
  {
    "message": "user Mark Essien successfully deleted"
  }   
``` 

