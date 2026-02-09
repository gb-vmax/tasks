# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with unary expressions in the tree-shaking process. It seems like code that should be eliminated as having no side effects is being kept in the bundle, or vice versa - code that should be retained is being incorrectly removed.

### Reproduction

```js
// Example 1: void operator
const obj = {
  method() {
    console.log('side effect');
  }
};

void obj.method(); // This interaction behavior seems incorrect

// Example 2: other unary operators
const result = !someValue.property;
```

The bundler appears to be making incorrect assumptions about whether accessing properties on unary expression results has side effects or not. This affects tree-shaking decisions.

### Expected behavior

Unary expressions should correctly report whether property access on their results has side effects. The tree-shaker should:
- Keep code when property access might have side effects
- Remove code when it's safe to do so based on the unary operator type

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
