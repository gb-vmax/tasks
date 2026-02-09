# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with object parameters that have `required` properties defined, the generated examples are not respecting the required constraint. All properties are being included in the example object regardless of whether they're marked as required or not.

### Reproduction

Given a Swagger 2.0 spec with an object parameter like this:

```yaml
parameters:
  - name: user
    in: body
    schema:
      type: object
      required:
        - username
        - email
      properties:
        username:
          type: string
        email:
          type: string
        phone:
          type: string
        address:
          type: string
```

When importing this spec, the generated example includes all properties (username, email, phone, address) instead of just the required ones (username, email).

### Expected behavior

The generated example should only include the required properties when the `required` constraint is specified. Optional properties should be excluded from the example unless needed to satisfy `minProperties` constraint.

For the example above, the generated object should only contain:
```json
{
  "username": "",
  "email": ""
}
```

### Additional context

This affects the quality of generated examples and can be confusing when working with APIs that have many optional fields. The examples should be minimal and focus on required fields to provide clearer guidance.

---
Repository: /testbed
