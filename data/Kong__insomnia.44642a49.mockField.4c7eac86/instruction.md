# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality where deeply nested protobuf fields are causing unexpected behavior. When mocking fields that have circular references or deep nesting, the function seems to return incorrect values or gets stuck in infinite recursion.

### Reproduction

```js
// When mocking a protobuf message with nested fields
const mockData = mockField(myNestedField, stackDepth);

// Expected: Should return an empty object when max depth is reached
// Actual: Returns something else entirely

// Also, when a field has a null scalar value:
// Expected: Should resolve and mock the field recursively
// Actual: The logic seems inverted - it only resolves when the value is NOT null
```

### Expected behavior

1. When the stack depth exceeds the maximum allowed depth, the function should return an empty object `{}` to prevent infinite recursion
2. When `mockScalar` returns `null` (indicating a complex type that needs further resolution), the field should be resolved recursively
3. When `mockScalar` returns a non-null value (a primitive), that value should be returned directly

### Current behavior

The automock function appears to have inverted logic in two places:
- When max depth is reached, it's not returning the expected empty object
- The null check for `mockPropertyValue` seems to be doing the opposite of what's intended

This is causing issues when trying to generate mock data for complex protobuf schemas with nested message types.

### System Info
- Insomnia version: latest
- OS: Not relevant to this issue

---
Repository: /testbed
