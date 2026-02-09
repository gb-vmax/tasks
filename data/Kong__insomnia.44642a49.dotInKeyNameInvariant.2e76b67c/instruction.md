# Bug Report

### Describe the bug
When importing data with keys that contain dots (.), the validation is incorrectly rejecting valid keys. The importer is now only checking if keys start with a dot instead of checking if they contain a dot anywhere in the key name.

### Reproduction
```js
// This should be rejected but isn't
const data = {
  "my.invalid.key": "value"
}

// Try importing this data - it will be accepted even though the key contains dots
```

### Expected behavior
The importer should reject any keys that contain a dot (`.`) character anywhere in the key name, not just keys that start with a dot. Keys like `"my.invalid.key"` or `"test.value"` should trigger the validation error.

Currently, only keys starting with a dot like `".startswithDot"` are being caught, while keys with dots in the middle like `"has.dot.inside"` pass through validation and may cause issues with nedb.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
