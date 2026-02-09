# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the parser appears to be completely broken. When trying to parse MDX content, I'm getting unexpected errors or incorrect AST nodes being generated.

### Reproduction

```js
// Attempting to parse any MDX content fails
const mdx = `
# Hello

<Component />
`;

// Parser throws errors or generates malformed AST
const result = parseMDX(mdx);
```

### Expected behavior

The MDX parser should correctly parse the content and generate a valid AST with proper node positions and types.

### Additional context

This seems to have started happening recently. The parser was working fine before, but now even simple MDX documents are failing to parse correctly. The issue appears to be related to how AST nodes are being finalized during the parsing process.

---
Repository: /testbed
