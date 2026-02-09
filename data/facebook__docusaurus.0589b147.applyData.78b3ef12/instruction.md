# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where element properties and children are not being applied correctly from data attributes. It seems like the logic for handling `hName` and `hChildren` from the data object is inverted or broken.

### Reproduction

When processing MDX content with custom data attributes:

```js
const node = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: ['original content'],
  data: {
    hName: 'span',
    hChildren: ['new content']
  }
}

// After processing with applyData:
// - hName is not applied when result.type === 'element'
// - hChildren replaces children only when it's null/undefined instead of when it has a value
```

### Expected behavior

- When `hName` is provided and the result type is `element`, the `tagName` should be updated to `hName`
- When `hChildren` is provided (not null/undefined), it should replace the existing children array

### Current behavior

The opposite seems to be happening - the conditions appear to be inverted, causing:
1. Tag names not being applied to elements
2. Children being replaced with null/undefined values instead of actual content

This is breaking MDX component transformations that rely on these data attributes.

---
Repository: /testbed
