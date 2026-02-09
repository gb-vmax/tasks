# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the parser seems to get stuck in an infinite loop or hangs when processing code block content. This appears to be related to how the tokenizer handles code flow values.

### Reproduction

```mdx
```js
const example = "test";
console.log(example);
```
```

When parsing MDX content with fenced code blocks like the above, the parser doesn't complete properly. The content inside the code fence isn't being processed correctly.

### Expected behavior

The fenced code block should be parsed completely without hanging, and the content should be properly tokenized and rendered.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The parser appears to be stuck in the `contentChunk` function when processing code block values.

---
Repository: /testbed
