# Bug Report

### Describe the bug

Config validation error messages are showing incorrect field paths and not displaying properly when unknown fields are detected in the Docusaurus configuration file.

### Reproduction

Create a `docusaurus.config.js` with an unknown field:

```js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  unknownField: 'test value',
  nested: {
    alsoUnknown: 'another value'
  }
};
```

When running Docusaurus, the error message about unrecognized fields either:
1. Shows the wrong path format (brackets vs dots mixed up)
2. Doesn't display the helpful message about using `customFields` at all

### Expected behavior

Should show a clear error message like:
```
These field(s) ("unknownField", "nested.alsoUnknown") are not recognized in docusaurus.config.js.
If you still want these fields to be in your configuration, put them in the "customFields" field.
See https://docusaurus.io/docs/api/docusaurus-config/#customfields
```

The field paths should use proper dot notation for nested objects and bracket notation for array indices.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
