# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX files where leading newlines are not being stripped correctly. After processing, code blocks retain their initial newline character, which causes unexpected whitespace at the beginning of the rendered code.

### Reproduction

```mdx
```js
const example = 'test';
```
```

When this MDX is processed, the resulting code value includes a leading newline:

```js
// Expected: "const example = 'test';"
// Actual: "\nconst example = 'test';"
```

### Expected behavior

Fenced code blocks should have both leading and trailing newlines removed during processing, similar to how most Markdown parsers handle code blocks. The code content should be clean without extra whitespace at the start or end.

### Additional context

This seems to affect all fenced code blocks regardless of the language specified. The trailing newlines appear to be handled correctly, but the leading ones are preserved in the output.

---
Repository: /testbed
