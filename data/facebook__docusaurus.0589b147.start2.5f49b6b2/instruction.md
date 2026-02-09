# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where certain characters are being incorrectly treated as angle bracket delimiters for URLs. It seems like the parser is now accepting characters that shouldn't trigger the "enclosed URL" syntax (like `<url>`).

### Reproduction

When trying to parse MDX content with links, characters with ASCII codes less than or equal to 60 (which includes many valid characters like digits, some punctuation, etc.) are being treated as if they were the opening angle bracket `<` (ASCII 60).

For example:
```markdown
[link](5example.com)
[link](9test.org)
[link](:url.com)
```

These should be parsed as raw URLs, but instead they're being processed as if they started with `<`, leading to unexpected parsing behavior.

### Expected behavior

Only the actual `<` character (ASCII code 60) should trigger the enclosed URL syntax. Other characters with lower ASCII values should be processed as part of raw URLs or rejected appropriately based on the markdown spec.

The condition should specifically check for the `<` character, not for any character with an ASCII value less than or equal to 60.

### Additional context

This appears to affect URL parsing in link destinations within MDX documents. The issue likely impacts any links that might start with certain ASCII characters in the range below 60.

---
Repository: /testbed
