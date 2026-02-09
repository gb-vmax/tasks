# Bug Report

### Describe the bug

I'm encountering an issue where markdown parsing seems to hang or produce incorrect output when processing certain content. The parser appears to be getting stuck in what looks like an infinite loop or recursion when trying to serialize tokens.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Test heading

Some paragraph text with **bold** content.
`;

// This call hangs indefinitely
const result = processor.processSync(markdown);
```

### Expected behavior

The markdown should be parsed normally without hanging, and the serialization process should complete successfully.

### Additional context

This seems to have started happening recently. The parser gets stuck during the token serialization phase. I noticed it particularly happens with documents that have formatted text, but I'm not sure if that's the exact trigger.

---
Repository: /testbed
