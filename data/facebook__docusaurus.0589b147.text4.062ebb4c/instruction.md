# Bug Report

### Describe the bug

I'm experiencing an issue with MDX text node processing where the source positions/locations are being assigned incorrectly. When text nodes are converted to JSX expression containers, the position information seems to be swapped between the literal value and its container.

### Reproduction

```mdx
# Hello World

This is some text content in MDX.
```

When processing text nodes, the position data ends up on the wrong AST nodes. The `Literal` node receives the position from the container, and the `JSXExpressionContainer` receives the position from the literal, which is backwards.

This affects any tooling that relies on accurate source position information (like syntax highlighting, error reporting, or source maps).

### Expected behavior

The `state.inherit()` and `state.patch()` calls should apply position information to the correct nodes:
- The `Literal` expression should inherit position from the original text node
- The `JSXExpressionContainer` wrapper should be patched with the original text node's position

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
