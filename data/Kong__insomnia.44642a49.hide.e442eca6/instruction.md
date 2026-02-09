# Bug Report

### Describe the bug

The JSONPath Filter option in the OS template tag is not appearing for several OS functions that return objects. Currently it only shows up for `userInfo` and `cpus`, but there are many other OS functions like `networkInterfaces`, `totalmem`, `freemem`, etc. that also return objects and would benefit from JSONPath filtering.

### Reproduction

1. Create a new request with a template tag
2. Select the OS template tag
3. Choose a function like `networkInterfaces` or `freemem` from the dropdown
4. Notice that the JSONPath Filter field doesn't appear, even though these functions return objects that could be filtered

### Expected behavior

The JSONPath Filter field should be visible for all OS functions that return objects, not just `userInfo` and `cpus`. Functions like `networkInterfaces`, `totalmem`, `freemem`, `homedir`, `tmpdir`, `endianness`, `loadavg`, `uptime`, `type`, `version`, and `machine` all return objects or structured data that would be useful to filter with JSONPath.

### Additional context

This makes it difficult to extract specific values from these OS functions without the JSONPath filtering capability. For example, if I want to get a specific network interface's address from `networkInterfaces`, I currently can't do that easily.

---
Repository: /testbed
