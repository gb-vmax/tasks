# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the document chunk linking appears to be broken. When parsing nested directive containers, the previous/next token chain seems to get corrupted, causing the document structure to be malformed.

### Reproduction

```js
const markdown = `
:::outer
Content in outer

:::inner
Nested content
:::

More outer content
:::
`;

// Parse the markdown with directive containers
const result = parseMarkdown(markdown);

// The token chain is broken - previous/next references are incorrect
console.log(result.children); // Shows malformed structure
```

### Expected behavior

The parser should correctly maintain the token chain when processing nested directive containers. Each chunk document should properly reference its previous token, and the previous token should reference the current one via the `next` property.

### Additional context

This seems to affect any markdown content with nested directive containers. The issue appears to be in how the chunk tokens are being linked together during parsing.

---
Repository: /testbed
