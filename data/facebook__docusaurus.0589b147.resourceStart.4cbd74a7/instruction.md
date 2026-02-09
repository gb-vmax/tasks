# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where resource markers (the opening parenthesis in link syntax) are not being properly consumed/processed. When using standard markdown link syntax like `[text](url)`, the parser seems to be skipping the consumption of the opening parenthesis character, which causes the tokenization to fail or produce incorrect results.

### Reproduction

```markdown
[Link text](https://example.com)
```

When parsing the above markdown link, the opening parenthesis `(` of the resource part should be consumed as a token, but it appears to be skipped in the tokenization process. This results in malformed or incorrect parsing of the link structure.

### Expected behavior

The parser should properly tokenize the resource marker (opening parenthesis) by:
1. Entering the resource marker state
2. Consuming the `(` character
3. Exiting the resource marker state
4. Continuing to parse the rest of the resource (URL)

Instead, it seems like the consumption step is being skipped, causing the parser to not advance correctly through the input.

### System Info
- @mdx-js/mdx version: 3.0.0
- This affects standard markdown link syntax parsing

---
Repository: /testbed
