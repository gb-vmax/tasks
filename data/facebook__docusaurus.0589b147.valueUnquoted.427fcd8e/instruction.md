# Bug Report

### Describe the bug

I'm experiencing an issue with parsing unquoted attribute values in directives. When an unquoted attribute value contains a backtick character (`` ` ``), it's being incorrectly rejected/not parsed properly. The parser seems to be treating backticks as invalid characters in unquoted attribute values.

### Reproduction

```markdown
::directive{attr=value`with`backtick}
```

When parsing the above directive, the attribute value should be parsed as `value`with`backtick`, but instead the parser appears to fail or not handle it correctly.

### Expected behavior

Backtick characters should be allowed in unquoted attribute values for directives. The parser should successfully consume the entire value including any backticks.

### Additional context

This seems to affect directives that use unquoted attribute values containing backticks. Quoted attribute values work fine as a workaround:

```markdown
::directive{attr="value`with`backtick"}
```

But it would be nice if unquoted values could support backticks as well since they're commonly used in code-related contexts.

---
Repository: /testbed
