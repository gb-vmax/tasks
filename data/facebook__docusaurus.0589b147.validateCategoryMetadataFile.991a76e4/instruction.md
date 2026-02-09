# Bug Report

### Describe the bug

I'm getting validation errors thrown when trying to use valid category metadata in my sidebar configuration. The validation is rejecting perfectly valid metadata files and throwing errors even when the content is correct.

### Reproduction

```js
// _category_.json
{
  "label": "My Category",
  "position": 2,
  "link": {
    "type": "generated-index"
  }
}
```

When I try to use this valid category metadata file, I get an error thrown even though the structure is completely valid according to the schema.

### Expected behavior

Valid category metadata files should pass validation without throwing errors. The validator should only throw when the metadata is actually invalid.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, the same metadata files were working fine.

---
Repository: /testbed
