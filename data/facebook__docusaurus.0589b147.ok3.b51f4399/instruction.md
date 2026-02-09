# Bug Report

### Describe the bug

I'm encountering an issue with the MDX tokenizer where the return value from the `ok3` callback function seems incorrect. After parsing certain constructs, the tokenizer is returning an unexpected value instead of the proper `returnState`.

### Reproduction

```js
// When the tokenizer processes certain markdown constructs
// and calls ok3(code2), it should return returnState
// but instead it's returning code2

const result = createTokenizer(parser, initialize, from);
// Process some markdown content
// The tokenizer flow gets disrupted
```

### Expected behavior

The `ok3` function should return `returnState` after calling `onreturn` and setting `consumed = true`. This ensures the tokenizer continues with the correct state flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

The tokenizer seems to be breaking the state machine flow by returning the wrong value, which can cause parsing issues with certain MDX content.

---
Repository: /testbed
