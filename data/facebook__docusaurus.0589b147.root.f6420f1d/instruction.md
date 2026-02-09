# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown to HTML transformation where the root node structure appears to be processed incorrectly. The `wrap` function seems to be called with the wrong arguments, which is causing the transformation pipeline to fail or produce unexpected results.

### Reproduction

```js
// When transforming a markdown AST to HAST
const mdast = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello world' }]
    }
  ]
}

// The root handler processes this incorrectly
// Expected: wrap should receive the children array
// Actual: wrap is being called on the result object instead
```

### Expected behavior

The `state.wrap()` function should be called with the children array (result of `state.all(node)`), not with the result object itself. The wrapped children should then be assigned to the result's children property.

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest

This seems to have broken the normal transformation flow. The order of operations appears to be incorrect - `wrap` should wrap the children before they're assigned to the result object, and `patch` should be called before `applyData`.

---
Repository: /testbed
