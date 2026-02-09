# Bug Report

### Describe the bug

Deprecation warnings are not being logged when `activeDeprecation` is true but `strictDeprecations` is false. It seems like the warning system is only working when both flags are enabled together.

### Reproduction

```js
// Set up with activeDeprecation enabled but strictDeprecations disabled
const options = {
  activeDeprecation: true,
  strictDeprecations: false
};

// Try to trigger a deprecation warning
warnDeprecationWithOptions(
  deprecation,
  urlSnippet,
  options.strictDeprecations,
  plugin
);

// Expected: Warning should be logged
// Actual: Nothing happens, no warning is shown
```

### Expected behavior

Deprecation warnings should be logged whenever `activeDeprecation` is true, regardless of the `strictDeprecations` setting. The `strictDeprecations` flag should only control whether the warning is treated as an error or just a warning.

### System Info
- Version: Latest from main branch

---
Repository: /testbed
