# Bug Report

### Describe the bug
When importing Postman collections that contain items with duplicate names at the same level, the importer doesn't properly handle name conflicts. All items keep their original names even when duplicates exist, which can cause confusion and potential issues when working with the imported collection.

### Reproduction
```js
// Example Postman collection structure with duplicate names
{
  "item": [
    {
      "name": "Get User",
      "request": { /* ... */ }
    },
    {
      "name": "Get User",
      "request": { /* ... */ }
    },
    {
      "name": "Get User",
      "request": { /* ... */ }
    }
  ]
}
```

When importing this collection, all three requests end up with the name "Get User" instead of being renamed to something like:
- Get User
- Get User (2)
- Get User (3)

### Expected behavior
The importer should detect duplicate names within the same folder/level and automatically append a counter suffix (e.g., "(2)", "(3)") to make each item name unique, similar to how file systems handle duplicate filenames.

### System Info
- Insomnia version: latest
- Import format: Postman Collection v2.1

---
Repository: /testbed
