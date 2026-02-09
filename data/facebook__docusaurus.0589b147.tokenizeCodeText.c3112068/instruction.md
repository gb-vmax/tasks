# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When using backticks in inline code blocks, the parser seems to be handling nested or multiple backticks incorrectly. Specifically, when I have inline code that contains backticks or when the opening and closing backtick sequences are of different lengths, the parsing doesn't work as expected.

### Reproduction

```markdown
This is `code with ` backtick` inside

Or this: ``code with `backtick` inside``

Also: ```multiple backticks``` should work
```

When parsing the above markdown, the inline code blocks are not being recognized correctly. The parser seems to be treating backticks within the code content as potential delimiters even when they shouldn't be.

### Expected behavior

Inline code blocks should:
1. Allow backticks within the code content when using multiple backticks as delimiters (e.g., `` `backtick` ``)
2. Properly match opening and closing backtick sequences of the same length
3. Not terminate early when encountering backticks that are part of the code content

The standard markdown spec allows for this kind of nesting by using multiple backticks as delimiters.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
