# Bug Report

### Describe the bug

I'm encountering random errors when parsing markdown with directives. The parser throws "Validation failed" errors intermittently, making it impossible to reliably process markdown content.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkDirective = require('remark-directive');

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const markdown = `
:::note
This is a note directive
:::
`;

// This randomly throws "Validation failed" error
try {
  const result = processor.processSync(markdown);
  console.log('Success:', result);
} catch (error) {
  console.error('Error:', error.message);
}
```

### Expected behavior

The parser should consistently process markdown directives without throwing validation errors. The same input should always produce the same output.

### Additional context

This seems to happen randomly - sometimes the parsing works fine, other times it fails with the validation error. The behavior is non-deterministic which makes debugging very difficult.

---
Repository: /testbed
