# Bug Report

### Describe the bug

I'm experiencing an issue where certain warnings are not being displayed immediately during the build process. It seems like warnings that should be shown right away are being deferred or not shown at all.

### Reproduction

When running a build that generates warnings, some warnings that should appear immediately are not being displayed. For example:

```js
// Build configuration that should trigger immediate warnings
rollup({
  // ... config that generates warnings with specific codes
})
```

Expected: Warnings should be displayed immediately according to their handler type
Actual: Some warnings are not showing up or are being handled incorrectly

### Expected behavior

Warnings should be categorized and displayed correctly:
- Immediate warnings should be shown right away
- Deferred warnings should be batched and shown later
- All warnings should be counted and tracked properly

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
