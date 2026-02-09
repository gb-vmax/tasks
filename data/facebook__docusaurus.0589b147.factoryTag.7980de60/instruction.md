# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain characters in JSX tag names are not being handled correctly. It seems like the parser is rejecting valid tag names that start with specific Unicode characters.

### Reproduction

```jsx
// This MDX content fails to parse correctly
<Component\u0000Name>content</Component\u0000Name>

// Also affects tags with null byte characters
const mdx = `<Tag\x00>Hello</Tag\x00>`
```

When trying to parse MDX content that includes tag names with null bytes or certain low-value Unicode characters, the parser doesn't behave as expected. The tag name validation appears to be too strict.

### Expected behavior

The parser should properly handle edge cases with Unicode characters in tag names, or at least provide clear error messages when encountering invalid characters. Currently it seems to silently fail or produce unexpected results.

### Additional context

This might be related to how the parser checks character codes when validating tag names. The issue appears to affect the transition between tag name parsing and attribute parsing states.

---
Repository: /testbed
