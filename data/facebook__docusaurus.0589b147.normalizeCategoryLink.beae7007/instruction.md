# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category links in Docusaurus. When a category has a `link` property pointing to a doc, the link disappears/becomes undefined even when the doc is NOT a draft. It seems like the logic is inverted - published docs are being treated as drafts and vice versa.

### Reproduction

```js
// In sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      link: {
        type: 'doc',
        id: 'intro'  // This is a published doc, not a draft
      },
      items: ['tutorial-basics/create-a-page']
    }
  ]
};
```

### Expected behavior

The category link should work correctly and point to the `intro` doc. Instead, the link becomes undefined and the category is not clickable, even though the doc exists and is published.

This seems to be affecting all category links that reference published documents. Draft documents might be working when they shouldn't be.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
