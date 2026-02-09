# Bug Report

### Describe the bug

I'm experiencing an issue with parsing unquoted attribute values in directives. When an unquoted attribute value contains an equals sign (`=`), the parser incorrectly rejects it, even though equals signs should be valid characters in unquoted attribute values (as long as they're not at the start).

### Reproduction

```markdown
::directive{attribute=value=with=equals}
content
::
```

The parser fails to handle this correctly and doesn't parse the attribute value properly. The equals signs after the first one should be treated as part of the attribute value itself.

### Expected behavior

Unquoted attribute values should allow equals signs within them (just not as the first character). The attribute should be parsed as `attribute="value=with=equals"`.

According to the HTML spec, unquoted attributes can contain most characters except whitespace, quotes, `<`, `>`, `` ` ``, and `=` at the beginning. Equals signs in the middle of the value should be fine.

### Additional context

This seems to be related to how the `valueUnquoted` function validates characters. It's currently being too strict about what characters are allowed in unquoted attribute values.

---
Repository: /testbed
