# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX parsing. When I have a code fence without an info string (language identifier), the parser seems to hang or not properly exit the fence parsing state.

### Reproduction

```mdx
```
const code = 'hello';
```
```

When parsing the above MDX content with a fenced code block that has no language/info string specified, the parser doesn't handle it correctly. The code block should still be valid even without specifying a language.

### Expected behavior

Fenced code blocks without an info string should be parsed correctly, just like they work in standard Markdown. The parser should:
1. Recognize the opening fence
2. Process the code content
3. Properly close and exit the fence state

### Additional context

This seems to affect basic code blocks that don't specify a language. Code blocks with language identifiers (like ` ```javascript `) work fine, but plain ` ``` ` blocks cause issues.

---
Repository: /testbed
