# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality for gRPC/protobuf messages. When trying to generate mock data for message types, nested fields are not being populated correctly. The mock data generation seems to stop prematurely and returns empty objects for nested types.

### Reproduction

Given a protobuf definition with nested message types:

```protobuf
message User {
  string id = 1;
  Profile profile = 2;
}

message Profile {
  string name = 1;
  Address address = 2;
}

message Address {
  string street = 1;
  string city = 2;
}
```

When generating mock data for the `User` message, the nested `Profile` and `Address` fields are coming back as empty objects instead of being populated with mock values.

Expected output:
```json
{
  "id": "mock-id",
  "profile": {
    "name": "mock-name",
    "address": {
      "street": "mock-street",
      "city": "mock-city"
    }
  }
}
```

Actual output:
```json
{
  "id": "mock-id",
  "profile": {}
}
```

The nested fields are completely missing from the generated mock data. This makes it difficult to test requests that require nested message structures.

### System Info
- Insomnia version: latest main branch
- OS: macOS

---
Repository: /testbed
