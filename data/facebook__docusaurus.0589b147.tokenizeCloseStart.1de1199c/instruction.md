# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX files not being parsed correctly. When I use triple backticks to create a code fence, the closing fence is not being recognized properly, causing the entire rest of the document to be treated as code.

### Reproduction

```markdown
# My Document

Some text here

```js
console.log('hello');
```

More text after the code block
```

### Expected behavior

The code block should be properly closed after the three closing backticks, and "More text after the code block" should be rendered as normal markdown text, not as part of the code block.

### Actual behavior

The closing fence (```) is not recognized, so everything after the opening fence is treated as code content. The parser doesn't exit the code fence state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking our documentation updates. Any help would be appreciated!

---
Repository: /testbed
