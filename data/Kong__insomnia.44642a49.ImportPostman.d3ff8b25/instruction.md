# Bug Report

### Describe the bug
When importing Postman collections with deeply nested folder structures, the import process seems to hang or take an extremely long time to complete. This appears to affect collections that have many levels of nested folders.

### Reproduction
```js
// Create a Postman collection with multiple levels of nested folders
const collection = {
  info: {
    schema: 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'
  },
  item: [
    {
      name: 'Folder1',
      item: [
        {
          name: 'Folder2',
          item: [
            {
              name: 'Folder3',
              item: [
                // ... many more nested levels
              ]
            }
          ]
        }
      ]
    }
  ]
}

// Try to import this collection
// The import process becomes unresponsive with deep nesting
```

### Expected behavior
The import should complete successfully even with deeply nested folder structures, or at least provide feedback if there's a nesting limit.

### Additional context
This seems to have started happening recently. Collections with moderate nesting (3-4 levels) work fine, but anything deeper causes issues. Not sure if there's supposed to be a maximum depth limit or if this is a regression.

---
Repository: /testbed
