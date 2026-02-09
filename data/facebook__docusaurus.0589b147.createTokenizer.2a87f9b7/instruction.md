# Bug Report

### Describe the bug

I'm experiencing an issue with tokenization where the parser seems to be skipping the first construct in a list. When processing markdown content, certain syntax elements are not being recognized properly, particularly at the beginning of lines or blocks.

### Reproduction

```js
// When parsing markdown with multiple possible constructs
const content = `
# Heading
Some text
`;

// The parser appears to skip the first available construct
// and starts checking from the second one instead
```

### Expected behavior

The parser should evaluate all available constructs starting from index 0, not skip the first one. All valid markdown syntax should be properly recognized and tokenized.

### Additional context

This seems to affect various markdown elements including headings, lists, and code blocks. The issue appears to be related to how the construct list is being iterated during the tokenization process.

---
Repository: /testbed
