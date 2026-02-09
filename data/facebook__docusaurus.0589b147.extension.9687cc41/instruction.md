# Bug Report

### Describe the bug

I'm experiencing an issue with MDX extension merging where multiple extensions aren't being combined correctly. When I register multiple extensions that define handlers or transforms, only the last extension's configuration seems to be applied, and the earlier ones are completely ignored.

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

// After combining these extensions, only extension2's values are present
// extension1's canContainEols and transforms are lost
const combined = combineExtensions([extension1, extension2])
```

### Expected behavior

When combining multiple extensions, all `canContainEols` entries should be merged together into a single array, all `transforms` should be accumulated, and all `enter`/`exit` handlers should be combined into a single object with all handlers available.

Currently it seems like the second extension is completely replacing the first one's configuration instead of merging with it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
