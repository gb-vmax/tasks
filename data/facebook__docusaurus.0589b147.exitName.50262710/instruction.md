# Bug Report

### Describe the bug

I'm experiencing an issue with directive name parsing in nested directive structures. When using directives inside other directives, the name property seems to be assigned to the wrong node in the AST.

### Reproduction

```js
// Example markdown with nested directives
const markdown = `
:::outer
::inner
Content here
::
:::
`;

// After parsing, the inner directive's name gets incorrectly assigned
// The 'outer' directive ends up with the name 'inner' instead of 'outer'
```

When I parse markdown containing nested directives (like container directives with leaf or text directives inside them), the name of the inner directive appears to overwrite or be assigned to the parent directive node instead of the correct child node.

### Expected behavior

Each directive should have its own name property correctly assigned to its corresponding node. The parent directive should retain its name even when child directives are parsed.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
