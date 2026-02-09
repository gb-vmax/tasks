# Bug Report

### Describe the bug

Inline code blocks (backtick-delimited text) are not rendering correctly when they contain spaces. The parser seems to be treating spaces differently than before, causing the code text to be broken up or terminated prematurely.

### Reproduction

```js
// Example markdown with inline code containing spaces
const markdown = 'This is `code with spaces` in it';

// When parsed, the inline code block is not handled correctly
// The spaces inside the backticks cause unexpected behavior
```

Try parsing markdown with inline code that has spaces:
```
`hello world`
`foo bar baz`
```

The code blocks should preserve the spaces inside, but they're being processed incorrectly.

### Expected behavior

Inline code blocks should preserve all characters including spaces. The text between backticks should be treated as literal code text regardless of whitespace.

For example:
- Input: `` `code with spaces` ``
- Expected: The entire string "code with spaces" should be captured as code text
- Actual: Spaces are causing issues with the tokenization

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
