# Bug Report

### Describe the bug

I'm encountering an issue with MDX element transformations when using `hName` with non-element nodes. When a non-element result (like a text node) is transformed into an element using the `hName` property, the children array is not being constructed correctly.

### Reproduction

```js
const from = {
  type: 'text',
  value: 'Hello',
  data: {
    hName: 'span'
  }
}

const to = {
  type: 'text',
  value: 'Hello'
}

// After applying data transformation
// Expected: result.children should be an array containing the original node
// Actual: result.children is set to the node itself (not wrapped in an array)
```

When transforming a non-element node to an element using `hName`, the children property ends up being assigned the raw result object instead of wrapping it in an array. This causes issues downstream when the code expects `children` to always be an array.

### Expected behavior

When a non-element node is transformed into an element via `hName`, the original node should be wrapped in an array and assigned to the `children` property. The resulting element structure should have a properly formatted children array.

### Additional context

This seems to affect text nodes and other non-element nodes that get transformed into elements through the data transformation process. The issue appears to be in how the children are being extracted and assigned during the transformation.

---
Repository: /testbed
