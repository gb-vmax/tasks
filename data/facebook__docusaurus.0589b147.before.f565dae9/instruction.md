# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading sequence tokens are being closed prematurely. When parsing markdown headings (like `# Heading` or `## Subheading`), the token structure appears to be malformed.

### Reproduction

```js
// Parse a simple ATX heading
const result = parse('# Hello World')

// The atxHeadingSequence token is exited before 
// the sequence is fully consumed
```

When tokenizing headings, the `atxHeadingSequence` token gets exited immediately in the `before` function, but the actual sequence parsing happens in `sequenceOpen` which is called after the exit. This creates an incorrect token structure where the exit happens before all the `#` characters are consumed.

### Expected behavior

The `atxHeadingSequence` token should be entered, then all heading characters (`#`) should be consumed, and only then should the token be exited. The token boundaries should properly encapsulate the entire heading sequence.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
