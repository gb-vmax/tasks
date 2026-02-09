# Bug Report

### Describe the bug

I'm encountering an issue with the automock functionality where the mock data generation seems to be inverted. When I try to generate mocks for gRPC service methods, I'm getting empty objects instead of properly mocked data with fields populated.

### Reproduction

```js
// Attempting to generate mock data for a gRPC service method
const mocked = mockMethodReturnType(
  root,
  serviceMethods,
  'GetUser',
  MethodType.request,
  true  // mocks enabled
);

// Expected: mocked.plain should contain generated mock data
// Actual: mocked.plain is an empty object {}
```

The behavior seems backwards - when mocks are explicitly enabled, I get empty objects. When I disable mocks (passing `false`), the system appears to try generating mock data (though that's not what I want).

### Expected behavior

When `mocks` parameter is `true`, the function should generate mock data by calling `mockTypeFields()` and populate the returned object with appropriate field values based on the protobuf message type definition.

When `mocks` is `false`, it should return empty objects.

### Additional context

This is affecting our ability to test gRPC services properly. Also noticed that the request/response type selection might be related - not sure if that's part of the same issue or separate.

---
Repository: /testbed
