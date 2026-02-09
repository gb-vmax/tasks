# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where `this` keyword is not being resolved correctly in certain scope contexts. The parser seems to be returning the wrong scope when checking for `this` bindings, which causes unexpected behavior in arrow functions and regular functions.

### Reproduction

```jsx
const Component = () => {
  function regularFunction() {
    console.log(this); // Should have proper scope
  }
  
  const arrowFunction = () => {
    console.log(this); // Should inherit from parent scope
  }
}
```

When parsing MDX files with nested function scopes, the `this` keyword doesn't resolve to the expected scope. This appears to affect how the parser handles the scope stack traversal.

### Expected behavior

The parser should correctly identify the appropriate scope for `this` keyword based on whether it's inside an arrow function or a regular function. Arrow functions should inherit `this` from their parent scope, while regular functions should have their own `this` binding.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
