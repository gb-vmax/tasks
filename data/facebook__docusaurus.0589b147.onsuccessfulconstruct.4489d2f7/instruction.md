# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it seems to stop processing tokens correctly. After making some changes to my markdown content, the parser appears to hang or not complete parsing, and I'm not getting the expected output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some paragraph text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result); // Expected: parsed AST, Actual: incomplete or no output
```

### Expected behavior

The markdown should be parsed successfully and return a complete AST with all the nodes (heading, paragraph, list, etc.) properly tokenized and structured.

### Additional context

This seems to happen with various markdown constructs - headings, lists, emphasis, etc. The parser worked fine before, but now it's not producing the expected results. Not sure if this is related to a recent change in the tokenizer logic.

---
Repository: /testbed
