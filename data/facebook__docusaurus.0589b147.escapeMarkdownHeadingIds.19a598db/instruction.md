# Bug Report

### Describe the bug

The `escapeMarkdownHeadingIds` function is not properly handling markdown headings that have only whitespace after the hash symbols. When a heading line contains just `#` followed by spaces or is otherwise empty, the heading ID escaping doesn't work as expected.

### Reproduction

```js
const content = `
# 
## Valid Heading {#custom-id}
### 
`;

const escaped = escapeMarkdownHeadingIds(content);
// The headings with only whitespace are not being processed correctly
```

Another case:
```js
const content = `# `;
const result = escapeMarkdownHeadingIds(content);
// Expected to handle this edge case but doesn't match the pattern
```

### Expected behavior

The function should properly handle all valid markdown heading patterns, including headings that may have trailing whitespace or are effectively empty after the hash symbols. The regex pattern should match headings consistently regardless of whether they have substantial content after the `#` symbols.

### Additional context

This affects markdown files where headings might be formatted with extra whitespace or where headings are still being written/edited. The current behavior is inconsistent with how markdown parsers typically handle heading syntax.

---
Repository: /testbed
