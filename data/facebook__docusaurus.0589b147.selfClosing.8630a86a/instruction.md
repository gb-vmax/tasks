# Bug Report

### Describe the bug

Self-closing JSX tags are not being handled correctly in MDX. When I use a self-closing tag with the proper syntax (ending with `/>` and then `>`), it's not being recognized and instead causes parsing errors or unexpected behavior.

### Reproduction

```mdx
<MyComponent />
```

When trying to use a standard self-closing JSX tag like the one above, the parser doesn't properly validate the closing sequence. It seems like the logic for checking the `>` character after the `/` is inverted.

### Expected behavior

Self-closing tags should parse correctly when they follow the standard JSX syntax of `/>`. The parser should:
1. Recognize the `/` character
2. Expect a `>` character immediately after
3. Successfully close the tag

Instead, it appears to be accepting invalid syntax and rejecting valid syntax.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
