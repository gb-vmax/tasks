# Bug Report

### Describe the bug

I'm encountering an issue with inline code handling in MDX. When using inline code (backticks) in my MDX content, it's being parsed incorrectly and the output is not what I expect.

### Reproduction

```mdx
This is some text with `inline code` in it.
```

When this is processed, the inline code element seems to have the wrong structure. Instead of being treated as inline code, it appears to be handled as a code block or has an undefined value.

### Expected behavior

Inline code wrapped in single backticks should be parsed as `inlineCode` type nodes with a proper string value. The rendered output should display the code inline with the surrounding text.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

Has anyone else run into this? It seems like inline code blocks are not being processed correctly.

---
Repository: /testbed
