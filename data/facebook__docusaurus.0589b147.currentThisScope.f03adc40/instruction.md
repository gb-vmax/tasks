# Bug Report

### Describe the bug

I'm experiencing issues with `this` binding in arrow functions when parsing MDX files. It seems like the scope resolution is not working correctly - arrow functions are incorrectly inheriting `this` context when they shouldn't be, or the parser is getting confused about which scope to use.

### Reproduction

```js
class MyComponent {
  constructor() {
    this.value = 'test';
  }
  
  render() {
    const arrowFn = () => {
      // this should refer to MyComponent instance
      console.log(this.value);
    };
    arrowFn();
  }
}
```

When this code is processed through the MDX parser, the `this` context appears to be resolved incorrectly. The behavior suggests that the scope traversal logic might be starting at the wrong index or checking the wrong scope flags.

### Expected behavior

Arrow functions should properly inherit `this` from their enclosing lexical scope, and the parser should correctly identify which scope contains the appropriate `this` binding.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be related to how the scope stack is being traversed when determining the current `this` scope. The issue manifests when using arrow functions in class methods or other contexts where `this` binding matters.

---
Repository: /testbed
