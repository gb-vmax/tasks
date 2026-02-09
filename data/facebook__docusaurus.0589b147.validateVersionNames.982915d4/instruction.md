# Bug Report

### Describe the bug

When validating version names in the docs plugin, only every other version is being validated. If you have multiple versions defined, some of them are silently skipped during validation, which means invalid version names can slip through.

### Reproduction

```js
// versions.json
[
  "1.0.0",
  "invalid version!",  // This should fail validation
  "2.0.0",
  "another bad one",   // This should also fail
  "3.0.0"
]
```

With the current behavior, only versions at odd indices (1, 3, etc.) are validated, so "invalid version!" and "another bad one" would be checked, but "1.0.0", "2.0.0", and "3.0.0" would be skipped.

### Expected behavior

All version names in the array should be validated, not just every other one. Every version should go through the validation check to ensure they meet the required format.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
