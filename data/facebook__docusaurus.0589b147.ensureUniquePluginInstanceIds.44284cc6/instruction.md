# Bug Report

### Describe the bug

When using multiple instances of the same plugin with different IDs, Docusaurus throws an error about duplicate plugin instances even though each instance has a unique ID configured.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs-1',
        // ... other options
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs-2',
        // ... other options
      },
    ],
  ],
};
```

### Expected behavior

Multiple plugin instances with different IDs should be allowed and work correctly. The validation should check for duplicate IDs, not just group by plugin name.

### Additional context

This seems to have broken recently. Previously I could run multiple instances of the same plugin as long as they had different IDs specified in the options.

---
Repository: /testbed
