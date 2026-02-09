# Bug Report

### Describe the bug

I'm experiencing an issue with markdown text rendering where whitespace at the beginning and end of text nodes is being stripped unexpectedly. This is causing problems with formatting in my markdown documents, particularly when intentional leading or trailing spaces are needed.

### Reproduction

```js
const textNode = {
  type: 'text',
  value: '  some text with spaces  '
}

// After processing, the spaces are removed
// Expected: "  some text with spaces  "
// Actual: "some text with spaces"
```

This also affects inline code and other scenarios where preserving exact whitespace is important. For example:

```markdown
This is `  code with spaces  ` in the middle of a sentence.
```

The spaces inside the code block get trimmed when they shouldn't be.

### Expected behavior

Text node values should be preserved exactly as they are, including any leading or trailing whitespace. The markdown processor should not automatically trim whitespace from text content unless explicitly required by the markdown specification.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
