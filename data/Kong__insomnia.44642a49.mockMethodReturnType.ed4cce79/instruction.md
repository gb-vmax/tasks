# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality where method return values are not being generated correctly. When mocking methods, the return value structure seems to be broken - instead of getting both `plain` and `message` properties, I'm only receiving the data object directly.

### Reproduction

```js
// When calling a mocked method
const result = mockedService.someMethod();

// Expected: { plain: {...}, message: MessageType }
// Actual: just the plain data object
```

This appears to affect all mocked methods that should return the standard format with both plain data and message instances.

### Expected behavior

Mocked methods should return an object with two properties:
- `plain`: the raw data object
- `message`: the protobuf message instance created from the data

Instead, when mocking is enabled, only the plain data is returned without the wrapper object.

### System Info
- Insomnia version: latest main branch
- Platform: All platforms affected

---
Repository: /testbed
