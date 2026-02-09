# Bug Report

### Describe the bug

The `getAncestors` function in the templating base extension is not working correctly. When trying to retrieve ancestor documents for a request, the function appears to be broken and likely returns an error or unexpected results.

### Reproduction

```js
// In a template tag or plugin
const ancestors = await models.request.getAncestors(currentRequest);
// This should return parent request groups and workspace
// but instead fails or returns incorrect data
```

### Steps to reproduce:
1. Use the templating system to access request ancestors
2. Call `models.request.getAncestors()` with a request object
3. The function doesn't work as expected

### Expected behavior

The function should return an array of ancestor documents (request groups and workspaces) for the given request, excluding the request itself.

### Additional context

This seems to have broken recently. The function was working fine before but now the code structure looks malformed. It appears there might be an issue with how the function is defined within the models object.

---
Repository: /testbed
