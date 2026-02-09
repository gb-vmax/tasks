# Bug Report

### Describe the bug

I'm experiencing an issue with `this` binding in arrow functions within MDX files. When using `this` inside arrow functions, it seems to be incorrectly scoped and doesn't behave as expected according to JavaScript semantics.

Arrow functions should inherit `this` from their enclosing scope, but it appears the parser is treating them differently, causing unexpected behavior at runtime.

### Reproduction

```jsx
class MyComponent {
  constructor() {
    this.value = 42;
  }
  
  render() {
    const arrowFunc = () => {
      console.log(this.value); // Should print 42
    };
    arrowFunc();
  }
}
```

When this code is processed through the MDX parser, the `this` context inside the arrow function doesn't resolve correctly.

### Expected behavior

Arrow functions should maintain the `this` binding from their parent scope. The code above should successfully access `this.value` and print `42`.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a regression as similar code was working in previous versions. Any help would be appreciated!

---
Repository: /testbed
