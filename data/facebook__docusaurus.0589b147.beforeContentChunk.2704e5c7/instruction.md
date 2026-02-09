# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the content parsing logic seems to be inverted. Code blocks are not being recognized correctly, and the content inside them is being processed incorrectly.

### Reproduction

```mdx
```js
const example = 'test';
console.log(example);
```
```

When parsing this MDX content, the code block content is not handled properly. The parser appears to be checking conditions in the wrong order when processing code flow values.

### Expected behavior

Fenced code blocks should be parsed correctly with their content preserved as code, not processed as regular markdown content. The tokenizer should properly identify and handle the code block boundaries and content.

### Additional context

This seems to affect the `beforeContentChunk` function in the code fenced tokenizer. The logic for determining when to enter "codeFlowValue" appears to be executing at the wrong time, causing the parser to mishandle line endings and null values within code blocks.

---
Repository: /testbed
