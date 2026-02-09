# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain inline constructs are not being recognized correctly. It seems like the parser is treating valid markdown syntax as plain text instead of processing it as expected.

### Reproduction

```js
const markdown = `
This is **bold text** and this is *italic text*.

Here's a [link](https://example.com) in the middle of a sentence.
`;

// Parse the markdown
const result = remark.parse(markdown);

// Expected: bold, italic, and link nodes to be created
// Actual: Everything is treated as plain text
```

When parsing markdown with inline elements like bold text, italics, or links that appear after certain characters or in specific positions, they're not being detected properly. The inline constructs seem to be ignored in cases where they should be valid.

### Expected behavior

The parser should correctly identify and process inline markdown constructs (bold, italic, links, etc.) regardless of their position in the text. All valid markdown syntax should be converted to the appropriate AST nodes.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in how the parser handles construct detection, but it's definitely affecting markdown rendering in my application.

---
Repository: /testbed
