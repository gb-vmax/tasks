# Bug Report

### Describe the bug

I'm experiencing an issue with MDX extension merging where arrays and objects aren't being combined correctly. When multiple extensions are used together, the properties from earlier extensions seem to be overriding later ones instead of being properly merged.

### Reproduction

```js
const extension1 = {
  canContainEols: ['element1'],
  transforms: [transform1],
  enter: { node1: handler1 }
}

const extension2 = {
  canContainEols: ['element2'],
  transforms: [transform2],
  enter: { node2: handler2 }
}

// After combining extensions
const combined = combineExtensions([extension1, extension2])

// Expected: combined.canContainEols should be ['element1', 'element2']
// Actual: combined.canContainEols contains nested arrays

// Expected: combined.enter should have both node1 and node2 handlers
// Actual: only handlers from extension2 are present
```

### Expected behavior

When combining multiple extensions:
- Arrays like `canContainEols` and `transforms` should flatten and merge all items from both extensions
- Objects like `enter` and `exit` should merge properties from both extensions, with later extensions taking precedence only for duplicate keys

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
