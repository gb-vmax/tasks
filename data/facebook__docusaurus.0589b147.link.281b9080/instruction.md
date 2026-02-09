# Bug Report

### Describe the bug

I'm experiencing an issue where link nodes in MDX are not being processed correctly. When rendering markdown links with data attributes or custom properties, the data doesn't seem to be applied to the resulting element properly.

### Reproduction

```js
// Create a link node with custom data
const linkNode = {
  type: 'link',
  url: 'https://example.com',
  title: 'Example',
  data: {
    hProperties: {
      className: 'custom-link'
    }
  },
  children: [{ type: 'text', value: 'Click here' }]
}

// Process the link
const result = link(state, linkNode)

// Expected: result should have the custom properties from data
// Actual: custom properties are not applied correctly
```

### Expected behavior

When a link node has custom data (like `hProperties`), those properties should be correctly merged into the resulting HTML element. The `applyData` function should receive the correct arguments to properly apply the data attributes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently and is affecting links that need custom styling or attributes applied through the data property.

---
Repository: /testbed
