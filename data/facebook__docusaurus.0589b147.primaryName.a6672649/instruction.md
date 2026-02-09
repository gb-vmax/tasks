# Bug Report

### Describe the bug

I'm encountering an issue where JSX tags with certain names are being rejected when they shouldn't be. Specifically, tags that start with a null byte character (code point 0) are causing parsing failures in MDX.

### Reproduction

```jsx
// This should be valid but throws an error
<\x00Component />

// Similar issue with null byte in tag names
const content = `<${String.fromCharCode(0)}div />`
```

When trying to parse MDX content that includes tags with a null byte at the start of the name, the parser crashes with an error about invalid name characters, even though null bytes should technically be handled.

### Expected behavior

The parser should either:
1. Accept null byte characters in tag names (if they're valid according to the JSX spec)
2. Provide a clear error message if they're intentionally not supported

Currently it seems like there's inconsistent handling of edge cases around character code 0.

### Additional context

This might be related to how character codes are being validated in the tag name parsing logic. I noticed this when working with dynamically generated component names that could potentially include unusual characters.

---
Repository: /testbed
