# Bug Report

### Describe the bug

I'm encountering an issue with MDX link and image reference handling. When using reference-style links or images in MDX, the parser seems to be incorrectly processing the label content, causing links to render with their children in the wrong place or images to have their alt text assigned incorrectly.

### Reproduction

```mdx
[link text][ref]

[ref]: https://example.com

![alt text][img-ref]

[img-ref]: /image.png
```

When parsing the above MDX content, the link children and image alt text appear to be swapped or assigned to the wrong node types. Links are getting alt text treatment and images are getting children assignments.

### Expected behavior

- Reference-style links should have their label text properly assigned as children nodes
- Reference-style images should have their label text properly assigned as alt text
- The parser should correctly distinguish between link and image reference types

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken reference-style syntax which was working in previous versions. The content renders incorrectly or throws errors during compilation.

---
Repository: /testbed
