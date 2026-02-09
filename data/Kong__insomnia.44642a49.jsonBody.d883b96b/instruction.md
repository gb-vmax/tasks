# Bug Report

### Describe the bug

I'm encountering an issue with the response validation methods in the SDK. When trying to validate JSON responses, the code appears to be incomplete or corrupted. The `to.not` object is missing the `jsonBody` property definition, and there seems to be a syntax error where the function implementation is cut off mid-statement.

### Reproduction

```js
const response = {
  body: '{"user": {"name": "test", "age": 25}}',
  // ... other response properties
};

// This should work but throws an error
pm.expect(response).to.not.jsonBody({ user: { name: "test" } });
```

When I try to use the `to.not.jsonBody()` method for negative assertions on response bodies, I get unexpected errors. It looks like the implementation got corrupted or wasn't properly merged.

### Expected behavior

The `to.not.jsonBody()` method should work properly for negative assertions, similar to how `to.not.status()`, `to.not.header()`, and `to.not.body()` work. The code should be complete and syntactically valid.

### Additional context

This seems to have broken recently. The code in the response.ts file shows that helper functions like `extractValueByPath` and `partialDeepEqual` were added but the actual `jsonBody` method definition in the `to.not` object is incomplete. There's a dangling `verify(actualValue,` statement that doesn't finish.

---
Repository: /testbed
