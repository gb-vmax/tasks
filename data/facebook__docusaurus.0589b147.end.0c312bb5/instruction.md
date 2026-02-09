# Bug Report

### Describe the bug
HTML text parsing in markdown is broken - inline HTML tags are not being recognized correctly. When I try to use simple HTML tags like `<span>` or `<div>` in my markdown content, they're not being parsed as expected.

### Reproduction
```js
const markdown = 'This is <span>inline HTML</span> text'
const result = remark().processSync(markdown)
```

The HTML tags should be parsed and included in the output, but instead they seem to be getting rejected or handled incorrectly.

### Expected behavior
Inline HTML tags should be properly tokenized and included in the markdown AST. The parser should correctly identify the opening `<` and closing `>` of HTML tags and process them as valid HTML text nodes.

### Additional context
This seems to affect any inline HTML usage in markdown content. I noticed this started happening recently - previously inline HTML was working fine in my documents.

---
Repository: /testbed
