# Bug Report

### Describe the bug

Plugin warnings with URLs are not displaying correctly in the CLI output. When multiple warnings from the same plugin have different URLs, only the first URL is shown and subsequent URLs are being skipped.

### Reproduction

```js
// Create a plugin that generates warnings with different URLs
const plugin = {
  name: 'test-plugin',
  buildStart() {
    this.warn({
      message: 'Warning message',
      url: 'https://example.com/warning1'
    });
    this.warn({
      message: 'Warning message',
      url: 'https://example.com/warning2'
    });
  }
};
```

When running rollup with this plugin, the second URL (`https://example.com/warning2`) is not displayed in the console output even though both warnings have the same message but different documentation links.

### Expected behavior

Each warning should display its associated URL if it differs from the previous warning's URL. Users should be able to see all relevant documentation links for their warnings.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
