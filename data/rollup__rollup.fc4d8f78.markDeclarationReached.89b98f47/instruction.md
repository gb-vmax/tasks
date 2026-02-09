# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments in object patterns. When using destructuring with nested properties, the declaration tracking seems to be broken and causes unexpected behavior during the bundling process.

### Reproduction

```js
const obj = {
  prop: {
    nested: 'value'
  }
};

// Destructuring with property shorthand
const { prop } = obj;

// This should work but causes issues
function test({ prop: renamed }) {
  return renamed;
}
```

The problem appears when the bundler tries to track which declarations have been reached. It seems like the wrong node is being marked as reached, which can lead to incorrect tree-shaking or scope analysis.

### Expected behavior

Destructuring assignments should be properly tracked and the correct declaration nodes should be marked as reached. The bundler should correctly identify which variables are in scope and handle property destructuring without issues.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how property nodes handle their value nodes during the declaration phase. Any help would be appreciated!

---
Repository: /testbed
