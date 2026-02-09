# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain content is being consumed incorrectly, causing the parser to skip over characters or produce unexpected output. It seems like the parser is consuming an extra character at break points, which leads to malformed output or missing content.

### Reproduction

```js
// When parsing MDX content with specific break patterns
const mdx = `
Some text here
- List item
More content
`

// The parser appears to skip characters or produce incorrect output
// Expected: All content should be preserved
// Actual: Some characters are missing or duplicated
```

### Expected behavior

The MDX parser should correctly handle all characters in the input without consuming extra characters at break points. All content should be preserved and rendered correctly.

### Additional context

This appears to be related to how the parser handles data tokens and break detection. The issue manifests when the parser encounters certain character sequences that trigger the break detection logic.

---
Repository: /testbed
