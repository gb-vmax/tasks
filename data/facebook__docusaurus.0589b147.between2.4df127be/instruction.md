# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When I have inline code that contains backticks (`` ` ``), the parser seems to be incorrectly handling the code text sequence detection. The backtick character (code 96) is not being properly recognized, causing the inline code to either not be parsed correctly or to parse incorrectly.

### Reproduction

```markdown
This is `inline code` with text.
This is `code with backtick` inside.
```

When parsing markdown with inline code blocks, particularly those that might contain spaces or backticks, the tokenizer doesn't correctly identify where the code sequence ends.

### Expected behavior

The parser should correctly identify backtick sequences and properly tokenize inline code blocks, treating backtick characters (code 96) as the delimiters for code text sequences. Spaces after opening backticks should be handled correctly without breaking the parsing flow.

### Additional context

This appears to be related to the `tokenizeCodeText` function in the remark parser, specifically in how the `between2` function handles different character codes. The condition for checking backtick characters seems to be inverted or incorrect.

---
Repository: /testbed
