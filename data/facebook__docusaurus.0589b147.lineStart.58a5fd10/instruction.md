# Bug Report

### Describe the bug

I'm experiencing an issue with parsing code blocks in markdown. When I have a code block that spans multiple lines, the parser seems to be incorrectly handling lazy continuation lines. The result is that some valid code blocks are not being recognized properly.

### Reproduction

```markdown
Some text before

    indented code block
    second line of code
    third line of code

Text after
```

When parsing this markdown, the indented code block doesn't get recognized correctly. It seems like the parser is treating continuation lines as lazy when they shouldn't be, or vice versa.

### Expected behavior

The indented code block should be parsed as a single code block node with all three lines included. The parser should correctly identify which lines are part of the code block and which are not.

### Additional context

This appears to be related to how the parser determines whether a line is a lazy continuation or not. The behavior changed recently and is now causing valid markdown to be parsed incorrectly.

---
Repository: /testbed
