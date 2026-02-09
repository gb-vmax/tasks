# Bug Report

### Describe the bug

Inline code blocks with backticks are not being parsed correctly. When I try to use inline code in my markdown text, it's not being recognized as code at all.

### Reproduction

```js
const markdown = `This is \`inline code\` in text`;
// Parse the markdown
const result = processor.processSync(markdown);
```

The inline code with single backticks is not being tokenized properly. It seems like the backtick sequences aren't being detected or matched correctly.

### Expected behavior

Inline code wrapped in backticks should be properly recognized and parsed as code text. For example:
- `` `code` `` should parse as inline code
- ``` ``code`` ``` should also work for double backticks
- The opening and closing backtick sequences should match

### Additional context

This appears to have broken recently. Previously inline code was working fine, but now it's just being treated as regular text. The backtick characters are showing up in the output instead of being processed as code delimiters.

---
Repository: /testbed
