# Bug Report

### Describe the bug

When using the automock feature with GraphQL enums, I'm getting incorrect mock values generated. Instead of returning a valid enum value, the mocking seems to be producing unexpected results or errors.

### Reproduction

```graphql
enum Status {
  ACTIVE
  INACTIVE
  PENDING
}

type User {
  id: ID!
  status: Status!
}
```

When automocking a query that returns a `Status` enum field, the generated mock value doesn't match any of the valid enum values (ACTIVE, INACTIVE, PENDING). The behavior seems inconsistent and the mocked enum values are not what I'd expect.

### Expected behavior

The automock should return one of the valid enum values defined in the schema. For the `Status` enum above, it should return either "ACTIVE", "INACTIVE", or "PENDING" as the mocked value.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
