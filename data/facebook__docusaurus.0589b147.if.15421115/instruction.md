# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category links where unlisted links are now being returned as the first category link. When a sidebar category item has `linkUnlisted: true`, it should be skipped when finding the first category link, but instead it's being returned.

### Reproduction

```js
const categoryItem = {
  type: 'category',
  label: 'My Category',
  href: '/docs/unlisted-page',
  linkUnlisted: true,
  items: [
    {
      type: 'link',
      label: 'Visible Page',
      href: '/docs/visible-page'
    }
  ]
}

const link = findFirstSidebarItemCategoryLink(categoryItem)
// Returns: '/docs/unlisted-page'
// Expected: Should skip the unlisted link and return '/docs/visible-page' from items
```

### Expected behavior

When `linkUnlisted` is set to `true` on a category item, the function should skip that category's `href` and look for the first link in the nested `items` instead. Unlisted links shouldn't be used as the first sidebar item link since they're meant to be hidden from navigation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
