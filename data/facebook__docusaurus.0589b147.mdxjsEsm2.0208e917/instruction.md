# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where accessing nested properties on the `node2` object causes errors. When processing MDX ESM nodes, the code tries to access `node2.estree.comments` but it should be accessing `estree.comments` instead.

### Reproduction

```js
// When parsing an MDX file with ESM imports
const mdxContent = `
import { Component } from './component'

# Hello World
`

// The parser fails when trying to process the import statement
// Error occurs in mdxjsEsm2 handler when accessing node2.estree.comments
```

### Expected behavior

The MDX parser should correctly extract comments and ESM body from the estree data structure without errors. The comments should be retrieved from the `estree` variable (which is already extracted from `node2.data.estree`), not from `node2.estree` directly.

### Additional context

This seems to be related to how the estree data is being accessed in the mdxjsEsm2 handler. The variable `estree` is already defined from `node2.data && node2.data.estree`, so subsequent accesses should use that variable rather than going back to the node object.

---
Repository: /testbed
