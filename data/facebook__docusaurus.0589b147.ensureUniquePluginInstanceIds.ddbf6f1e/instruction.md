# Bug Report

### Describe the bug

I'm experiencing an issue with plugin instance validation where multiple plugins with different names but the same ID are not being detected as conflicts. The validation logic seems to be grouping plugins incorrectly, which allows duplicate plugin IDs to slip through without raising an error.

### Reproduction

```js
const plugins = [
  {
    name: 'plugin-a',
    options: { id: 'my-id' }
  },
  {
    name: 'plugin-b',
    options: { id: 'my-id' }
  }
];

// These plugins have the same ID but different names
// Expected: Error should be thrown
// Actual: No error is raised
```

### Expected behavior

When multiple plugins are configured with the same ID (regardless of their names), the system should throw an error indicating a duplicate plugin ID conflict. Currently, it only seems to validate uniqueness within plugins of the same name, which allows different plugins to share IDs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
