# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with schema composition keywords (`allOf`, `anyOf`, `oneOf`), the generated request examples are incomplete. Properties that aren't marked as required are being excluded from the example output, even though they should be included to provide a complete representation of the schema.

### Reproduction

Given a Swagger 2.0 spec with the following schema:

```json
{
  "parameters": [{
    "in": "body",
    "schema": {
      "allOf": [
        {
          "properties": {
            "id": { "type": "string" },
            "name": { "type": "string" }
          },
          "required": ["id"]
        },
        {
          "properties": {
            "email": { "type": "string" }
          }
        }
      ]
    }
  }]
}
```

When importing this spec, the generated example only includes the `id` field, but both `name` and `email` are missing from the example even though they are valid properties of the schema.

Similarly, for schemas using `anyOf` or `oneOf`, only required properties from the first schema are being included in the generated examples.

### Expected behavior

All properties defined in the schema should be included in the generated examples, not just the required ones. This would provide users with a complete template showing all available fields they can use in their requests.

### Additional context

This issue affects the usability of imported Swagger specs, as users won't see all available fields they can send in their API requests. The examples should be comprehensive to serve as proper documentation.

---
Repository: /testbed
