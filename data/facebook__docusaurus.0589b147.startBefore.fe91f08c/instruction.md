# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX. When parsing fenced code blocks, the closing fence delimiter is not being properly tokenized. The parser appears to be entering a "lineEnding" token but then immediately exiting a "lineEndingPrefix" token without consuming the actual code character, which seems incorrect.

### Reproduction

```mdx
# Test Document

```js
const test = 'hello';
```

More content here
```

When this MDX is parsed, the closing fence (the second set of backticks) doesn't get processed correctly. The tokenizer enters the lineEnding state but fails to consume the character before exiting.

### Expected behavior

The closing code fence should be properly tokenized with the character being consumed between entering and exiting the lineEnding token. The parser should correctly identify where the fenced code block ends.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
