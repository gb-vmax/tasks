# Bug Report

### Describe the bug

I'm experiencing issues when importing Postman collections with multiple folders. The folder IDs seem to be getting generated incorrectly, causing problems with the folder hierarchy structure.

### Reproduction

When importing a Postman collection that contains multiple folders:

```js
{
  "item": [
    {
      "name": "Folder 1",
      "item": [...]
    },
    {
      "name": "Folder 2", 
      "item": [...]
    },
    {
      "name": "Folder 3",
      "item": [...]
    }
  ]
}
```

The folders are imported but their generated IDs don't increment properly. Instead of getting unique IDs like `__GRP_1__`, `__GRP_2__`, `__GRP_3__`, the IDs seem to be going in the wrong direction or overlapping.

### Expected behavior

Each imported folder should receive a unique, incrementing ID so that the folder structure is maintained correctly and there are no ID conflicts.

### Additional context

This appears to have started recently. The folder import was working fine before but now collections with multiple folders are not importing with the correct structure.

---
Repository: /testbed
