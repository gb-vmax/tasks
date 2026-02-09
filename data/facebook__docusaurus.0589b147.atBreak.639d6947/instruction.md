# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in markdown. When processing headings with trailing hash symbols (like `## Heading ##`), the parser seems to be entering states in the wrong order, which causes the tokenization to fail or produce incorrect results.

### Reproduction

```js
// Parse markdown with ATX headings that have trailing hashes
const markdown = `## Heading Title ##`;

// The parser doesn't correctly handle the sequence
// Expected: proper tokenization of heading with trailing hashes
// Actual: incorrect state transitions in the tokenizer
```

This also affects headings with multiple spaces before the trailing hashes:

```js
const markdown2 = `### Another Heading   ###`;
```

### Expected behavior

The parser should correctly tokenize ATX headings regardless of whether they have trailing hash symbols or whitespace. The `atxHeadingSequence` token should be entered at the appropriate time during the tokenization process.

### Additional context

This seems to be related to how the `atBreak` function handles state transitions when encountering hash symbols and whitespace. The order of operations when entering/exiting token states appears to be incorrect.

---
Repository: /testbed
