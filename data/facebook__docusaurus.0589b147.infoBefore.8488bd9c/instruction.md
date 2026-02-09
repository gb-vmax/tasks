# Bug Report

### Describe the bug

When parsing fenced code blocks with info strings in markdown, the parser is generating events in the wrong order. The `codeFencedFenceInfo` event is being entered after `chunkString` instead of before it, which breaks the expected AST structure.

### Reproduction

```js
const markdown = '```javascript\nconst x = 1;\n```';
const ast = parser.parse(markdown);

// The event order in the token stream is incorrect
// Expected: codeFencedFenceInfo -> chunkString
// Actual: chunkString -> codeFencedFenceInfo
```

### Expected behavior

The `codeFencedFenceInfo` token should be entered before the `chunkString` token to maintain proper nesting in the AST. Additionally, the `codeFencedFence` exit event appears to be missing when processing the fence info line.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
