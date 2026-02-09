# Bug Report

### Describe the bug

I'm experiencing an issue with the automock functionality where deeply nested GraphQL schema fields are not being mocked correctly. When a schema has fields that reference other types recursively, the mocking seems to reset the depth tracking and generates much deeper object structures than expected.

### Reproduction

```graphql
type User {
  id: ID!
  name: String!
  friend: User
}

type Query {
  user: User
}
```

When automocking this schema, I would expect the recursion depth to be properly limited, but instead the mock generates deeply nested objects that go beyond the configured maximum depth. The `friend.friend.friend...` chain continues much deeper than it should.

### Expected behavior

The automock should respect the maximum stack depth configuration and return empty objects `{}` once the depth limit is reached. For example, with a max depth of 3, I would expect:

```json
{
  "user": {
    "id": "...",
    "name": "...",
    "friend": {
      "id": "...",
      "name": "...",
      "friend": {
        "id": "...",
        "name": "...",
        "friend": {}
      }
    }
  }
}
```

But instead, the nesting goes much deeper than configured.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
