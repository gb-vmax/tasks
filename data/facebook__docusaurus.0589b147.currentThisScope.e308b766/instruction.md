# Bug Report

### Describe the bug

I'm experiencing an issue with scope handling in the MDX parser. When using `this` keyword inside arrow functions in MDX files, the scope resolution seems to be incorrect. The parser appears to be returning the wrong scope context, which causes `this` to bind to unexpected values.

### Reproduction

```jsx
class MyComponent {
  constructor() {
    this.value = 42;
  }
  
  render() {
    const arrow = () => {
      console.log(this.value); // this is not binding correctly
    };
    arrow();
  }
}
```

When this code is parsed in an MDX file, the `this` context inside the arrow function doesn't resolve properly. It seems like the scope stack traversal is starting from the wrong position or using incorrect flag checks.

### Expected behavior

Arrow functions should properly inherit the `this` context from their enclosing scope. The `this` keyword inside arrow functions should refer to the same context as the surrounding code.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently, possibly related to scope stack handling changes. Any help would be appreciated!

---
Repository: /testbed
