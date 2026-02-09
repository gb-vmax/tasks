# Bug Report

### Describe the bug

I'm experiencing an issue with category metadata file validation in the docs plugin. When I create a `_category_.json` file with valid metadata, the build fails with an error. Conversely, when I intentionally use invalid metadata (to test error handling), the build succeeds but the category displays incorrectly or uses the wrong values.

### Reproduction

1. Create a docs folder with a `_category_.json` file containing valid category metadata:
```json
{
  "label": "My Category",
  "position": 2,
  "collapsible": true
}
```

2. Run the build

3. The build throws an error even though the metadata is valid

Alternatively:

1. Create a `_category_.json` with invalid metadata (e.g., wrong types, missing required fields)
2. The build succeeds but the category doesn't work as expected

### Expected behavior

Valid category metadata files should be accepted and the build should succeed. Invalid metadata files should cause validation errors during the build process.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
