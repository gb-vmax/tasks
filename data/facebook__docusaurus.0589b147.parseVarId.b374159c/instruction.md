# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in MDX files. When using `let` or `const` declarations, they're being treated incorrectly - it seems like they're being validated with the wrong binding type, which is causing unexpected behavior in my MDX components.

### Reproduction

```mdx
export const MyComponent = () => {
  let items = [1, 2, 3];
  const config = { enabled: true };
  
  return <div>{items.length}</div>;
}
```

When this MDX is processed, the `let` and `const` declarations don't behave as expected. It appears that the parser is confusing lexical bindings (`let`/`const`) with var bindings.

### Expected behavior

- `let` and `const` declarations should be treated as lexical bindings (block-scoped)
- `var` declarations should be treated as var bindings (function-scoped)
- The parser should correctly differentiate between these declaration types

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems to have broken recently and is affecting how variables are scoped in my MDX components. Any help would be appreciated!

---
Repository: /testbed
