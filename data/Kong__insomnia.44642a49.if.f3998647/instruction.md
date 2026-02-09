# Bug Report

### Describe the bug
When using localStorage with keys containing path separators or special characters, the application crashes or fails to properly store/retrieve values. The storage system doesn't handle nested key structures or sanitize invalid filesystem characters.

### Reproduction
```js
// Using a key with path separators
localStorage.getItem('user/settings/theme', { theme: 'dark' });

// Or keys with special characters
localStorage.getItem('config:app|data', { value: 'test' });
```

The application fails to create the necessary directory structure for nested keys, and special characters in keys can cause filesystem errors on different operating systems.

### Expected behavior
The localStorage implementation should:
1. Properly handle keys with path separators by creating nested directory structures
2. Sanitize keys to remove or replace invalid filesystem characters
3. Gracefully handle edge cases like empty segments, `.` and `..` in paths

### System Info
- Insomnia version: latest
- OS: Cross-platform issue (Windows/macOS/Linux)

---
Repository: /testbed
