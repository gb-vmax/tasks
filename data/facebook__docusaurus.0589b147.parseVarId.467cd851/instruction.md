# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. It seems like `const` and `let` declarations are being treated the same as `var` declarations, which is causing scoping problems in my code.

### Reproduction

```js
// In an MDX file
export const MyComponent = () => {
  const x = 1;
  let y = 2;
  
  if (true) {
    const x = 3; // Should be block-scoped
    let y = 4;   // Should be block-scoped
    console.log(x, y); // Should print 3, 4
  }
  
  console.log(x, y); // Should print 1, 2 but behaves incorrectly
}
```

The parser seems to be treating block-scoped declarations (`const` and `let`) as if they have `var` semantics, which breaks proper lexical scoping.

### Expected behavior

- `const` and `let` should be block-scoped
- Redeclaring `const` or `let` in nested blocks should create new bindings
- Variable bindings should follow ES6+ scoping rules, not `var` hoisting behavior

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues with variable shadowing and block scoping in my MDX components. Any help would be appreciated!

---
Repository: /testbed
