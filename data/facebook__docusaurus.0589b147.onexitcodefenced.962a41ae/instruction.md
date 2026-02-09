# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When processing code blocks with triple backticks (```), the content is not being captured correctly. It seems like the parser is accessing the wrong node in the stack, causing the code block value to be set on the parent element instead of the code block itself.

### Reproduction

```markdown
# Test Document

Some text before

```js
function test() {
  console.log('hello');
}
```

More text after
```

When parsing this markdown, the code block content ends up in the wrong place in the AST. The fenced code block node doesn't contain the actual code.

### Expected behavior

The fenced code block should contain the code content (`function test() { ... }`), and the parent node should remain unchanged. The parser should correctly identify and populate the code block node with its value.

### Additional context

This appears to affect all fenced code blocks regardless of the language specified. The issue doesn't occur with indented code blocks, only with fenced code blocks using triple backticks.

---
Repository: /testbed
