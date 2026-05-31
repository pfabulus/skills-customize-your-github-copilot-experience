# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI that exposes CRUD operations for a data model and returns JSON responses with automatic API documentation.

## 📝 Tasks

### 🛠️ Create the FastAPI App and Data Model

#### Description
Set up a FastAPI application and define a Pydantic model that represents the API resource.

#### Requirements
Completed program should:

- Import and instantiate `FastAPI`
- Define a Pydantic model for the resource (for example, `Item` or `Book`)
- Use an in-memory list to store resource entries
- Provide an initial sample of stored data

### 🛠️ Implement CRUD Endpoints

#### Description
Build REST endpoints that allow clients to create, read, update, and delete resources.

#### Requirements
Completed program should:

- Implement a `GET` endpoint to return all resources
- Implement a `GET` endpoint to return a single resource by ID
- Implement a `POST` endpoint to create a new resource
- Implement a `PUT` or `PATCH` endpoint to update an existing resource by ID
- Implement a `DELETE` endpoint to remove a resource by ID

### 🛠️ Validate Input and Use Built-In Docs

#### Description
Use FastAPI validation features and verify the API documentation is available.

#### Requirements
Completed program should:

- Validate request payloads using Pydantic model fields
- Return appropriate status codes for success and error cases
- Make the automatic OpenAPI docs available at `/docs`
- Include clear field names and types in the model definitions
