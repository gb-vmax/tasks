# Bug Report

### Describe the bug
After a recent update, the `EXIT` constant from `unist-util-visit` is not working as expected. When trying to use `EXIT` to stop tree traversal, I'm getting an object instead of the expected constant value.

### Reproduction
```js
import { visit, EXIT } from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' }
  ]
}

visit(tree, 'paragraph', (node) => {
  console.log(EXIT) // Expected: Symbol or constant, Got: { value: ... }
  return EXIT
})
```

### Expected behavior
`EXIT` should be a simple constant/symbol that can be returned directly to stop tree traversal, similar to how `CONTINUE` and `SKIP` work. Currently it appears to be wrapped in an object or transformed in some way.

### System Info
- Package: unist-util-visit@5.0.0
- Node version: 18.x

---
Repository: /testbed
