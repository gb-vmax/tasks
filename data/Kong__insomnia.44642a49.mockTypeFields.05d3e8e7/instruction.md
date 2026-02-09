# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC automocking where nested message types are not being properly mocked. When a field references a nested message type, the mock data appears to be empty instead of containing the expected field structure.

### Reproduction

Given a protobuf definition like:

```protobuf
message User {
  string id = 1;
  Profile profile = 2;
}

message Profile {
  string name = 1;
  string email = 2;
}
```

When trying to automock a `User` message, the `profile` field comes back as an empty object `{}` instead of having the `name` and `email` fields populated with mock data.

Steps to reproduce:
1. Define a protobuf message with nested message types
2. Use the automock functionality to generate mock data
3. Observe that nested fields are empty

### Expected behavior

The automock should recursively generate mock data for all nested message types. In the example above, I would expect something like:

```json
{
  "id": "mock_string",
  "profile": {
    "name": "mock_string",
    "email": "mock_string"
  }
}
```

Instead, I'm getting:

```json
{
  "id": "mock_string",
  "profile": {}
}
```

This makes it difficult to test gRPC endpoints that rely on nested message structures.

---
Repository: /testbed
