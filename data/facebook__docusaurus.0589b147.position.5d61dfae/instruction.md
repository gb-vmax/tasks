# Bug Report

### Describe the bug

I'm encountering a critical issue where position information is completely broken in the MDX parser. When trying to process MDX files, the parser crashes because it can't properly stringify position data for error reporting or source mapping.

### Reproduction

```js
const mdx = `
# Hello World

Some content here
`;

// Try to parse MDX content
const result = parseSync(mdx);

// Any operation that needs position information fails
// For example, error reporting or source map generation
```

When the parser tries to format position information (like for error messages showing line/column numbers), it completely fails because the position stringification is broken.

### Expected behavior

The parser should be able to properly format position information as `line:column-line:column` (e.g., `1:1-2:5`) for error messages and source mapping. This is essential for debugging and tooling support.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a regression - the position formatting was working in previous versions but now appears to be completely corrupted in the vendored bundle.

---
Repository: /testbed
