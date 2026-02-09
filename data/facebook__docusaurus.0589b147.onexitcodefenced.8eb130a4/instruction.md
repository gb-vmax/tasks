# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX files. When a fenced code block starts with a newline, the leading newline is being preserved in the output, which breaks the formatting of code examples.

### Reproduction

```mdx
```js

console.log('hello');
```
```

The code block above has a newline immediately after the opening fence. Currently, this leading newline is being included in the code block's value, resulting in unexpected blank lines at the start of rendered code.

### Expected behavior

Leading newlines after the opening fence of a code block should be stripped, just like trailing newlines before the closing fence are removed. The code content should start immediately without any leading blank lines.

For the example above, the expected output should be:
```
console.log('hello');
```

Instead of:
```

console.log('hello');
```

### Additional context

This affects the rendering of code blocks in documentation and makes it difficult to format MDX files in a readable way. The trailing newlines are already being stripped correctly, so it seems like the leading newline stripping might have been removed unintentionally.

---
Repository: /testbed
