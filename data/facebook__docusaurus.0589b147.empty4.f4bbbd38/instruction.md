# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX content. Text nodes that should be considered empty/whitespace-only are now being treated as non-empty, which is causing unexpected rendering behavior.

### Reproduction

```js
// When processing MDX content with whitespace-only text nodes
const content = `
<Component>
   
</Component>
`

// The whitespace between tags is not being properly detected as empty
// This causes extra spacing or unexpected elements in the output
```

### Expected behavior

Whitespace-only text nodes (containing only spaces, tabs, newlines, etc.) should be correctly identified as empty and handled accordingly. The current behavior seems to be treating them as non-empty content.

### System Info
- @mdx-js/mdx version: 3.0.0

This is affecting our documentation site where we have components with whitespace between tags. The extra spacing is breaking our layout.

---
Repository: /testbed
