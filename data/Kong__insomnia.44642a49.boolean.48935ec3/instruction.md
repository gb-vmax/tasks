# Bug Report

### Describe the bug

After importing a Swagger 2.0 spec, boolean parameters in requests are being set to unexpected values based on their names or descriptions. Previously, all boolean parameters defaulted to `true`, but now they're being inferred from the parameter name/description which causes incorrect default values.

### Reproduction

When importing a Swagger spec with boolean parameters like:

```yaml
parameters:
  - name: isDisabled
    type: boolean
    description: "Whether the feature is disabled"
```

The generated request now has `isDisabled` set to `false` instead of `true`, presumably because the word "disabled" is in the name. This is problematic because:

1. The actual default value might be different from what's inferred
2. Parameter names don't always reflect their semantic meaning
3. This breaks existing imports that relied on the consistent `true` default

### Expected behavior

Boolean parameters should default to a consistent value (like `true`) or respect the `default` field from the spec if present. The parameter name/description shouldn't be used to guess the boolean value since it's unreliable and can lead to incorrect API calls.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
