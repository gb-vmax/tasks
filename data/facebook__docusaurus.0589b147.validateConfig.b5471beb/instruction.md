# Bug Report

### Describe the bug

When validating the Docusaurus configuration file, validation errors are not being thrown properly. Instead of stopping the build process when there are configuration errors, Docusaurus continues and returns the value as if the configuration was valid.

### Reproduction

Create a `docusaurus.config.js` with invalid fields:

```js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  invalidField: 'this should not be allowed',
  anotherBadField: 123,
  // ... other config
}
```

Run `docusaurus start` or `docusaurus build`.

### Expected behavior

Docusaurus should throw an error indicating that `invalidField` and `anotherBadField` are not recognized fields and suggest moving them to `customFields`. The build/start process should fail with a clear error message.

### Actual behavior

The configuration validation passes without throwing an error, even though there are unrecognized fields in the config file. The site continues to build/start normally, which could lead to unexpected behavior or silent failures.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
