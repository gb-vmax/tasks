# Bug Report

### Describe the bug

I'm encountering an issue with sidebar categories in Docusaurus. When a category has exactly one item, it's being incorrectly filtered out or converted to a link, even when it should remain as a collapsible category.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'intro', // Only one item
      ],
    },
  ],
};
```

After building the docs, the "Getting Started" category either disappears entirely or gets converted to a direct link instead of showing as a proper category with one item inside.

### Expected behavior

A category with a single item should still render as a category (collapsible or not, depending on configuration). The single item should be visible within that category structure.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Categories with 2+ items work fine, but single-item categories are affected.

---
Repository: /testbed
