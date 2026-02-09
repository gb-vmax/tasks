# Bug Report

### Describe the bug

The `removeSuffix` utility function is not removing suffixes correctly. When trying to remove a suffix from a string, the last character of the suffix is being left behind in the result.

### Reproduction

```js
import { removeSuffix } from '@docusaurus/utils';

// Expected: "hello"
// Actual: "hellod"
console.log(removeSuffix("helloworld", "world"));

// Expected: "test"
// Actual: "test."
console.log(removeSuffix("test.md", ".md"));
```

### Expected behavior

The function should completely remove the specified suffix from the string. For example, `removeSuffix("helloworld", "world")` should return `"hello"`, not `"hellod"`.

### Additional context

This seems to have started happening recently. The function appears to be leaving the last character of the suffix in the output string instead of removing the entire suffix.

---
Repository: /testbed
