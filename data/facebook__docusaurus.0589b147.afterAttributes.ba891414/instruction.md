# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where inline directives (leaf directives) seem to be consuming all subsequent content on the same line instead of properly terminating. The parser appears to be stuck in an infinite loop or continuously consuming whitespace after the directive attributes.

### Reproduction

```markdown
:directive[label]{attr="value"} some text after the directive
```

When parsing the above markdown, the text "some text after the directive" is not being recognized as separate content. Instead, the directive parser seems to be consuming everything after the closing brace.

### Expected behavior

The directive should end after the attributes block, and any text following the directive on the same line should be parsed as normal inline content. For example:

```markdown
:directive[label]{attr="value"} regular text
```

Should parse as:
1. A directive node with label and attributes
2. Regular text content "regular text"

But currently, it appears the parser is not properly terminating the directive and continuing to consume content.

### Additional context

This seems to affect inline/leaf directives specifically. Container and text directives appear to work as expected. The issue manifests when there's content immediately following the directive on the same line.

---
Repository: /testbed
