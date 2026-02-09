# Bug Report

### Describe the bug

I've encountered an issue with code fence parsing in MDX content. When using fenced code blocks with closing fence sequences, the parser is not correctly validating the fence markers, which causes incorrect parsing behavior.

### Reproduction

```mdx
# Example MDX file

```js
const example = "test";
```

More content here
```

The closing fence sequence (the three backticks after the code) should only close the code block if it matches the opening marker, but it seems like the parser is accepting any character sequence as a valid closing fence.

### Expected behavior

The parser should verify that the closing fence sequence uses the same marker character as the opening fence. If the markers don't match, it should continue treating the content as part of the code block rather than closing it prematurely.

For example:
- Opening with ` ``` ` should only close with ` ``` `
- Opening with `~~~` should only close with `~~~`
- Mismatched markers should not close the fence

### Additional context

This appears to be affecting the tokenization logic for fenced code blocks. The issue may cause MDX documents with certain code fence patterns to be parsed incorrectly, potentially breaking the rendered output.

---
Repository: /testbed
