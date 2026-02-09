# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, boolean parameters are always being set to `true` regardless of their parameter name or context. This causes issues with parameters that semantically represent negative states (like `disabled`, `inactive`, `hidden`, etc.) which should logically default to `false`.

### Reproduction

Import a Swagger 2.0 specification with boolean parameters that have names suggesting a negative state:

```yaml
parameters:
  - name: disabled
    in: query
    type: boolean
  - name: isActive
    in: query
    type: boolean
  - name: hidden
    in: query
    type: boolean
```

After import, all these boolean parameters get example values of `true`, which doesn't make semantic sense for parameters like `disabled` or `hidden`.

### Expected behavior

Boolean parameters should have more intelligent defaults based on their names:
- Parameters like `disabled`, `inactive`, `hidden`, `closed`, `locked`, `deleted`, `archived`, `suspended` should default to `false`
- Other boolean parameters should default to `true`
- If `example` or `default` values are explicitly provided in the spec, those should be respected

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
