# Bug Report

### Describe the bug

I'm experiencing an issue with directive attributes where multiple `class` attributes are being concatenated in the wrong order. When a directive has multiple class attributes, they appear in reverse order compared to how they're defined in the source.

### Reproduction

```markdown
:::directive{.first .second .third}
content
:::
```

The resulting class attribute becomes `"third second first"` instead of `"first second first"`.

### Expected behavior

The classes should be concatenated in the order they appear in the source, so the final class attribute should be `"first second third"`.

This seems to have started happening recently and is affecting how our styles are applied since CSS specificity depends on the order of classes in some cases.

---
Repository: /testbed
