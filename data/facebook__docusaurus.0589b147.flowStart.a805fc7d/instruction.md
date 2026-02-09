# Bug Report

### Describe the bug

I'm encountering an issue with MDX document parsing where empty documents or documents with only whitespace are not being handled correctly. The parser seems to exit containers improperly when reaching the end of the document, which causes the document structure to be malformed.

### Reproduction

```js
// Parse an empty MDX document
const result = compile('');

// Or a document with only whitespace
const result2 = compile('   \n\n');
```

When parsing these types of documents, the internal container state doesn't get cleaned up properly at the end of the document flow.

### Expected behavior

Empty or whitespace-only MDX documents should be parsed successfully and produce valid output with properly closed containers. The parser should handle the end-of-document (`null` code) by closing all flows and exiting all containers correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
