# Bug Report

### Describe the bug

The `toKebabCase` function is not handling camelCase and PascalCase strings correctly. It only replaces spaces with hyphens, but doesn't convert actual camelCase/PascalCase text to kebab-case format.

### Reproduction

```js
import { toKebabCase } from './common/misc';

// Expected: 'my-variable-name'
// Actual: 'myVariableName'
console.log(toKebabCase('myVariableName'));

// Expected: 'some-component-name'
// Actual: 'SomeComponentName'
console.log(toKebabCase('SomeComponentName'));

// Expected: 'hello-world'
// Actual: 'hello-world' (this one works)
console.log(toKebabCase('hello world'));
```

### Expected behavior

The function should properly convert camelCase and PascalCase strings to kebab-case, not just replace spaces. For example:
- `myVariableName` should become `my-variable-name`
- `SomeComponentName` should become `some-component-name`
- `HTTPSConnection` should become `https-connection`

It should also handle edge cases like multiple consecutive spaces, special characters, and leading/trailing hyphens.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
