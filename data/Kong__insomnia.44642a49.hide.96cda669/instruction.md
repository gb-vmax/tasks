# Bug Report

### Describe the bug

The JSONPath Filter option in the OS template tag is not appearing for `networkInterfaces` even though it returns a complex object that would benefit from JSONPath filtering. Currently only `userInfo` and `cpus` show the filter option, but `networkInterfaces` also returns an object structure that should be filterable.

### Reproduction

```js
// Using the OS template tag with networkInterfaces function
{% os 'networkInterfaces' %}
```

When selecting `networkInterfaces` as the function, the JSONPath Filter field doesn't appear in the UI, making it impossible to extract specific values from the returned network interface objects.

### Expected behavior

The JSONPath Filter option should be visible when using `networkInterfaces` (similar to how it works for `userInfo` and `cpus`) since it returns a complex object structure. This would allow users to query specific network interface properties like IP addresses, MAC addresses, etc.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
