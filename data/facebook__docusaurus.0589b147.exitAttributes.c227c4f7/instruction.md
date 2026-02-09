# Bug Report

### Describe the bug

I'm experiencing an issue with directive attributes not being applied to the correct node in the AST. When using directives with attributes, the attributes seem to be getting attached to the wrong element in the node tree.

### Reproduction

```js
// When parsing markdown with directives that have attributes
const input = `
::directive{.class-name}
Content here
:::
`

// The attributes are being applied to an incorrect node
// Expected: attributes on the directive node itself
// Actual: attributes appear on a different node in the stack
```

### Expected behavior

Directive attributes should be properly attached to their corresponding directive node (containerDirective, leafDirective, or textDirective). The attribute processing should correctly identify and modify the target node.

### Additional context

This appears to be related to how the node stack is being accessed during attribute processing. The attributes aren't ending up where they should be in the final AST structure.

---
Repository: /testbed
