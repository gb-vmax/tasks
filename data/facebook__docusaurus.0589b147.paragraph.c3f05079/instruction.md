# Bug Report

### Describe the bug
When rendering markdown paragraphs, the output is incorrect - it seems like paragraph content is being processed as flow content instead of phrasing content. This is causing unexpected formatting issues in the generated markdown.

### Reproduction
```js
const markdown = remark()
  .use(remarkStringify)
  .processSync('This is a simple paragraph with **bold** text.');

console.log(String(markdown));
// Output is malformed - phrasing content not handled correctly
```

### Expected behavior
Paragraphs should be processed as phrasing content (inline elements like bold, italic, links, etc.) and maintain proper markdown structure. The paragraph content should be correctly serialized with inline formatting preserved.

### Additional context
This appears to affect any markdown document with paragraphs containing inline formatting. The issue seems related to how the paragraph node processes its children - it's treating them as block-level flow content when they should be inline phrasing content.

---
Repository: /testbed
