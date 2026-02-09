# Bug Report

### Describe the bug

I'm encountering an issue where parsing markdown content that ends abruptly (without proper line breaks or at EOF) causes unexpected behavior. The parser seems to be attempting to process data tokens even after encountering a null code point, which leads to errors or incorrect parsing results.

### Reproduction

```js
// When parsing markdown that ends with text at EOF
const markdown = "Some text without trailing newline";
const result = remark.parse(markdown);

// Or when content ends abruptly
const content = "# Heading\nSome content";
const parsed = remark.process(content);
```

The parser appears to continue processing after reaching the end of input, resulting in malformed AST nodes or runtime errors.

### Expected behavior

The parser should gracefully handle end-of-file scenarios and properly terminate data token processing when encountering a null code point. The AST should be correctly formed regardless of whether the input ends with a line break or not.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
