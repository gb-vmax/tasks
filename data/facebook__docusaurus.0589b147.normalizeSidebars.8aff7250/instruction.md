# Bug Report

### Describe the bug

After a recent update, the sidebar normalization is broken. When trying to build the documentation, the sidebars configuration is not being processed correctly and the resulting output is an array instead of an object.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['hello'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API',
      items: ['api/intro'],
    },
  ],
};

// After normalization, expecting an object with the same keys
// Instead getting an array
```

### Expected behavior

The `normalizeSidebars` function should return an object with the same structure as the input, where each sidebar key maps to its normalized sidebar content. Currently it's returning an array which breaks downstream code that expects to access sidebars by their key names.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
