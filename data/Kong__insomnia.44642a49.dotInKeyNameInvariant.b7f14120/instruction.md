# Bug Report

### Describe the bug

When importing data with nested objects, valid keys without dots are being rejected with an error message saying they contain '.'. The validation logic appears to be inverted - it's throwing errors for keys that should be valid instead of keys that actually contain dots.

### Reproduction

```js
// This should work but throws an error
const validData = {
  name: 'test',
  settings: {
    timeout: 5000,
    retries: 3
  }
}

// Error: Detected invalid key "name", which contains '.'. Please update it in the original tool and re-import it.
```

### Expected behavior

Keys without dots should pass validation and import successfully. Only keys that actually contain '.' characters should be rejected with the error message.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
