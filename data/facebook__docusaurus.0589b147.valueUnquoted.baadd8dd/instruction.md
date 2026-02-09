# Bug Report

### Describe the bug

I'm encountering an issue with unquoted attribute values in directives. When an unquoted attribute value contains a pipe character (`|`), the attribute parsing terminates prematurely instead of treating the pipe as part of the value.

### Reproduction

```markdown
::directive{attr=value|with|pipes}
```

When parsing this directive, the attribute value gets cut off at the first pipe character instead of reading the full `value|with|pipes` string.

### Expected behavior

The pipe character (`|`) should be treated as a valid character in unquoted attribute values, similar to how other special characters are handled. The full attribute value including pipes should be parsed correctly.

### Additional context

This seems to affect any directive with unquoted attributes that contain pipe characters. Using quoted values works as a workaround:

```markdown
::directive{attr="value|with|pipes"}
```

But unquoted values should also support pipes unless there's a specific reason to exclude them.

---
Repository: /testbed
