# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in MDX nodes. When working with AST nodes that have position information, the `end` property is missing from the returned position object, even when the node has valid end position data.

### Reproduction

```js
const node = {
  type: 'element',
  position: {
    start: { line: 1, column: 1, offset: 0 },
    end: { line: 1, column: 10, offset: 9 }
  }
}

const pos = position2(node)
console.log(pos)
// Expected: { start: {...}, end: {...} }
// Actual: { start: {...} }
// The end property is missing!
```

### Expected behavior

When a node has both start and end position information, the returned position object should include both properties. This is breaking position-based operations that rely on having complete range information.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
