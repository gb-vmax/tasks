# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in markdown parsing. When a directive container reaches the end of the document (null character), the parser seems to hang or not properly terminate the parsing flow.

### Reproduction

```js
const markdown = `
:::note
This is a directive container
:::
`;

// Parser doesn't complete properly when processing this
const result = parser.parse(markdown);
```

The issue appears when the directive container is at the end of the document without trailing content. The parser flow doesn't return correctly after processing the container's closing sequence.

### Expected behavior

The parser should properly complete and return the parsed result when encountering the end of a directive container at the document boundary. The parsing should terminate cleanly without hanging.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
