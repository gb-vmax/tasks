# Bug Report

### Describe the bug
When using `using` declarations in my code, the variable kind is not being tracked correctly. It seems like `using` declarations are being treated as `await using` declarations instead.

### Reproduction
```js
using resource = getResource();

// The resource is being treated as if it was declared with 'await using'
// instead of just 'using'
```

I noticed this when working with synchronous disposable resources. The declarator seems to be setting the wrong flags internally - both `isUsingDeclaration` and `isAsyncUsingDeclaration` appear to have incorrect values when I use a regular `using` statement.

### Expected behavior
Regular `using` declarations should be distinguished from `await using` declarations. The `isUsingDeclaration` flag should be `true` for `using` and `false` for `await using`, while `isAsyncUsingDeclaration` should be `false` for `using` and `true` for `await using`.

### Additional context
This affects how the variables are declared and could lead to incorrect disposal behavior for synchronous resources.

---
Repository: /testbed
