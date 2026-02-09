# Bug Report

### Describe the bug
When prettifying JSON strings that contain Unicode escape sequences (like `\u0041`), the conversion is producing incorrect output. The converted characters are appearing in the wrong position in the resulting string.

### Reproduction
```js
import { prettifyJson } from './utils/prettify/json';

const jsonWithUnicode = '{"text": "Hello \\u0041 World"}';
const result = prettifyJson(jsonWithUnicode);

console.log(result);
// Expected: {"text": "Hello A World"}
// Actual: Characters are misplaced or string is malformed
```

The issue occurs when the JSON string contains Unicode escape sequences that should be converted to their corresponding characters. The prettified output has the converted characters in incorrect positions.

### Expected behavior
Unicode escape sequences like `\u0041` should be properly converted to their corresponding characters (e.g., 'A') and appear in the correct position within the string.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
