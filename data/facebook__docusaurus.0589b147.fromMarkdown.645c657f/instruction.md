# Bug Report

### Describe the bug

When calling `fromMarkdown()` with only 2 arguments (value and options object), the function doesn't work correctly. The options parameter gets misassigned to the encoding parameter instead, causing the markdown parsing to fail or behave unexpectedly.

### Reproduction

```js
const markdown = '# Hello World\n\nThis is a test.';
const options = { 
  // some parsing options
};

// This doesn't work as expected - options are ignored
const result = fromMarkdown(markdown, options);
```

### Expected behavior

When passing an options object as the second parameter (without an explicit encoding string), the function should correctly recognize it as options and use default encoding. The markdown should be parsed according to the provided options.

### Additional context

This seems to affect cases where you want to pass options but don't need to specify encoding explicitly. The function signature suggests it should handle this case with optional encoding parameter, but currently the parameter assignment logic appears to be reversed.

---
Repository: /testbed
