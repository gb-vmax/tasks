# Bug Report

### Describe the bug

I'm encountering an issue with parsing fenced code blocks in MDX content. The parser seems to be generating events in the wrong order, which causes problems when processing the token stream.

### Reproduction

```js
const mdx = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parse the MDX content
const result = compile(mdx);
// The event order for codeFenced tokens is incorrect
```

When parsing fenced code blocks, the events are being emitted in an unexpected sequence. Specifically, the `codeFenced` and `codeFencedFence` events appear to be out of order, which breaks downstream processing that relies on the correct nesting structure.

### Expected behavior

The parser should emit events in the proper hierarchical order:
1. `codeFenced` (parent container)
2. `codeFencedFence` (fence markers)
3. `codeFencedFenceSequence` (the actual backticks)

Instead, it seems like `codeFencedFence` is being emitted before `codeFenced`, which violates the expected nesting structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues with custom plugins that traverse the syntax tree and expect proper event ordering. Any help would be appreciated!

---
Repository: /testbed
