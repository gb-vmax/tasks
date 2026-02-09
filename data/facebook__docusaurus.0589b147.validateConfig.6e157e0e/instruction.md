# Bug Report

### Describe the bug

When the Docusaurus config validation encounters errors, the error messages are not being displayed correctly. It seems like validation errors are being silently ignored or filtered out in certain cases, making it very difficult to debug configuration issues.

### Reproduction

Create a `docusaurus.config.js` with an invalid configuration that should trigger a validation error:

```js
module.exports = {
  title: 'My Site',
  url: 'https://example.com',
  baseUrl: '/',
  // Add some invalid config option
  invalidOption: 'this should error',
  // Or use an incorrect type for a valid option
  organizationName: 123, // should be string
};
```

Run the Docusaurus build or start command. Expected to see validation errors, but they don't appear or are incomplete.

### Expected behavior

All configuration validation errors should be displayed to help users identify what's wrong with their config. If there's a single validation error, it should be shown. If there are multiple errors, all of them should be listed.

### Additional context

This makes it really hard to figure out what's wrong with the configuration since the error messages that should guide you through fixing the issues are missing or incomplete.

---
Repository: /testbed
