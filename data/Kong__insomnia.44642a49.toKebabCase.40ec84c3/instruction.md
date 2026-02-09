# Bug Report

### Describe the bug

The `toKebabCase()` function is not handling camelCase and PascalCase strings correctly. It only replaces spaces with hyphens but doesn't convert uppercase letters to lowercase with hyphens as expected for proper kebab-case formatting.

### Reproduction

```js
import { toKebabCase } from './common/misc';

// Current behavior - only handles spaces
console.log(toKebabCase('hello world')); // 'hello-world' ✓
console.log(toKebabCase('HelloWorld')); // 'HelloWorld' ✗ (should be 'hello-world')
console.log(toKebabCase('myVariableName')); // 'myVariableName' ✗ (should be 'my-variable-name')
console.log(toKebabCase('someAPIKey')); // 'someAPIKey' ✗ (should be 'some-api-key')
```

### Expected behavior

The function should properly convert camelCase, PascalCase, snake_case, and other formats to kebab-case:
- `'HelloWorld'` → `'hello-world'`
- `'myVariableName'` → `'my-variable-name'`
- `'someAPIKey'` → `'some-api-key'`
- `'my_variable_name'` → `'my-variable-name'`

This is causing issues when generating CSS class names or HTML attributes from JavaScript variable names, as they're not being properly converted to the expected kebab-case format.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
