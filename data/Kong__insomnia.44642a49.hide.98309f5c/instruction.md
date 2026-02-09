# Bug Report

### Describe the bug

The "Parent Index" field for request template tags is not showing up when using `header` or `parameter` attributes with array notation in the name field. According to the functionality, when you specify a header or parameter name with array notation like `myHeader[0]` or `param[*]`, the index field should become visible to allow selecting a parent folder index, but it remains hidden.

### Reproduction

1. Create a request template tag
2. Set attribute to `header` or `parameter`
3. Enter a name with array notation, e.g., `Content-Type[0]` or `Authorization[*]`
4. The "Parent Index" field doesn't appear even though it should be available for indexed lookups

Expected: The "Parent Index" field should be visible when using array notation with headers or parameters, similar to how it works with the `folder` attribute.

### Current behavior

The index field only shows for `folder` attribute, but not for `header` or `parameter` attributes even when array notation is used in the name.

### Expected behavior

When using array notation in header/parameter names (e.g., `[0]`, `[1]`, `[*]`), the "Parent Index" field should be displayed to allow specifying which parent folder level to search in.

### System Info
- Insomnia version: latest

---
Repository: /testbed
