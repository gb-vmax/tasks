# Bug Report

### Describe the bug

I'm experiencing an issue with category links in the sidebar configuration. When I set a custom `slug` for a category with a `generated-index` link type, the custom slug is being ignored and replaced with the default auto-generated slug instead.

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
        slug: '/my-custom-slug'  // This gets ignored
      },
      items: [
        'doc1',
        'doc2'
      ]
    }
  ]
}
```

### Expected behavior

When I specify a custom `slug` in the category link configuration, it should use that slug for the permalink instead of always generating one based on the category label. The category page should be accessible at `/docs/my-custom-slug` instead of `/docs/category/my-category`.

### Additional context

This seems to have broken recently. The custom slug configuration used to work properly, but now it's always using the auto-generated slug pattern regardless of what I specify in the configuration.

---
Repository: /testbed
