# Bug Report

### Email parameter generation not working correctly in OpenAPI 3 importer

I'm experiencing an issue with the OpenAPI 3 importer where email parameters are not being generated properly. It seems like the importer is trying to create contextual email examples based on schema metadata, but this is causing problems.

### Reproduction

When importing an OpenAPI 3 spec with email parameters:

```yaml
parameters:
  - name: email
    in: query
    schema:
      type: string
      format: email
```

The importer appears to be attempting to extract context from the schema's title or description to generate more meaningful email examples (like `admin@example.com` or `support@example.com`), but this functionality doesn't seem to be working as expected.

### Expected behavior

Email parameters should consistently generate valid example values. The importer should fall back to a simple default like `user@example.com` when no context is available.

### Additional context

This appears to affect any OpenAPI spec that includes email format parameters. The issue seems related to how the `generateParameterExample` function handles the `string_email` type.

---
Repository: /testbed
