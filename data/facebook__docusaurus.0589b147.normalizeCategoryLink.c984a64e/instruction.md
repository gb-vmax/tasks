# Bug Report

### Describe the bug

When configuring a sidebar category with a `generated-index` link type, the slug is not being properly applied. Instead of using the provided slug from the configuration, it appears to be ignored and the category link doesn't work as expected.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'My Category',
      link: {
        type: 'generated-index',
        slug: '/custom-category-slug'
      },
      items: ['doc1', 'doc2']
    }
  ]
}
```

When navigating to the category, the custom slug doesn't seem to be respected. The link generation for categories with generated-index type seems broken.

### Expected behavior

The category link should use the custom slug provided in the configuration (`/custom-category-slug` in this example). The permalink should be generated correctly based on the provided slug value.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
