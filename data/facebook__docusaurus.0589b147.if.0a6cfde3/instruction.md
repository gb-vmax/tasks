# Bug Report

### Describe the bug

When navigating through sidebar categories with nested items, the first link in a category is not being resolved correctly. Categories that should show their `href` property as the first link are not returning it, and instead the function seems to be looking through nested items even when a direct `href` is available.

### Reproduction

```js
const category = {
  type: 'category',
  label: 'Getting Started',
  href: '/docs/intro',
  linkUnlisted: false,
  items: [
    { type: 'doc', id: 'intro' },
    { type: 'doc', id: 'tutorial' }
  ]
}

// Expected to return '/docs/intro' but returns undefined or wrong link
const firstLink = findFirstSidebarItemCategoryLink(category);
```

### Expected behavior

When a sidebar category has an `href` property and `linkUnlisted` is false, the function should return that `href` as the first link. The category's own link should take precedence before searching through nested items.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
