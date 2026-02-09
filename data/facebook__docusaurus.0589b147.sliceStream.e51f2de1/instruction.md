# Bug Report

### Describe the bug

I'm encountering an issue with the MDX tokenizer where the arguments to `sliceChunks` appear to be in the wrong order. When processing MDX content, the tokenizer is passing parameters incorrectly which causes unexpected behavior during parsing.

### Reproduction

```js
// When the tokenizer tries to slice the stream:
function sliceStream(token) {
  return sliceChunks(token, chunks);  // Arguments seem reversed
}

// This causes issues when parsing MDX content with tokens
```

The `sliceStream` function is calling `sliceChunks` with `token` as the first argument and `chunks` as the second, but based on the context and how it's used elsewhere in the codebase, these arguments should be in the opposite order.

### Expected behavior

The tokenizer should correctly slice chunks based on the token boundaries. The arguments to `sliceChunks` should be `(chunks, token)` not `(token, chunks)`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Affected file: jest/vendor/@mdx-js__mdx@3.0.0.js

This is causing parsing issues when processing MDX documents. Has anyone else run into this?

---
Repository: /testbed
