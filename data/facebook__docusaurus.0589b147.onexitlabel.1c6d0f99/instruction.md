# Bug Report

### Describe the bug

I'm encountering an issue with markdown link and image parsing where the children nodes are being assigned incorrectly. When parsing markdown that contains both links and images with labels, the node structure gets mixed up - links end up with `alt` text instead of `children`, and images get `children` instead of `alt` text.

### Reproduction

```js
// Parsing a markdown link like:
[link text](url)

// Results in the link node having:
// node.alt = "link text"  // Wrong! Should be in children
// node.children = undefined

// Similarly, parsing an image like:
![alt text](image.url)

// Results in the image node having:
// node.children = [...]  // Wrong! Should be alt text
// node.alt = undefined
```

### Expected behavior

- Link nodes should have their label text stored in `children` property
- Image nodes should have their label text stored in `alt` property

The node types are being checked but the assignment logic appears to be inverted, causing links and images to have their label content stored in the wrong properties.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
