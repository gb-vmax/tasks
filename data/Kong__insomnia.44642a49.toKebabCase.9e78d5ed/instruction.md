# Bug Report

### Describe the bug
The `toKebabCase` function is not converting strings to proper kebab-case format. It seems to only replace the first space and uses double dashes instead of single dashes.

### Reproduction
```js
import { toKebabCase } from './misc';

const input = 'hello world test';
const result = toKebabCase(input);

console.log(result);
// Expected: "hello-world-test"
// Actual: "hello--world test"
```

### Expected behavior
The function should replace all spaces with single dashes to create valid kebab-case strings. For example:
- `"hello world"` should become `"hello-world"`
- `"my test string"` should become `"my-test-string"`

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
