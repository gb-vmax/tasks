# Bug Report

### Describe the bug
When importing Postman collections, folder descriptions are not being preserved. All imported folders end up with empty descriptions even when the original Postman collection had descriptions defined for those folders.

### Reproduction
```js
// Import a Postman collection with folder descriptions
const postmanCollection = {
  item: [
    {
      name: "API Endpoints",
      description: "This folder contains all API endpoint requests",
      item: [...]
    }
  ]
}

// After import, the folder description is empty
// Expected: "This folder contains all API endpoint requests"
// Actual: ""
```

### Steps to reproduce:
1. Export a Postman collection that has folders with descriptions
2. Import the collection into Insomnia
3. Check the imported folder properties
4. Notice that the description field is empty

### Expected behavior
Folder descriptions from Postman collections should be imported and preserved in Insomnia. The description text should be visible in the imported request groups.

### Additional context
This seems to have started recently. Previously imported collections retained their folder descriptions correctly.

---
Repository: /testbed
