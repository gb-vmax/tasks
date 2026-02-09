# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the output is completely broken. Instead of getting the actual parsed markdown content, I'm receiving numeric values (what looks like array indices or lengths) in the output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Hello World

This is a paragraph with **bold** text.

- Item 1
- Item 2
`;

const result = processor.processSync(markdown);
console.log(String(result));
```

### Expected behavior

The processor should return the properly parsed markdown content. Instead, I'm getting numbers in the output where the actual content should be.

### Additional context

This seems to affect all markdown processing - headings, paragraphs, lists, etc. The structure might be there but the actual text content is replaced with what appears to be numeric values. This makes the entire parser unusable for any practical purpose.

Not sure if this is related to a recent change, but it's preventing me from using the library at all right now.

---
Repository: /testbed
