# Bug Report

### Describe the bug

The `toKebabCase` function is not handling camelCase and PascalCase strings correctly. It only replaces spaces with hyphens, but doesn't convert camelCase or PascalCase to kebab-case format.

### Reproduction

```js
import { toKebabCase } from './common/misc';

// Current behavior - doesn't convert camelCase
console.log(toKebabCase('myVariableName'));
// Expected: 'my-variable-name'
// Actual: 'myVariableName'

// Current behavior - doesn't convert PascalCase
console.log(toKebabCase('MyComponentName'));
// Expected: 'my-component-name'
// Actual: 'MyComponentName'

// Only spaces are converted
console.log(toKebabCase('my variable name'));
// Works as expected: 'my-variable-name'
```

### Expected behavior

The function should properly convert camelCase, PascalCase, snake_case, and space-separated strings to kebab-case format. It should also handle edge cases like multiple consecutive spaces/underscores and trim leading/trailing hyphens.

### Additional context

This is causing issues when generating CSS class names or HTML attributes from variable names that use camelCase or PascalCase conventions.

---
Repository: /testbed
