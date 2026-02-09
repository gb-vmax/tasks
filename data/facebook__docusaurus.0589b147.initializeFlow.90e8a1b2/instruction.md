# Bug Report

### Describe the bug

I'm experiencing an issue with flow parsing where the parser seems to get stuck or doesn't properly continue after processing line endings. The flow initialization appears to be handling blank line endings incorrectly, and after processing a construct with a line ending, the parser doesn't return to the initial state as expected.

### Reproduction

```js
// Parse MDX content with blank lines and flow constructs
const content = `
Some content here

Another line after blank
`;

// The parser doesn't properly handle the transition
// between blank line endings and subsequent flow content
```

When parsing content that contains:
1. Initial flow content
2. Blank lines (line endings)
3. Additional flow content after the blank lines

The parser fails to properly transition back to parsing the next flow content after encountering blank line endings.

### Expected behavior

After processing a blank line ending or a line ending following a construct, the parser should return to the initial flow parsing state to continue processing subsequent content. The flow should continue seamlessly through blank lines and constructs.

### Additional context

This seems to affect content parsing where there are multiple sections separated by blank lines. The parser state (`currentConstruct`) may not be getting reset at the right time, causing issues with how subsequent content is processed.

---
Repository: /testbed
