# Bug Report

### Describe the bug

I'm encountering an issue when importing data that contains keys with dots in them. The validation seems to be too strict now - it's rejecting keys that have dots anywhere in the middle, but it's allowing keys that start with a dot, which doesn't make sense.

### Reproduction

When trying to import an object with keys containing dots:

```js
const data = {
  "user.name": "John",
  "settings.theme": "dark"
}
```

The import fails with an error about invalid keys, even though these keys should be valid (dots in the middle are commonly used in configuration objects).

However, if I try to import:

```js
const data = {
  ".hidden": "value"
}
```

This goes through without any validation error, even though keys starting with dots are typically more problematic.

### Expected behavior

The validation should catch keys that actually cause issues with the database (like keys starting with dots), but allow keys with dots in the middle since those are commonly used in imported data from other tools.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
