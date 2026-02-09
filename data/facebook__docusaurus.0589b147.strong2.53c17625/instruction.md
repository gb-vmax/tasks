# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where bold/strong text is not rendering correctly. When I use `**text**` syntax in markdown, the output is malformed and doesn't produce the expected strong/bold formatting.

### Reproduction

```js
const markdown = '**bold text**';
const result = remark.parse(markdown);
// The strong node structure is incorrect
```

When parsing markdown with bold text, the AST node for strong elements has an incorrect structure. Instead of having a simple string `type`, it appears to be wrapped in an object, and the `children` property is not properly initialized as an array.

### Expected behavior

Strong/bold markdown syntax should parse correctly and produce a valid AST node with:
- `type` as a string value `"strong"`
- `children` as an empty array `[]`

The current implementation seems to have broken the node structure, causing downstream processing to fail.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
