# Bug Report

### Describe the bug

When I have unknown/unrecognized fields in my `docusaurus.config.js`, the validation error message is not being displayed. The error should tell me which fields are not recognized and suggest using `customFields`, but instead I'm getting a generic error without the helpful details.

### Reproduction

1. Add an unrecognized field to your `docusaurus.config.js`:

```js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  unknownField: 'some value',  // This field doesn't exist
  anotherBadField: 123,
};
```

2. Try to start or build the site
3. The error message doesn't include information about which fields are invalid

### Expected behavior

The error should tell me something like:
```
These field(s) ("unknownField", "anotherBadField") are not recognized in docusaurus.config.js.
If you still want these fields to be in your configuration, put them in the "customFields" field.
See https://docusaurus.io/docs/api/docusaurus-config/#customfields
```

Instead, I'm just getting a generic validation error without the list of problematic fields.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
