# Bug Report

### Describe the bug

When using template variables with arrays, the first element is being skipped and array indices appear to be off by one. This causes incorrect template rendering when trying to access array elements.

### Reproduction

```js
const data = {
  items: ['first', 'second', 'third']
};

// Expected: Should access all elements starting from index 0
// Actual: First element is skipped, and indices are shifted
```

When templating tries to process an array, it starts from index 1 instead of 0, which means:
- The first element (index 0) is never processed
- All subsequent elements are accessed with wrong indices (off by one)

### Expected behavior

Template rendering should process all array elements starting from index 0, with correct index values for each element.

### System Info
- Package: @insomnia/insomnia
- Module: templating/utils

---
Repository: /testbed
