# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the directive name is being assigned to the wrong node in the AST. When parsing directives (container, leaf, or text directives), the name property appears to be set on an incorrect element in the node stack.

### Reproduction

```js
// Parse a directive with remark-directive
const directive = ':myDirective[label]{key=value}'

// After parsing, the directive name 'myDirective' 
// is not being assigned to the correct node
```

When processing directives, the name extraction seems to be targeting the wrong stack position, which could lead to:
- Directive names appearing on parent nodes instead of the directive node itself
- Missing or undefined directive names on the actual directive nodes
- Potential crashes or assertion failures during parsing

### Expected behavior

The directive name should be correctly assigned to the directive node itself (containerDirective, leafDirective, or textDirective), not to its parent or sibling nodes in the stack.

### Additional context

This affects all three directive types:
- Container directives (:::)
- Leaf directives (::)
- Text directives (:)

The issue appears to be in the exitName function where the node is retrieved from the stack before assigning the name property.

---
Repository: /testbed
