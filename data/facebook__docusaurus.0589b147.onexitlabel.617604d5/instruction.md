# Bug Report

### Describe the bug

I'm encountering an issue with link and image parsing in markdown content. When using reference-style links or images with labels, the parsed output is incorrect - links are getting the wrong content and images are having their alt text replaced with child nodes.

### Reproduction

```js
// Reference-style link
const markdown1 = '[link text][ref]';
const result1 = remark().parse(markdown1);
// Link node has incorrect children/alt assignment

// Reference-style image
const markdown2 = '![alt text][ref]';
const result2 = remark().parse(markdown2);
// Image node has incorrect children/alt assignment
```

### Expected behavior

- For reference-style links (`[text][ref]`), the link node should have the text as children
- For reference-style images (`![alt][ref]`), the image node should have the alt text in the `alt` property, not as children

Currently it seems like the logic is inverted - links are getting alt text and images are getting children nodes.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
