# Bug Report

### Bug with `removePrefix` function not removing prefix correctly

I'm experiencing an issue with the `removePrefix` utility function where it's not removing the prefix as expected. Instead of removing the prefix from the beginning of the string, it seems to be doing something completely different.

### Reproduction

```js
import { removePrefix } from '@docusaurus/utils';

const result = removePrefix('hello-world', 'hello-');
console.log(result); // Expected: 'world', but getting unexpected output
```

When I call `removePrefix` with a string that starts with the given prefix, the prefix is not being removed. The function should strip the prefix from the start of the string and return the remainder.

### Expected behavior

The function should:
1. Check if the string starts with the given prefix
2. If yes, remove the prefix and return the rest of the string
3. If no, return the original string unchanged

For example:
- `removePrefix('hello-world', 'hello-')` should return `'world'`
- `removePrefix('goodbye', 'hello-')` should return `'goodbye'`

This seems like it might have been broken in a recent change. The function used to work correctly before.

---
Repository: /testbed
