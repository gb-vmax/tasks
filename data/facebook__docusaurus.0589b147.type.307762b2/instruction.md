# Bug Report

### Describe the bug

I'm experiencing an issue with MDX node type checking where the type factory appears to be returning inverted results. When checking if a node matches a specific type, it's returning `true` for nodes that don't match and `false` for nodes that do match.

### Reproduction

```js
const check = typeFactory('paragraph');

const paragraphNode = {
  type: 'paragraph',
  children: []
};

const headingNode = {
  type: 'heading',
  children: []
};

// This returns false when it should return true
console.log(check(paragraphNode)); // Expected: true, Got: false

// This returns true when it should return false  
console.log(check(headingNode)); // Expected: false, Got: true
```

### Expected behavior

The type factory should return `true` when a node's type matches the check parameter, and `false` when it doesn't match.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
