# Bug Report

### Describe the bug

When using the automock functionality with protobuf types that have nested message fields, the mocking behavior is incorrect. Fields that should be populated with mock data are being skipped, resulting in incomplete mock objects.

### Reproduction

```js
// Define a protobuf message with nested fields
message User {
  string name = 1;
  Profile profile = 2;
}

message Profile {
  string bio = 3;
  Settings settings = 4;
}

message Settings {
  bool notifications = 5;
}

// When automocking the User type, nested fields are not being generated properly
const mockedUser = automock(UserType);

// Expected: mockedUser should have profile.settings populated
// Actual: Nested message fields are missing or empty
```

### Expected behavior

All nested message fields should be properly mocked with default values according to their types. The mock should recursively generate data for nested message structures unless a depth limit is reached.

### Additional context

This appears to affect nested message types specifically. Primitive fields and repeated fields seem to work as expected, but when a message field references another message type, the nesting isn't handled correctly.

---
Repository: /testbed
