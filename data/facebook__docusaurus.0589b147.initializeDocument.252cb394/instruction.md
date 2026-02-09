# Bug Report

### Describe the bug
I'm experiencing issues with nested container parsing in markdown documents. When working with deeply nested block-level elements (like lists within blockquotes within lists), the parser seems to incorrectly handle container boundaries and exits, leading to malformed output or unexpected parsing behavior.

### Reproduction
```js
const markdown = `
> - Item 1
>   - Nested item
>     - Deeply nested
> - Item 2
`;

// Parse the markdown
const result = parse(markdown);

// The nested structure is not correctly preserved
// Some containers are exited prematurely or not at all
```

### Expected behavior
The parser should correctly maintain the container stack and properly exit containers at the right boundaries. Deeply nested structures should be preserved with their correct hierarchy.

### Additional context
This seems to affect documents with multiple levels of nesting (3+ levels deep). The issue appears to be related to how the parser tracks and exits container states when processing line endings and continuation checks.

---
Repository: /testbed
