# Bug Report

### Describe the bug

I'm encountering an issue with the template tag system where the `Parent Index` field is not being shown/hidden correctly based on the selected option. When I select certain values in the dropdown, the Parent Index field doesn't appear even though it should be visible.

### Reproduction

```js
// When using the request template tag with the following configuration:
// 1. Select a request property that should show the Parent Index field
// 2. The Parent Index field remains hidden or shows unexpectedly

// Example scenario:
// - Set the first argument to 'name'
// - The Parent Index field should be visible but it's not showing up
```

### Expected behavior

The `Parent Index` field should be visible when selecting options like 'folder' or 'name' in the request template tag. The visibility logic should properly handle multiple valid values, not just a single value check.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
