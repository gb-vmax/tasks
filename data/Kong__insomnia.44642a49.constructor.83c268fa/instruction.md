# Bug Report

### Describe the bug

When importing Postman collections, the importer fails to process the collection data correctly. The collection appears to be empty or undefined after initialization, causing the import to fail silently or produce no results.

### Reproduction

```js
const postmanCollection = {
  info: {
    name: 'My API Collection',
    schema: 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'
  },
  item: [
    {
      name: 'Get Users',
      request: {
        method: 'GET',
        url: 'https://api.example.com/users'
      }
    }
  ]
}

// Try to import the collection
const importer = new ImportPostman(postmanCollection)
// Collection data is not accessible/processed correctly
```

### Expected behavior

The importer should correctly parse and store the Postman collection data, making all items and requests available for import into Insomnia.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. Previously, Postman collections were importing without any issues.

---
Repository: /testbed
