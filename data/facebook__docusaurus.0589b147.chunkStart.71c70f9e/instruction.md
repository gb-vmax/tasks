# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the document structure seems to be getting corrupted. When using nested directive containers, the content type and token linking appears to be broken, leading to parsing errors or incorrect AST generation.

### Reproduction

```js
const input = `
:::outer
Some content

:::inner
Nested content
:::

More outer content
:::
`;

// Parse the markdown with remark-directive
const result = processor.parse(input);
// The AST structure is malformed - contentType is wrong
// and the token chain linking (previous/next) is broken
```

### Expected behavior

Nested directive containers should parse correctly with proper contentType set to "document" and the token chain should be properly linked so that `previous.next` points to the current token.

### Additional context

This seems to affect how the parser handles the document chunks within directive containers. The issue manifests when trying to process nested directives or when the directive container has multiple content blocks.

---
Repository: /testbed
