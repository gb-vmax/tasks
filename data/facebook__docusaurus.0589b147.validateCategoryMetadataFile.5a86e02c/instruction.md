# Bug Report

### Describe the bug

When loading category metadata files in the docs plugin, invalid content is being accepted without validation. The validation function appears to be passing through malformed metadata instead of throwing errors when the content doesn't match the expected schema.

### Reproduction

```js
// Create a _category_.json file with invalid content
{
  "label": 123,  // should be a string
  "position": "invalid",  // should be a number
  "randomField": "not allowed"
}
```

The plugin loads this file without any validation errors, even though the schema should reject it.

### Expected behavior

The validation should throw an error when the category metadata file contains:
- Wrong types for known fields (e.g., number for label instead of string)
- Invalid field values
- Any content that doesn't conform to the category metadata schema

Instead, it seems like the validation is being bypassed and invalid content is being accepted.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
