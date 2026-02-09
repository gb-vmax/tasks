# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where column positions appear to be off by one in certain scenarios. This seems to be affecting source mapping and error reporting accuracy.

When parsing MDX content, the column positions reported in the AST nodes don't match the actual character positions in the source text. Specifically, it looks like columns are being incremented when they shouldn't be.

### Reproduction

```js
const mdx = `
# Hello

Some text here
`;

const result = compile(mdx);
// Check the position information in the AST
// Column values are shifted by +1 from expected positions
```

### Expected behavior

Column positions in the AST should accurately reflect the actual character positions in the source code. If a token starts at column 5, the position should report column 5, not column 6.

This is particularly problematic when:
- Generating source maps
- Reporting syntax errors with precise locations
- Building editor integrations that rely on accurate position data

### Additional context

This seems to have been introduced recently and affects the `defineSkip` function in the tokenizer. The column tracking logic appears to have changed in a way that shifts all positions.

---
Repository: /testbed
