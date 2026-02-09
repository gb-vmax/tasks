# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the document flow handling seems to be broken. When processing MDX content, the parser appears to be consuming code points incorrectly and the flow tokenizer isn't being initialized properly in certain cases.

### Reproduction

```js
// Processing an MDX document with flow content
const mdx = `
# Heading

Some paragraph content.
`;

// Parse the MDX content
const result = compile(mdx);
// The parsing fails or produces unexpected output
```

### Expected behavior

The MDX parser should correctly handle flow content initialization and consume code points in the proper order. The `childFlow` tokenizer should be initialized before being used, and `effects.consume()` should be called at the appropriate time during the flow parsing process.

Currently, it seems like the flow continuation logic is trying to use `childFlow` before it's properly set up, and the consumption of code points is happening out of sequence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
