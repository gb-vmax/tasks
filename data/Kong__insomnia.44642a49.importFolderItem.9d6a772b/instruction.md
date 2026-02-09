# Bug Report

### Describe the bug
When importing Postman collections, folder names are being replaced with their descriptions. If a folder has both a name and a description, the description is used as the folder name instead of the actual name field.

### Reproduction
```js
// Postman collection structure
{
  name: "API Endpoints",
  description: "Collection of all API endpoints for the project",
  // ... other fields
}

// After import, the folder appears as:
// Name: "Collection of all API endpoints for the project"
// Description: "Collection of all API endpoints for the project"

// Expected:
// Name: "API Endpoints"
// Description: "Collection of all API endpoints for the project"
```

### Steps to reproduce
1. Create a Postman collection with folders that have both name and description fields
2. Import the collection into Insomnia
3. Observe that folder names are showing the description text instead of the actual name

### Expected behavior
The folder name should use the `name` field from the Postman collection, not the `description` field. The description should only populate the description field.

### Additional context
This seems to affect all imported folders from Postman collections. The name field is being overwritten by the description during the import process.

---
Repository: /testbed
