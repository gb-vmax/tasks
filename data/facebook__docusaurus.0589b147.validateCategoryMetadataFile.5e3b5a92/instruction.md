# Bug Report

### Describe the bug

When using invalid category metadata in sidebar configuration, the validation is not working as expected. Invalid metadata files are being silently accepted instead of throwing validation errors, which can lead to unexpected behavior or broken sidebars.

### Reproduction

```js
// _category_.json with invalid content
{
  "label": 123,  // Should be a string
  "position": "invalid",  // Should be a number
  "customProps": "not-an-object"
}
```

The above invalid metadata should fail validation but is currently being accepted without any errors being thrown.

### Expected behavior

The validation should throw an error when the category metadata file contains invalid data types or structure. This would help catch configuration mistakes early during the build process rather than causing issues at runtime.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
