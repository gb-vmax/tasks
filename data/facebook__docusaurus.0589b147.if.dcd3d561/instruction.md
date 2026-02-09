# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category links in the docs theme. When a sidebar category item has `linkUnlisted: true` set, the `findFirstSidebarItemCategoryLink` function is returning the category's `href` even though it should be skipping unlisted links.

### Reproduction

```js
const categoryItem = {
  type: 'category',
  label: 'Getting Started',
  href: '/docs/intro',
  linkUnlisted: true,
  items: [
    {
      type: 'link',
      href: '/docs/installation',
      label: 'Installation'
    }
  ]
}

const link = findFirstSidebarItemCategoryLink(categoryItem)
// Returns '/docs/intro' but should return '/docs/installation' instead
// because the category link is marked as unlisted
```

### Expected behavior

When `linkUnlisted` is set to `true`, the function should skip the category's own `href` and look for the first valid link in the child items instead. The current behavior incorrectly returns the unlisted link.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
