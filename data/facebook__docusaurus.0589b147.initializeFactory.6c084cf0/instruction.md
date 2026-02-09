# Bug Report

### Describe the bug

I'm experiencing an issue where the MDX parser seems to be entering states in the wrong order during tokenization. The parser appears to consume code before properly entering the "data" state, which is causing unexpected behavior in how content is processed.

### Reproduction

```js
// When parsing MDX content with certain character sequences,
// the tokenizer doesn't handle the state transitions correctly

const mdx = `
Some content with special characters
`;

// The parser consumes tokens before entering the data state,
// leading to incorrect token boundaries
```

### Expected behavior

The parser should enter the "data" state before consuming tokens to ensure proper state tracking and token generation. The state machine should maintain the correct order of operations during content parsing.

### Additional context

This seems to affect how the parser handles specific character codes during the tokenization process. The issue manifests when processing content that requires state transitions in the tokenizer.

---
Repository: /testbed
