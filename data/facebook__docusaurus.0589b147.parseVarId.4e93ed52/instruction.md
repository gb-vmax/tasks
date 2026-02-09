# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When using `let` or `const` declarations, the parser seems to be treating them the same as `var` declarations, which is causing incorrect scoping behavior.

### Reproduction

```mdx
export const MyComponent = () => {
  let x = 1;
  const y = 2;
  
  if (true) {
    let x = 3;  // Should be block-scoped, but behaves like var
    const y = 4; // Should be block-scoped, but behaves like var
  }
  
  console.log(x); // Expected: 1, but may show unexpected behavior
}
```

The block-scoped variables (`let` and `const`) are not being validated with proper lexical binding rules. This means they're being treated more like `var` declarations, which can lead to scoping issues that shouldn't occur with ES6+ syntax.

### Expected behavior

- `let` and `const` declarations should follow lexical scoping rules
- Variables declared with `let`/`const` inside blocks should be properly scoped to those blocks
- The parser should enforce block-level binding for lexical declarations

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This appears to be a regression in how the parser handles binding patterns for different variable declaration types.

---
Repository: /testbed
