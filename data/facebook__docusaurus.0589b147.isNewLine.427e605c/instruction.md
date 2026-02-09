# Bug Report

### Describe the bug

I'm encountering an issue with line break detection in MDX files. It seems like certain newline characters are not being recognized properly, which is causing parsing errors or unexpected behavior when processing MDX content.

### Reproduction

```js
// MDX content with different line break types
const mdxContent = `
# Heading

Some text with regular line breaks.
More content here.
`;

// Process the MDX - line breaks are not detected correctly
// Characters like \n (code 10) should be recognized as line breaks
```

When I have MDX files with standard newlines (character code 10), they're not being treated as line breaks anymore. This affects how the content is parsed and formatted.

### Expected behavior

All standard newline characters should be properly detected:
- `\n` (line feed, code 10)
- `\r` (carriage return, code 13)  
- Unicode line separator (code 8232)
- Unicode paragraph separator (code 8233)

The parser should correctly identify these as line breaks and handle the content accordingly.

### Additional context

This seems to have started recently. My MDX files that were working fine before are now having parsing issues. The line break detection logic might have been changed inadvertently.

---
Repository: /testbed
