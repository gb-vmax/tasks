# Bug Report

### Describe the bug

The markdown parser appears to be broken after a recent change. When trying to parse markdown content, the parser fails to process the input correctly and doesn't return any output or throws an error.

### Reproduction

```js
import {remark} from 'remark';

const markdown = `
# Hello World

This is a test document with **bold** text.
`;

const result = remark().processSync(markdown);
console.log(result); // Expected: parsed markdown tree, Actual: error or incomplete output
```

### Expected behavior

The parser should successfully tokenize and parse markdown content, returning a properly structured syntax tree. The tokenizer should be able to handle constructs and return states correctly.

### Additional context

This seems to affect the core tokenization logic. The parser is unable to complete processing even simple markdown documents. It looks like something in the construct factory handling might be incomplete or malformed.

---
Repository: /testbed
