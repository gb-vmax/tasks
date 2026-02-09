# Bug Report

### Describe the bug

The `toKebabCase` function is not handling camelCase and PascalCase strings correctly. It only replaces spaces with hyphens but doesn't convert camelCase/PascalCase to kebab-case format.

### Reproduction

```js
import { toKebabCase } from './common/misc';

// These don't work as expected
console.log(toKebabCase('myVariableName'));  // Expected: 'my-variable-name', Got: 'myvariablename'
console.log(toKebabCase('HTTPSConnection')); // Expected: 'https-connection', Got: 'httpsconnection'
console.log(toKebabCase('someAPIKey'));      // Expected: 'some-api-key', Got: 'someapikey'
```

The function currently only handles space replacement:
```js
toKebabCase('my variable name')  // Works: 'my-variable-name'
```

But it doesn't convert camelCase or PascalCase strings properly.

### Expected behavior

The function should convert various naming conventions to kebab-case:
- camelCase → kebab-case
- PascalCase → kebab-case  
- snake_case → kebab-case
- Handle consecutive uppercase letters (e.g., HTTP, API)
- Lowercase the output
- Trim leading/trailing hyphens

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
