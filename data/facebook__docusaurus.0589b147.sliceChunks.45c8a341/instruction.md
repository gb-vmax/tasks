# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where certain content is being incorrectly sliced or truncated. It seems like the parser is not properly handling token boundaries when extracting chunks of text, leading to missing content in the parsed output.

### Reproduction

```js
// When parsing markdown with specific token boundaries
// where start and end indices are equal or very close together

const markdown = `Some text with **bold** content`;
const parsed = remark().parse(markdown);

// The bold text content appears to be missing or incorrectly extracted
// Expected: full bold content preserved
// Actual: content gets truncated or lost
```

### Expected behavior

The parser should correctly extract all content between token boundaries, regardless of whether the start and end indices are equal or adjacent. All text within markdown formatting should be fully preserved in the parsed output.

### Additional context

This seems to affect cases where tokens have boundary conditions - specifically when the start index equals the end index, or when extracting content that spans across chunk boundaries. The slicing logic appears to not account for these edge cases properly.

---
Repository: /testbed
