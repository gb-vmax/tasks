# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX. When using backticks for inline code, the parser seems to be handling certain character sequences incorrectly, particularly around spaces and the backtick character itself.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
This is some text with \`inline code\` that should work.
`;

// The parser appears to be mishandling the logic for determining
// when to close the code text sequence
```

When parsing inline code blocks (text wrapped in backticks), the tokenizer doesn't correctly identify the closing backtick sequence. The conditions for checking whether a character is a backtick (code 96) appear to be inverted or incorrectly ordered.

### Expected behavior

Inline code wrapped in backticks should be properly tokenized with the opening and closing sequences correctly identified. The parser should:
1. Recognize the opening backtick(s)
2. Process the content between backticks
3. Correctly identify the closing backtick(s)

Currently, it seems like the logic for detecting backticks vs other characters is not working as intended, causing the tokenizer to fail at properly parsing inline code blocks.

### System Info
- @mdx-js/mdx version: 3.0.0
- Affected file: tokenizeCodeText function in the MDX vendor bundle

---
Repository: /testbed
