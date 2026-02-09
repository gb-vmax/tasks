# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2.0 imports where integer parameters with constraints (minimum, maximum, multipleOf) are not generating example values that respect those constraints. The generated examples always default to 0, even when the parameter schema specifies boundaries or multiples.

### Reproduction

Import a Swagger 2.0 spec with the following parameter definition:

```yaml
parameters:
  - name: page
    in: query
    type: integer
    minimum: 1
    maximum: 100
    multipleOf: 5
```

The generated request example shows `page=0` instead of a valid value between 1-100 that's a multiple of 5 (like 5, 10, 15, etc.).

Similarly, for parameters with just minimum/maximum:
```yaml
parameters:
  - name: count
    in: query
    type: integer
    minimum: 10
    maximum: 50
```

The example still generates `count=0` which violates the minimum constraint.

### Expected behavior

Integer parameters should generate example values that respect:
- `minimum` and `maximum` boundaries
- `multipleOf` constraints
- `enum` values if specified

For the first example above, it should generate something like 5, 10, 15... up to 100.
For the second example, it should generate a value between 10 and 50.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

This makes it difficult to test APIs that have validation rules on integer parameters since the auto-generated examples are always invalid.

---
Repository: /testbed
