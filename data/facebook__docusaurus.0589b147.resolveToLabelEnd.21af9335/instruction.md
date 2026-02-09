# Bug Report

### Describe the bug
I'm encountering an issue with markdown link/image parsing where the label text boundaries are being calculated incorrectly. This results in parts of the link text being cut off or improperly parsed.

### Reproduction
When parsing markdown with links or images, the text content within the label is not being captured correctly. For example:

```markdown
[link text here](url)
```

or

```markdown
![image alt text](image-url)
```

The parser seems to be off by one position when determining where the label text starts and ends, causing the text to be truncated or incorrectly delimited.

### Expected behavior
The full label text should be preserved and parsed correctly. All characters within the brackets should be included in the label text node.

### Additional context
This appears to be related to how the event positions are being calculated when resolving label boundaries. The offset calculations for determining the start and end positions of the label text seem incorrect.

---
Repository: /testbed
