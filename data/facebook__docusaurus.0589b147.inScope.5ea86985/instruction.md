# Bug Report

### Describe the bug

I'm experiencing an issue with variable scoping in MDX compilation. Variables that are clearly defined in the current scope are being treated as if they're not in scope, while variables that shouldn't be in scope are being treated as if they are.

This seems to be causing incorrect behavior when MDX tries to determine whether identifiers are in scope or not.

### Reproduction

```jsx
function MyComponent() {
  const localVar = 'test';
  
  return (
    <div>
      {/* This should recognize localVar is in scope */}
      {localVar}
    </div>
  );
}
```

When compiling MDX with local variables, the scope checking appears to be inverted - variables that ARE declared in the current scope are not being recognized, and vice versa.

### Expected behavior

The `inScope` function should return `true` when a variable is declared in the current scope or any parent scope, and `false` when it's not found anywhere in the scope chain.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
