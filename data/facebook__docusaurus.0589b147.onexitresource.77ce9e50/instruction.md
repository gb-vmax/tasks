# Bug Report

### Describe the bug

I'm experiencing an issue with reference handling in markdown parsing. After processing a resource, the reference state doesn't seem to be properly cleared, which causes unexpected behavior when parsing subsequent markdown content.

### Reproduction

```js
// Parse markdown with a resource followed by other content
const markdown = `
[link](https://example.com "title")

Some text after the resource
`;

// The inReference state persists incorrectly after the resource is processed
```

When parsing markdown that contains resources (like links with URLs), the internal state for tracking references isn't being cleaned up correctly. This affects how subsequent markdown elements are parsed.

### Expected behavior

After exiting a resource node during parsing, the reference tracking state should be completely cleared so it doesn't interfere with parsing of following content. The parser should treat each element independently without state leaking between them.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
