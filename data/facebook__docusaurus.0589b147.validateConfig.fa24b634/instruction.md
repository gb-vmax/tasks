# Bug Report

### Describe the bug

When I provide an unknown configuration field in my `docusaurus.config.js`, the validation error message doesn't show which field is problematic. The error output is empty or doesn't include the expected details about the unknown fields.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  baseUrl: '/',
  unknownField: 'this should trigger an error',
  anotherUnknownField: {
    nested: 'value'
  },
  // ... other valid config
};
```

When running the build or start command, I expect to see an error message telling me that `unknownField` and `anotherUnknownField` are not valid configuration options. However, the validation error message is not showing these unknown fields properly.

### Expected behavior

The config validation should clearly report which fields are unknown/invalid, something like:
```
Error: These field(s) ("unknownField", "anotherUnknownField") are not recognized in docusaurus.config.js
```

Instead, the error message seems to be showing other validation errors but not the unknown field names.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
