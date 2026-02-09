# Bug Report

### Describe the bug

I'm encountering an issue with MDX heading parsing where headings are being generated with incorrect node types. When processing MDX documents, the heading elements appear to be using the wrong type identifier in the AST.

### Reproduction

```js
// Parse an MDX document with headings
const mdxContent = `
# Hello World

Some content here
`;

const result = compile(mdxContent);
// The AST nodes for headings have unexpected type property
```

When I inspect the generated AST, heading nodes are not being created with the expected structure. This causes downstream processing to fail since the node type doesn't match what other parts of the system expect.

### Expected behavior

Headings should be generated with the correct node type in the AST. The type property should match the standard MDAST specification for heading nodes so that transformers and other plugins can properly identify and process them.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
