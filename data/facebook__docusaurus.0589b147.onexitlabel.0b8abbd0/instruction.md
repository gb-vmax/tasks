# Bug Report

### Describe the bug

When parsing MDX content with reference-style links or images, the link/image nodes are not being properly populated with their children or alt text. The reference tracking (`inReference` flag) is being set before the node structure is fully updated, which causes the node lookup to target the wrong element in the stack.

### Reproduction

```mdx
[link text][ref]

[ref]: /url
```

or with images:

```mdx
![alt text][ref]

[ref]: /image.png
```

### Expected behavior

- For reference links: The link node should contain the link text as children
- For reference images: The image node should have the alt text properly set
- The parser should correctly identify which node in the stack to update

### Current behavior

The children/alt text are not being assigned to the correct node because the stack position is off by one when resolving the label.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
