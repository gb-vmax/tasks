# Bug Report

### Describe the bug

I'm encountering an issue with markdown escaping in the remark library. Special characters that should NOT be escaped are getting escaped, while characters that SHOULD be escaped are not being escaped properly. This is causing markdown output to be incorrectly formatted.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Characters like '-' or '.' should be escaped in certain contexts
// but they're not being escaped when they should be

const input = 'Some text with special-characters.here';
const result = processor.stringify(ast);

// Expected: properly escaped special characters
// Actual: incorrect escaping behavior
```

### Expected behavior

Special characters that need escaping in markdown (like `|`, `\`, `{`, `}`, `(`, `)`, `[`, `]`, `^`, `$`, `+`, `*`, `?`, `.`, `-`) should be escaped with a backslash when necessary. Characters that don't need escaping should be left as-is.

The current behavior seems to have the logic inverted - it's escaping characters that shouldn't be escaped and not escaping ones that should be.

### Additional context

This appears to affect the `compilePattern` function in the markdown serialization logic. The pattern matching for determining which characters need escaping seems to be working backwards from what it should be.

---
Repository: /testbed
