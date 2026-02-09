# Bug Report

### Describe the bug

I'm experiencing an issue with identifier parsing in MDX files. It seems like valid JavaScript identifiers are not being recognized properly, causing parsing errors when they should be accepted.

### Reproduction

```js
// This MDX content fails to parse correctly
const myVariable = 123;
const _privateVar = 'test';
const $jquery = 'selector';
```

When trying to use these valid JavaScript identifiers in MDX content, they're not being parsed as expected. The parser seems to reject identifiers that should be valid according to ECMAScript 6+ specifications.

### Expected behavior

The parser should recognize all valid JavaScript identifiers, including:
- Variables starting with letters, underscores, or dollar signs
- Unicode escape sequences in identifiers
- Any identifier that's valid in ES6+

These should all be parsed without errors, just like they would be in regular JavaScript code.

### System Info
- MDX version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
