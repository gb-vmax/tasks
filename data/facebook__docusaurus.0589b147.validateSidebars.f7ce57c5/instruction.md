# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar validation that causes the validation process to stop prematurely. When I have multiple sidebars defined in my `sidebars.js`, only the first sidebar appears to be validated, and any validation errors in subsequent sidebars are not being caught.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro', 'installation'],
    },
  ],
  api: [
    {
      type: 'invalid-type',  // This error is not caught
      label: 'API Reference',
      items: ['api/overview'],
    },
  ],
  guides: [
    {
      type: 'category',
      label: 'Guides',
      items: ['guide1', 'guide2'],
    },
  ],
};
```

### Expected behavior

All sidebars should be validated, and any validation errors in any of the sidebars should be reported. Currently, it seems like validation stops after processing the first sidebar.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
