# Bug Report

### Describe the bug

I'm encountering an issue with nested brackets in directive labels. When using multiple levels of brackets (e.g., `[[text]]`), the parser doesn't handle them correctly and fails to parse the label.

### Reproduction

```markdown
:directive[outer [inner text] more]
```

When parsing directives with nested brackets like this, the label parsing breaks down. It seems like the bracket balance tracking isn't working as expected.

Another example that fails:

```markdown
:directive[[nested brackets]]
```

### Expected behavior

The parser should correctly handle nested brackets within directive labels, maintaining proper bracket balance and allowing reasonable nesting depth (up to the documented limit).

### Additional context

This appears to be related to how the bracket balance is being tracked during label parsing. The issue manifests when there are consecutive opening or closing brackets.

---
Repository: /testbed
