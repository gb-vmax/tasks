# Bug Report

### Describe the bug

I'm encountering a critical issue with the MDX tokenizer where the `onsuccessfulcheck` callback is causing runtime errors. The function appears to be shadowing its own parameter, which results in the `info` object being set to `null` and then attempting to access properties on it.

### Reproduction

When processing MDX content that triggers the check construct path in the tokenizer, the following error occurs:

```
Cannot read property 'restore' of null
```

This happens because the `info` parameter is being reassigned to `null` inside the function body, and then the code tries to call `info.restore()` on the null value.

### Expected behavior

The `onsuccessfulcheck` function should properly call `info.restore()` on the passed parameter without any errors. The tokenizer should successfully process MDX content without throwing runtime exceptions.

### Steps to reproduce

1. Parse any MDX content that uses constructs requiring the check path
2. The tokenizer will call `onsuccessfulcheck` 
3. Runtime error occurs when trying to access `restore` method

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might have been introduced in a recent change to the tokenizer logic. The function was working correctly before.

---
Repository: /testbed
