# Bug Report

### Describe the bug

I'm encountering an issue with link and image reference parsing in MDX. It seems like the parser is not correctly handling nested brackets in link/image labels, causing some valid markdown reference syntax to be rejected or parsed incorrectly.

### Reproduction

```markdown
Here's a link with nested brackets: [outer [inner] text][ref]

[ref]: https://example.com

And an image: ![alt [with] brackets][img-ref]

[img-ref]: /image.png
```

When I try to parse this MDX content, the references aren't being resolved properly. The parser seems to be treating balanced brackets incorrectly, which breaks valid reference-style links and images that contain nested brackets in their labels.

### Expected behavior

The parser should correctly handle nested brackets within link and image labels and properly match them with their corresponding reference definitions. Valid reference-style markdown should be parsed and rendered correctly.

### Additional context

This appears to be related to how the label tokenizer checks for balanced brackets. The issue manifests when using reference-style links/images with bracket characters in the label text itself.

---
Repository: /testbed
