# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript keywords are being accepted as valid identifiers when they shouldn't be. The parser is allowing reserved words like `class`, `function`, `return`, etc. to be used as variable names without throwing an error.

### Reproduction

```js
// This should throw an error but doesn't
const class = 'test';
const function = 'another test';
const return = 'value';

// These reserved words are being treated as valid identifiers
```

When trying to parse code that uses JavaScript keywords as identifiers, the parser doesn't raise the expected "Unexpected keyword" error. This is causing invalid JavaScript to be accepted as valid.

### Expected behavior

The parser should reject JavaScript keywords when used as identifiers and throw an error message like "Unexpected keyword 'class'" or similar. Reserved words should not be allowed as variable names in strict mode or when using older ECMAScript versions.

### Additional context

This seems to be affecting the keyword validation logic. The parser is incorrectly allowing reserved words to pass through validation instead of catching them during the parsing phase.

---
Repository: /testbed
