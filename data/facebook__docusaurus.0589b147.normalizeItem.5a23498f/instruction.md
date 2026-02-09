# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar item normalization in the docs plugin. When building the sidebar, certain item types are not being converted properly, which causes the sidebar structure to break.

### Reproduction

```js
const sidebar = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        { type: 'doc', id: 'intro' },
        { type: 'ref', id: 'tutorial' }
      ]
    },
    {
      type: 'link',
      label: 'External',
      href: 'https://example.com'
    }
  ]
};
```

When the sidebar is processed, the category and doc items remain unconverted instead of being transformed into the normalized prop format. This results in the sidebar not rendering correctly in the UI.

### Expected behavior

All sidebar items should be properly normalized according to their type:
- `category` items should be converted using `convertCategory()`
- `doc` and `ref` items should be converted using `convertDocLink()`
- `link` items should pass through as-is

The sidebar should render with all items properly formatted and accessible.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
