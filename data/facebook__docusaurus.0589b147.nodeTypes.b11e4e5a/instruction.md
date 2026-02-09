# Bug Report

### Describe the bug

I'm experiencing an issue where `nodeTypes` from `@mdx-js/mdx` is returning an incomplete object. It appears that the first node type is missing from the returned object, which is causing problems when trying to iterate over or access all available node types.

### Reproduction

```js
import { nodeTypes } from '@mdx-js/mdx'

// First call
const types1 = nodeTypes
console.log(Object.keys(types1)) // Missing the first node type

// Subsequent calls
const types2 = nodeTypes
console.log(Object.keys(types2)) // Missing even more node types
```

Each time `nodeTypes` is accessed, it seems like another node type disappears from the object. This is breaking code that depends on having access to the complete set of node types.

### Expected behavior

`nodeTypes` should return a consistent, complete object containing all available node types on every access. The object should not be mutated between calls.

### Additional context

This is affecting any code that needs to reference the full list of MDX node types, particularly when building custom plugins or transformers that need to handle different node types dynamically.

---
Repository: /testbed
