# Bug Report

### Describe the bug

The `toKebabCase` function is not converting strings to kebab-case correctly. It seems to be doing the opposite - converting kebab-case back to spaces and then only replacing the first space with a hyphen.

### Reproduction

```js
import { toKebabCase } from './common/misc';

// Expected: "hello-world-test"
// Actual: "hello world-test"
console.log(toKebabCase("hello world test"));

// Expected: "my-variable-name"
// Actual: "my variable name"
console.log(toKebabCase("my variable name"));
```

When I pass a string with multiple spaces, only the first space gets converted to a hyphen while the rest remain as spaces. This breaks any code that expects proper kebab-case formatting.

### Expected behavior

The function should convert all spaces in the input string to hyphens to produce valid kebab-case output.

For example:
- `"hello world"` should become `"hello-world"`
- `"my variable name"` should become `"my-variable-name"`
- `"test case example"` should become `"test-case-example"`

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
