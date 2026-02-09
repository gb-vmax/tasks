# Bug Report

### Describe the bug
I'm experiencing an issue with image parsing in markdown. When using images in my markdown content, they're not being processed correctly - it seems like the parser is accessing the wrong node in the stack, causing images to be malformed or missing properties.

### Reproduction
```js
const markdown = `
![alt text](image.png "title")

Some text with ![inline image](photo.jpg)
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The image nodes have incorrect properties
// Expected: proper image node with url and title
// Actual: properties are deleted or wrong node is modified
```

### Expected behavior
Images should be parsed correctly with their URL, alt text, and title preserved. Both standalone and inline images should work as expected.

### Additional context
This seems to affect both image references and regular images. The logic for handling reference vs non-reference images appears to be inverted - properties are being deleted from the wrong type of image node.

---
Repository: /testbed
