# Bug Report

### Describe the bug

The JSONPath Filter option is not appearing for the `networkInterfaces` OS function in the template tag editor. When selecting `networkInterfaces` as the OS function, the JSONPath Filter field that should allow filtering complex object results is hidden/unavailable.

### Reproduction

1. Open a template tag with the OS plugin
2. Select `networkInterfaces` from the function dropdown
3. Notice that the JSONPath Filter option is not displayed

The JSONPath Filter currently only shows up for `userInfo` and `cpus` functions, but `networkInterfaces` also returns complex objects that need filtering capabilities.

### Expected behavior

The JSONPath Filter field should be visible and available when using the `networkInterfaces` function, similar to how it works with `userInfo` and `cpus` since all three return complex objects that benefit from JSONPath querying.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
