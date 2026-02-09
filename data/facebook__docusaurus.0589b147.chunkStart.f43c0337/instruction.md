# Bug Report

### Describe the bug

I'm experiencing an issue with markdown content parsing where the order of operations seems to have changed. The parser is now entering the "content" token after entering the "chunkContent" token, which appears to be causing problems with the token tree structure.

### Reproduction

When parsing markdown content, the tokenizer is not properly structuring the token hierarchy. The issue manifests when processing chunks of content - the parent "content" token is being entered at the wrong point in the sequence.

```js
// Parsing any markdown content now produces an incorrect token structure
const result = parseMarkdown("Some **bold** text");
// The content and chunkContent tokens are nested incorrectly
```

### Expected behavior

The "content" token should be entered before the "chunkContent" token to maintain the proper parent-child relationship in the token tree. The tokenizer should:
1. Enter "content" token first
2. Then enter "chunkContent" token as a child
3. Process the chunk inside

Instead, it's currently:
1. Entering "chunkContent" token first
2. Then entering "content" token (passed as an argument to chunkInside)

This breaks the expected token hierarchy and likely causes downstream parsing issues.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
