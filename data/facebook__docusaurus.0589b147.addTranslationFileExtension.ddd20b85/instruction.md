# Bug Report

### Describe the bug

When specifying translation file paths that contain `.json` anywhere in the path (not just at the end), the system throws an error even though the path is valid. For example, a path like `translations/v2.json.backup/messages` or `my.json.folder/translations` incorrectly triggers a validation error.

### Reproduction

```js
// This now fails incorrectly
const translationPath = 'translations/v2.json.backup/messages';
// Error: Translation file path at "translations/v2.json.backup/messages" must end with ".json".

// Another example that fails
const anotherPath = 'my.json.folder/translations';
// Also throws the same error
```

The validation is checking if `.json` appears anywhere in the path string instead of only checking if the path ends with `.json`.

### Expected behavior

The system should only reject paths that actually end with `.json` extension, not paths that happen to contain `.json` in folder names or other parts of the path. Paths like `translations/v2.json.backup/messages` should be accepted and automatically get `.json` appended to become `translations/v2.json.backup/messages.json`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
