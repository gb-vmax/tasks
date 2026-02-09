# Bug Report

### Describe the bug

After a recent update, the `getName()` method in the request context is returning unexpected results. The method appears to be broken and not returning the request name properly.

### Reproduction

```js
// When calling getName() on a request context
const requestContext = context.request;
const name = requestContext.getName();

// The function doesn't return the expected name
```

### Expected behavior

The `getName()` method should return the request name as it did before. It should simply return `renderedRequest.name` without any additional processing or transformations.

### System Info
- Insomnia version: latest
- OS: Various

### Additional context

This seems to have broken after some changes to the request context plugin. The method used to work correctly but now it's not functioning as expected. Looking at the code, there seems to be a syntax/structural issue with how the `getName()` method is defined.

---
Repository: /testbed
