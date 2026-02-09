# Bug Report

### Describe the bug
The `toKebabCase` function is not converting spaces to kebab-case format correctly. Instead of replacing spaces with hyphens (`-`), it's replacing them with underscores (`_`), and it only replaces the first space instead of all spaces in the string.

### Reproduction
```js
import { toKebabCase } from './common/misc';

const result = toKebabCase('hello world test');
console.log(result); // Expected: 'hello-world-test', Got: 'hello_world test'
```

### Expected behavior
The function should convert all spaces in a string to hyphens to produce proper kebab-case formatting. For example:
- `'hello world'` should become `'hello-world'`
- `'my variable name'` should become `'my-variable-name'`
- `'test case example'` should become `'test-case-example'`

Currently it's only converting the first space and using underscores instead of hyphens.

### System Info
- Version: latest
- OS: macOS

---
Repository: /testbed
