# Bug Report

### Describe the bug

When importing a Postman collection that contains disabled folders, the importer is creating empty folder structures in the workspace. These folders should be excluded from the import since they're marked as disabled and don't contain any active requests.

### Reproduction

1. Create a Postman collection with the following structure:
```json
{
  "item": [
    {
      "name": "Disabled Folder",
      "disabled": true,
      "item": [
        {
          "name": "Request inside disabled folder",
          "request": {
            "method": "GET",
            "url": "https://example.com"
          }
        }
      ]
    },
    {
      "name": "Active Folder",
      "item": [
        {
          "name": "Active Request",
          "request": {
            "method": "POST",
            "url": "https://example.com/api"
          }
        }
      ]
    }
  ]
}
```

2. Import this collection into Insomnia
3. Observe that the "Disabled Folder" appears in the workspace hierarchy even though it's marked as disabled

### Expected behavior

Folders marked with `"disabled": true` should be completely excluded from the import, along with all their child items. Only active folders and requests should be imported into the workspace.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
