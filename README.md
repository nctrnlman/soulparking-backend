# Todo API Documentation

This API allows you to manage a simple Todo list. You can perform operations such as creating, updating, finishing, retrieving, and deleting Todos.

## Endpoints

### Create Todo

- **URL:** `/todo`
- **Method:** `POST`
- **Request Body:**
  - `title` (string, required): Title of the Todo.
  - `description` (string, required): Description of the Todo.
- **Response:**
  - 201 Created: Returns the created Todo with additional information like `id`, `created_at`, and optional `updated_at`.

### Get All Todos

- **URL:** `/todo`
- **Method:** `GET`
- **Response:**
  - 200 OK: Returns a list of all Todos with details like `id`, `title`, `description`, `created_at`, `updated_at`, and `deleted_at`.

### Get Todo by ID

- **URL:** `/todo/{todo_id}`
- **Method:** `GET`
- **Path Parameter:**
  - `todo_id` (integer, required): ID of the Todo to retrieve.
- **Response:**
  - 200 OK: Returns the Todo with details like `id`, `title`, `description`, `created_at`, `updated_at`, and `deleted_at`.
  - 404 Not Found: If the Todo with the specified ID does not exist.

### Update Todo

- **URL:** `/todo/{todo_id}`
- **Method:** `PUT`
- **Path Parameter:**
  - `todo_id` (integer, required): ID of the Todo to update.
- **Request Body:**
  - `title` (string, required): Updated title of the Todo.
  - `description` (string, required): Updated description of the Todo.
- **Response:**
  - 200 OK: Returns the updated Todo with details like `id`, `title`, `description`, `created_at`, `updated_at`, and `deleted_at`.
  - 400 Bad Request: If the updated Todo's title or description is empty.
  - 404 Not Found: If the Todo with the specified ID does not exist.

### Finish Todo

- **URL:** `/todo/{todo_id}/finish`
- **Method:** `PUT`
- **Path Parameter:**
  - `todo_id` (integer, required): ID of the Todo to mark as finished.
- **Response:**
  - 200 OK: Returns the finished Todo with details like `id`, `title`, `description`, `created_at`, `updated_at`, `finished_at`, and `deleted_at`.
  - 404 Not Found: If the Todo with the specified ID does not exist.

### Delete Todo

- **URL:** `/todo/{todo_id}`
- **Method:** `DELETE`
- **Path Parameter:**
  - `todo_id` (integer, required): ID of the Todo to delete.
- **Response:**
  - 200 OK: Returns the deleted Todo with details like `id`, `title`, `description`, `created_at`, `updated_at`, and `deleted_at`.
  - 400 Bad Request: If the Todo has already been deleted.
  - 404 Not Found: If the Todo with the specified ID does not exist.
