# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where the marker tokens appear to be in the wrong order in the output. When parsing MDX expressions (like `{expression}`), the opening marker is being emitted after the expression type is entered but before it's actually consumed, which seems backwards.

### Reproduction

```jsx
// Parse MDX content with an expression
const mdx = `
# Hello

{someExpression}
`

// When parsing this, the token stream has the markerType exit 
// happening before the marker is consumed, causing issues with
// proper AST construction
```

### Expected behavior

The marker should be entered, consumed, and then exited in the proper sequence. The current behavior breaks the expected token order where we should see:
1. Enter expression type
2. Enter marker type  
3. Consume marker
4. Exit marker type
5. Continue with expression content

Instead, the marker type is being exited before it's consumed, which disrupts downstream parsers and AST builders that rely on the correct token ordering.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
