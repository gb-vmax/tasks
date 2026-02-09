# Bug Report

### Describe the bug

I'm experiencing an issue with nested extension configurations in remark. When passing extensions that have their own `extensions` property (nested extensions), the configuration isn't being applied correctly. It seems like the extensions are being processed but the final configuration is not what I expected.

### Reproduction

```js
const processor = remark().use({
  extensions: [
    { /* base config */ },
    { /* additional config */ }
  ]
});

// The nested extensions don't seem to be configured properly
// Base configuration appears to be overridden or lost
```

### Expected behavior

When using nested extensions (extensions that contain an `extensions` array), each extension should be properly merged into the base configuration. The base settings should be preserved and extended by the nested extensions, not replaced.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
