# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX. When parsing code blocks, the content appears to be processed incorrectly, causing the parser to fail or produce unexpected output for certain code block patterns.

### Reproduction

```mdx
```js
const example = 'test';
console.log(example);
```
```

When this MDX content is parsed, the code block content doesn't render correctly or the parser throws an error during tokenization.

### Expected behavior

The fenced code block should be parsed correctly and the content should be preserved as-is without any parsing errors. The tokenizer should properly handle the code flow value tokens.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems to have started happening recently. The code block parsing was working fine before but now certain code patterns cause issues during the tokenization phase.

---
Repository: /testbed
