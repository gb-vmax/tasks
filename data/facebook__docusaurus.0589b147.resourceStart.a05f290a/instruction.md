# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where the resource token is being closed prematurely. When processing markdown links with resources (like `[text](url)`), the parser appears to be exiting the "resource" state too early in the tokenization process.

### Reproduction

```mdx
[Click here](https://example.com)
```

When parsing the above link, the resource tokenizer exits the "resource" state immediately after consuming the opening parenthesis `(`, before actually processing the URL content. This causes the rest of the link resource to be parsed incorrectly.

### Expected behavior

The "resource" state should remain active while parsing the entire URL portion of the link, including whitespace handling and the actual URL content. The resource should only be exited after the complete resource has been tokenized, not immediately after the opening marker.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
