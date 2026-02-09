# Bug Report

### Describe the bug

I'm encountering an issue with keyword detection in the parser. It seems like keywords are not being recognized properly, causing the parser to treat reserved words as regular identifiers.

### Reproduction

When parsing code that contains JavaScript keywords, they're being tokenized incorrectly:

```js
// Example code that fails to parse correctly
const code = `
  if (condition) {
    return true;
  }
`;

// Keywords like 'if' and 'return' are not recognized as keywords
// They get treated as regular identifiers instead
```

### Expected behavior

Reserved keywords should be properly identified and tokenized with their correct type (e.g., `if`, `return`, `function`, etc.) rather than being treated as generic names/identifiers.

### System Info
- Version: 3.0.0
- Parser: acorn 8.10.0

This seems to have started recently. The keyword test is failing because the word variable is undefined when it's being checked against the keywords regex.

---
Repository: /testbed
