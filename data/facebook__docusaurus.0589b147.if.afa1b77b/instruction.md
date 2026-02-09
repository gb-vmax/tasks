# Bug Report

### Describe the bug

I'm encountering an issue where invalid translation files are being silently accepted without proper validation. When a translation file has incorrect structure or invalid content, it's not being caught and validated properly.

### Reproduction

1. Create a translation file with invalid JSON structure or content that doesn't match the expected format
2. Try to load the translation file
3. The file is accepted without validation, leading to potential runtime errors later

For example, if I have a malformed translation file like:

```json
{
  "invalid": "structure",
  "missing": "required fields"
}
```

This gets loaded without any validation errors, even though it doesn't conform to the expected translation file schema.

### Expected behavior

Translation files should be validated against the expected schema before being accepted. If a file has invalid structure, an error should be thrown immediately during the loading process, not later when the translations are actually used.

The validation should happen before the content is returned, so that any issues are caught early in the build process.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
