# Bug Report

### Describe the bug

Inline code blocks with backticks are not being parsed correctly. When using multiple backticks to delimit inline code (e.g., ``` `` `code` `` ```), the parser seems to be exiting the code text sequence prematurely, causing the code content to not be recognized properly.

### Reproduction

```js
const markdown = '``code``';
// Parser fails to recognize this as inline code

const markdown2 = '```code```';
// This also doesn't work as expected
```

When trying to parse markdown with inline code that uses multiple backticks, the output is incorrect. The backticks are being processed but the code sequence isn't being handled right.

### Expected behavior

Inline code with multiple backticks should be parsed correctly. For example:
- ``` `code` ``` should recognize a single backtick as inline code
- ``` ``code`` ``` should recognize double backticks as inline code delimiters
- ``` ```code``` ``` should recognize triple backticks as inline code delimiters

The parser should consume all opening backticks before moving to the content between them.

### Additional context

This seems to have broken recently. Not sure what changed but inline code parsing is definitely not working as it should.

---
Repository: /testbed
