# Bug Report

### Describe the bug

I'm encountering an issue with whitespace handling in MDX parsing. When processing markdown content with spaces, the parser seems to skip over the space consumption logic and immediately returns, causing whitespace to not be properly handled in the output.

### Reproduction

```js
// Example MDX content with spaces
const mdxContent = `
# Heading with    multiple spaces

This paragraph    has irregular    spacing.
`;

// Parse the content
const result = compile(mdxContent);

// Expected: spaces should be normalized/processed
// Actual: spaces appear to be skipped in processing
```

### Expected behavior

Whitespace should be properly consumed and processed according to the markdown specification. Multiple spaces should be handled correctly, and the `factorySpace` function should iterate through all space characters up to the specified limit before continuing.

### Additional context

This seems to affect any content where space normalization is important. The parser appears to be returning early without properly consuming the space characters, which breaks the expected flow of the tokenization process.

---
Repository: /testbed
