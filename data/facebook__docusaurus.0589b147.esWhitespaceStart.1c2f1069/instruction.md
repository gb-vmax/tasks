# Bug Report

### Describe the bug
I'm experiencing an issue with MDX parsing where whitespace handling in JSX tags appears to be inverted. When there's actual whitespace (spaces or unicode whitespace characters), the parser doesn't enter the "esWhitespace" state as expected. Conversely, when there's NO whitespace, it incorrectly tries to process it as whitespace.

### Reproduction
```mdx
<Component
  prop="value"
/>
```

When parsing JSX tags with whitespace between attributes or before the closing bracket, the whitespace is not being properly recognized and processed. The issue seems to affect both regular spaces and unicode whitespace characters.

### Expected behavior
The parser should correctly identify and handle whitespace characters within JSX tags. Spaces and unicode whitespace between attributes should be properly tokenized as "esWhitespace" tokens.

### Additional context
This affects MDX documents that use JSX components with multi-line attributes or spacing. The parser's whitespace detection logic seems to have the condition backwards - it's entering the whitespace state when it shouldn't and skipping it when it should.

---
Repository: /testbed
