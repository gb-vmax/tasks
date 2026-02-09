# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace trimming in code blocks. When processing markdown content with trailing whitespace, the trimming function seems to be removing one character too many from the end of lines.

### Reproduction

```js
const content = `
  some text with spaces  
  another line  
`;

// After processing, the last character of each line is incorrectly removed
// Expected: "some text with spaces  "
// Actual: "some text with spaces "
```

### Expected behavior

The trimming should only remove leading/trailing whitespace characters (tabs and spaces), but preserve the actual content of the line. Currently it appears to be cutting off the last character even when it's not whitespace.

### System Info
- Version: remark-rehype@11.0.0
- Node: v18.x

---
Repository: /testbed
