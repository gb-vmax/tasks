# Bug Report

### Describe the bug

When parsing MDX JSX tags with closing markers, the tag object is being mutated directly instead of working with a copy. This causes the original `mdxJsxTag` data to be modified, which can lead to unexpected behavior when the same tag data is referenced elsewhere in the parsing process.

### Reproduction

```js
// Parse MDX content with self-closing JSX tags
const mdxContent = `
<Component />
`;

// The parser modifies the original tag object in place
// when setting the close property, affecting other references
// to the same tag data structure
```

### Expected behavior

The parser should work with a copy of the tag object when setting properties like `close`, so that the original `mdxJsxTag` data structure remains unchanged and can be safely used in other parts of the parsing logic.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
