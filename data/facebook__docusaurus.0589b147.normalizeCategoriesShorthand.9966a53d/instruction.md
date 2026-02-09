# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with sidebar categories when using the shorthand object notation. The category labels are being transformed in a way that breaks my sidebar structure - they're appearing lowercase and the order of categories is reversed from what I defined.

### Reproduction

```js
// sidebars.js
module.exports = {
  mySidebar: {
    'Getting Started': ['intro', 'installation'],
    'API Reference': ['api/overview', 'api/methods'],
    'Advanced Topics': ['advanced/performance', 'advanced/optimization']
  }
};
```

### Expected behavior

The sidebar categories should:
1. Display with the original label casing (e.g., "Getting Started", not "getting started")
2. Appear in the order they're defined in the configuration object

### Actual behavior

- Category labels are converted to lowercase ("getting started", "api reference", "advanced topics")
- The order of categories is reversed - "Advanced Topics" appears first, "Getting Started" appears last

This is breaking my documentation structure where I rely on proper capitalization for category names and a specific ordering for the user flow.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
