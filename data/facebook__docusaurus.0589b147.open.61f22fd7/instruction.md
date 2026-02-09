# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where certain nested structures are not being processed correctly. It seems like some callback functions that should be executed conditionally are being skipped when they shouldn't be, or vice versa.

### Reproduction

When parsing markdown with nested elements (like lists within blockquotes, or emphasis within links), the parser is not properly handling the opening of nested structures. The behavior is inconsistent with what was working before.

```js
const markdown = `
> - **bold text** in list
> - another item
`;

// Parse the markdown
const result = parse(markdown);

// The nested structure is not properly created
// Expected: blockquote containing list with bold items
// Actual: structure is malformed or incomplete
```

### Expected behavior

The parser should correctly handle nested markdown structures by properly executing the callback functions when opening nested elements. All nested elements should be properly initialized and added to the AST.

### Additional context

This seems to affect any markdown that has multiple levels of nesting. The issue appears to be related to how the parser handles the opening of nested tokens - it's either skipping necessary initialization steps or executing them when it shouldn't.

---
Repository: /testbed
