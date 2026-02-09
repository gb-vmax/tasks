# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where custom properties (`hName`, `hProperties`, `hChildren`) from the data object are not being applied correctly to nodes. It seems like the logic for handling these special properties has broken, particularly when dealing with `hChildren` overrides.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdx = `
# Hello

Some content
`

const result = await compile(mdx, {
  // ... options
})

// When trying to override children with hChildren
// The children are not being replaced as expected
```

When I set `hChildren` on a node's data object to override its children, the original children remain instead of being replaced. Additionally, there seems to be confusion about whether a node has children or not - sometimes the logic treats nodes with children as if they don't have any, and vice versa.

### Expected behavior

- When `hChildren` is set in the data object, it should replace the node's children
- The logic should correctly determine if a node has children before attempting to wrap it
- Nodes should be properly transformed based on their `hName` and `hProperties` values

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have regressed recently as I didn't see this behavior in earlier versions. The transformed output is now incorrect when using these data properties.

---
Repository: /testbed
