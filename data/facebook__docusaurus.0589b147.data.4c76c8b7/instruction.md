# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When I have inline code that contains spaces, the spaces seem to be getting lost or the code block is not being parsed correctly.

### Reproduction

```markdown
This is `code with spaces` in a sentence.
```

When parsing this markdown, the inline code block doesn't render properly. It seems like spaces within backticks are causing the parser to behave unexpectedly.

Another example:
```markdown
`hello world` should be inline code
```

The output is not what I expect - the spaces within the code block are not being handled correctly.

### Expected behavior

Inline code blocks (text wrapped in backticks) should preserve spaces and render as a single code element, regardless of how many spaces are inside the backticks.

For example:
- `` `code with spaces` `` should render as a single inline code block
- `` `a b c` `` should preserve all spaces between the letters
- `` `  leading spaces` `` should keep the leading spaces

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
