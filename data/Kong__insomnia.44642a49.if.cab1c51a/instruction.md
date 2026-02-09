# Bug Report

### Describe the bug

The `filterParameters` function appears to have duplicate return statements at the end of the function body. After the main function logic completes with a return statement, there's an additional unreachable return statement that will never execute.

### Reproduction

Looking at the code structure:

```js
export function filterParameters(parameters, name, options) {
  // ... validation logic
  
  // ... pattern matching logic with return
  
  // ... case insensitive logic with return
  
  return parameters.filter(h => (!h || !h.name ? false : h.name === name));
}

  return parameters.filter(h => (!h || !h.name ? false : h.name === name));
}
```

The second return statement is outside the function scope and will cause issues.

### Expected behavior

The function should have proper structure with only one return path for the default case, and the closing braces should be properly matched.

### System Info
- Package: @insomnia/insomnia
- File: packages/insomnia/src/plugins/context/request.ts

---
Repository: /testbed
