# Bug Report

### Describe the bug

When validating Docusaurus configuration with invalid or unknown fields, the error messages are being displayed incorrectly. The error output appears to be showing the wrong messages or formatting them in an unexpected way.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  unknownField: 'test',  // This should trigger a validation error
  anotherUnknown: 'value',
  // ... other config
}
```

When running the build or start command, the validation error messages don't seem to be showing up as expected. It looks like the error formatting logic might have an issue.

### Expected behavior

Configuration validation errors should properly display all relevant error messages, especially for unknown/invalid configuration fields. The error output should clearly indicate what went wrong with the config.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
