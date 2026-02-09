# Bug Report

### Describe the bug

When using the automock feature with GraphQL enums, the generated mock values are incorrect. Instead of returning the first enum value, it appears to be trying to access an undefined or incorrect enum value, which can cause the mocking to fail or return unexpected results.

### Reproduction

```graphql
enum Status {
  PENDING
  ACTIVE
  COMPLETED
}

type Query {
  status: Status
}
```

When automocking a query that returns this enum type, the mock generator doesn't return `PENDING` (the first value) as expected. Instead, it seems to be attempting to access a different index in the enum values, which may not exist or may return an incorrect value.

### Expected behavior

The automock should return the first enum value (`PENDING` in the example above) consistently. This is the most predictable behavior and matches what most developers would expect from an automocking system.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
