# Bug Report

### Describe the bug

I'm experiencing an issue with link and image reference parsing in MDX. When using collapsed reference-style links or images (e.g., `[label][]` or `![alt][]`), the parser seems to be skipping tokens or not processing them correctly. The output is malformed and some content appears to be missing or incorrectly merged.

### Reproduction

```markdown
This is a [collapsed link][] in the text.

Another example with ![collapsed image][].

[collapsed link]: https://example.com
[collapsed image]: /image.png
```

When parsing the above MDX content, the resulting output doesn't render the references properly. It looks like the token processing is off by one or something similar - characters that should be part of the link/image syntax are appearing in the regular text, or the opposite is happening where regular text is being consumed as part of the reference syntax.

### Expected behavior

Collapsed reference-style links and images should be parsed correctly, with all tokens properly identified and processed. The syntax should resolve to the correct link/image elements without any adjacent content being incorrectly included or excluded.

### Additional context

This appears to affect both `labelLink` and `labelImage` token types. The issue manifests when the parser tries to clean up or transform these tokens during the resolution phase.

---
Repository: /testbed
