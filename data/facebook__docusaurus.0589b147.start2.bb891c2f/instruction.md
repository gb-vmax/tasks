# Bug Report

### Describe the bug

Links with angle brackets in MDX are not being parsed correctly. When I try to use a link destination wrapped in `<>`, the parser seems to be treating it as raw text instead of an enclosed link destination.

### Reproduction

```mdx
[link text](<https://example.com>)
```

The above syntax should create a valid link with the URL enclosed in angle brackets, but instead the parser is not recognizing the `<` character correctly and treating the destination as a raw string.

### Expected behavior

Links with angle bracket delimiters should be parsed as enclosed destinations. The syntax `[text](<url>)` is valid Markdown/MDX and should work the same as `[text](url)`, but with the advantage of allowing spaces and other special characters in the URL.

### Additional context

This affects any link that uses the angle bracket syntax for destinations. Regular links without angle brackets still work fine, but the enclosed variant is broken.

---
Repository: /testbed
