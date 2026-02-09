# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with numeric parameters that have constraints like `minimum`, `maximum`, `multipleOf`, `exclusiveMinimum`, or `exclusiveMaximum`, the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of the parameter's validation rules.

### Reproduction

Given a Swagger 2.0 spec with a numeric parameter like:

```json
{
  "name": "quantity",
  "in": "query",
  "type": "number",
  "minimum": 10,
  "maximum": 100
}
```

Or with exclusive bounds:

```json
{
  "name": "price",
  "in": "query",
  "type": "number",
  "minimum": 0,
  "exclusiveMinimum": true,
  "maximum": 1000
}
```

Or with multipleOf constraint:

```json
{
  "name": "step",
  "in": "query",
  "type": "number",
  "multipleOf": 5,
  "minimum": 0,
  "maximum": 50
}
```

When importing these specs, the generated example value is always `0`, even when `0` is outside the valid range (e.g., when `minimum: 10` or when `exclusiveMinimum: true` with `minimum: 0`).

### Expected behavior

The importer should generate example values that satisfy the parameter constraints:
- For parameters with `minimum` and `maximum`, generate a value within that range
- For parameters with `exclusiveMinimum: true`, generate a value strictly greater than the minimum
- For parameters with `exclusiveMaximum: true`, generate a value strictly less than the maximum
- For parameters with `multipleOf`, generate a value that is a valid multiple within the specified range

This would make the imported requests immediately valid and usable without manual adjustments.

---
Repository: /testbed
