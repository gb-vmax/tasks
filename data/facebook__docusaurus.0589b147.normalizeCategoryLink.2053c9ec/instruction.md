# Bug Report

### Describe the bug

I'm experiencing an issue with category links in the sidebar. When I have a category with a `link` property of type `doc`, the link doesn't work as expected - it seems to be getting filtered out incorrectly.

Additionally, the generated slugs for categories with `generated-index` links are not using the category label anymore. Instead, they appear to be using some other value which results in incorrect URLs.

### Reproduction

```js
// Sidebar configuration
{
  type: 'category',
  label: 'My Category',
  link: {
    type: 'doc',
    id: 'some-doc-id'
  },
  items: [...]
}
```

When using this configuration, the category link disappears even when the document exists and is not a draft.

For generated-index links:
```js
{
  type: 'category',
  label: 'API Reference',
  link: {
    type: 'generated-index'
  },
  items: [...]
}
```

The expected URL should be `/category/api-reference` but it's generating something different based on the version path instead of the category label.

### Expected behavior

- Category links with `type: 'doc'` should only be filtered out when the referenced document is actually a draft
- Generated index slugs should be based on the category label (e.g., `/category/api-reference` for a category labeled "API Reference")

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
