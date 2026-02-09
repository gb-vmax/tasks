# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with array parameters that have `uniqueItems: true`, the generated example values are all identical instead of being unique. This makes it difficult to test APIs that require unique array elements.

### Reproduction

Given a Swagger 2.0 spec with an array parameter like this:

```yaml
parameters:
  - name: emails
    in: query
    type: array
    uniqueItems: true
    items:
      type: string
      format: email
```

The importer generates example values where all array elements are the same:
```
["user@example.com", "user@example.com", "user@example.com"]
```

### Expected behavior

When `uniqueItems: true` is specified, the generated examples should contain distinct values:
```
["user1@example.com", "user2@example.com", "user3@example.com"]
```

This should also work for other types like numbers, dates, and strings with different formats.

### Additional context

This affects API testing workflows where unique array values are required by the backend validation. Currently having to manually edit the generated examples every time I import the spec.

---
Repository: /testbed
