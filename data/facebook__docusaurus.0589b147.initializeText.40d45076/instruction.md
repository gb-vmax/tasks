# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain text content is not being processed correctly. It seems like the parser is getting stuck in an infinite loop or not properly handling text data when it encounters specific character sequences.

### Reproduction

When parsing MDX content with certain text patterns, the parser appears to consume characters incorrectly and doesn't exit the data state properly. This causes the output to be malformed or the parsing to hang.

Example MDX content that triggers the issue:
```mdx
This is some text content with special characters.

More text here that should be parsed normally.
```

The parser seems to be having trouble transitioning between text states, particularly when it encounters break points in the content.

### Expected behavior

The MDX parser should correctly process all text content and properly transition between parsing states. Text data should be consumed and exited appropriately without getting stuck or producing incorrect output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This appears to have started happening recently and is affecting our ability to parse standard MDX documents. Any help would be appreciated!

---
Repository: /testbed
