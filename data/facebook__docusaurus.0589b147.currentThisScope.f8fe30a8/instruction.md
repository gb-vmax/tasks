# Bug Report

### Describe the bug

I'm encountering an issue with arrow function scope handling in MDX parsing. When using arrow functions with `this` keyword, the scope resolution seems to be incorrect, causing `this` to reference the wrong scope or potentially leading to infinite loops in scope traversal.

### Reproduction

```jsx
const MyComponent = () => {
  const handler = () => {
    console.log(this.value);
  };
  
  return <div onClick={handler}>Click me</div>;
};
```

When parsing MDX content that includes arrow functions referencing `this`, the parser doesn't correctly identify the appropriate scope. This can lead to:
1. Incorrect scope resolution for `this` keyword
2. Potential infinite loops when traversing the scope stack
3. Unexpected behavior in nested arrow functions

### Expected behavior

The parser should correctly identify and skip arrow function scopes when looking for the appropriate `this` scope, since arrow functions don't have their own `this` binding. The scope stack traversal should start from the correct position and properly check scope flags.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be a regression in the scope resolution logic. Any arrow function that references `this` is affected by this issue.

---
Repository: /testbed
