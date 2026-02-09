# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX files where trailing newlines are not being stripped correctly. The code block content appears to retain trailing whitespace/newlines when it should be removed.

### Reproduction

```mdx
```js
console.log('test');

```
```

When processing the above MDX content, the resulting code block value includes the trailing newline character at the end, which shouldn't be there based on the expected behavior.

### Expected behavior

Fenced code blocks should have both leading AND trailing newlines/carriage returns stripped from their content. Currently only the leading newlines are being removed, but the trailing ones remain in the output.

For example, a code block like:
```
```
code here

```
```

Should result in just `"code here"` without any trailing newline characters.

### Additional context

This seems to affect the rendering of code blocks in MDX documents. The extra trailing whitespace can cause issues with syntax highlighting and code formatting in the final output.

---
Repository: /testbed
