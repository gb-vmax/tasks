# Bug Report

### Describe the bug

When running rollup with the `--silent` flag, the warning count still increments even though warnings are supposed to be suppressed. This causes incorrect warning statistics to be reported.

### Reproduction

```js
// Run rollup with --silent flag
rollup --silent -c

// Check warning count - it shows warnings were counted
// even though none were displayed
```

The issue is that warnings are being counted before checking if silent mode is enabled, so the counter increments regardless of whether warnings are actually processed or displayed.

### Expected behavior

When `--silent` is enabled, warnings should not be counted at all since they're being suppressed. The warning count should remain at 0 when silent mode is active.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
