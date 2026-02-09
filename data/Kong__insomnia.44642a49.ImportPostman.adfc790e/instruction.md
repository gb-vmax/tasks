# Bug Report

### Describe the bug

When importing Postman collections, disabled items (requests and folders) are being included in the import instead of being skipped. This causes disabled requests to appear in the workspace even though they should be excluded.

### Reproduction

1. Create a Postman collection with some disabled requests
2. Export the collection as JSON
3. Import the collection into Insomnia
4. Observe that disabled requests are imported and appear in the workspace

Example Postman collection structure:
```json
{
  "item": [
    {
      "name": "Active Request",
      "request": {
        "method": "GET",
        "url": "https://example.com"
      }
    },
    {
      "name": "Disabled Request",
      "disabled": true,
      "request": {
        "method": "POST",
        "url": "https://example.com"
      }
    }
  ]
}
```

### Expected behavior

Disabled requests and folders should be filtered out during import and not appear in the workspace. Only active/enabled items should be imported.

### Additional context

This affects both individual requests marked as disabled and requests within disabled folders. The importer should respect the `disabled` flag at both the item level and the request level.

---
Repository: /testbed
