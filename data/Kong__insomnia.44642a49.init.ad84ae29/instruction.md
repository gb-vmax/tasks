# Bug Report

### Describe the bug

After a recent update, I'm seeing issues with response initialization in Insomnia. When creating a new response object, the `bytesRead` property is being set to `-1` instead of `0`, which breaks some of my workflows that depend on this value.

Additionally, the `bodyCompression` field is now `null` instead of the expected `'__NEEDS_MIGRATION__'` string, which is causing problems when trying to handle legacy response bodies.

### Reproduction

```js
const response = init();

console.log(response.bytesRead);
// Expected: 0
// Actual: -1

console.log(response.bodyCompression);
// Expected: '__NEEDS_MIGRATION__'
// Actual: null
```

### Expected behavior

- `bytesRead` should initialize to `0` for new responses (not `-1`)
- `bodyCompression` should initialize to `'__NEEDS_MIGRATION__'` to properly handle legacy body migration

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might have been an accidental change? The `-1` value for `bytesRead` doesn't make sense for a fresh response, and the `null` value breaks the legacy migration logic.

---
Repository: /testbed
