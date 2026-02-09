# Bug Report

### Describe the bug

I'm experiencing an issue with unary expressions where the tree-shaking behavior seems incorrect. Properties accessed on unary expressions are being removed during the build even though they should be preserved.

### Reproduction

```js
const obj = {
  value: 42,
  getValue() {
    return this.value;
  }
};

// Accessing properties on void expression
const result = (void 0, obj).getValue();

// The getValue method call is incorrectly being tree-shaken
console.log(result);
```

When bundling this code, the method call gets removed as if it has no side effects, but it should be preserved since we're accessing a property on the result of the unary expression.

### Expected behavior

Property accesses on unary expressions should be treated as having potential side effects and not be removed during tree-shaking optimization. The bundled output should maintain the property access behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
