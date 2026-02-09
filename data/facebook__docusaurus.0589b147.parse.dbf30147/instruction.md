# Bug Report

### Describe the bug

The parser is throwing an error when trying to parse MDX content. It looks like something broke with the static `parse` method - getting errors about `this.parse` not being a function.

### Reproduction

```js
const Parser = require('remark-mdx');

const input = `
# Hello World

<Component prop="value" />
`;

// This throws an error
const result = Parser.parse(input, { sourceType: 'module' });
```

### Expected behavior

The parser should successfully parse the MDX input and return an AST without throwing errors.

### Additional context

This seems to have started happening recently. The parse method used to work fine but now it's failing with a TypeError. Not sure if this is related to a recent change or if I'm using it incorrectly, but the same code was working before.

---
Repository: /testbed
