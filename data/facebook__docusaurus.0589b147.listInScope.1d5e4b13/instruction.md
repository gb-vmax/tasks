# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where certain markdown constructs are not being processed correctly. It seems like the scope checking logic is failing when multiple element types should be allowed in a context.

### Reproduction

When trying to parse markdown with specific nested structures, the parser incorrectly rejects valid content or allows invalid content depending on the list of allowed elements.

For example, when checking if elements are in scope with a list containing multiple allowed types:

```js
// This should return true if any element in the list is in scope
// but seems to be returning the fallback value incorrectly
const allowed = ['paragraph', 'heading', 'list'];
const result = listInScope(stack, allowed, false);
```

The behavior changes unexpectedly when the allowed list has exactly one element versus multiple elements.

### Expected behavior

The scope checking should correctly determine if any of the provided element types are in the current stack, regardless of how many element types are in the allowed list. A list with one element should behave the same as a list with multiple elements in terms of the checking logic.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
