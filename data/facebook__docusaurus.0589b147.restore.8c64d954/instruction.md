# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer state restoration isn't working correctly. When the parser needs to backtrack and restore its state, the events array gets cleared completely instead of being restored to its previous state.

### Reproduction

```js
// Parse MDX content that requires tokenizer backtracking
const mdxContent = `
# Header

Some content with **bold** and *italic* text.

\`\`\`js
code block
\`\`\`
`;

const result = compile(mdxContent);
// Events are lost during parsing, resulting in incomplete output
```

### Expected behavior

When the tokenizer restores its state during backtracking, it should preserve the events that occurred before the restore point. The `context.events.length` should be set to `startEventsIndex` to keep the existing events, not cleared to 0.

### Additional context

This affects parsing of complex MDX documents where the tokenizer needs to backtrack, particularly with nested formatting or code blocks. The parsed output is incomplete because events are being discarded incorrectly.

---
Repository: /testbed
