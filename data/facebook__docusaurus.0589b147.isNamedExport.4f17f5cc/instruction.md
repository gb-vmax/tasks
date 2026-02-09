# Bug Report

### Describe the bug

I'm experiencing an issue with MDX table of contents (TOC) generation. It seems like the named export detection is behaving incorrectly - exports that should be recognized as TOC exports are being ignored, and vice versa.

### Reproduction

When I have an MDX file with a custom TOC export like this:

```mdx
export const toc = [
  {value: 'Heading 1', id: 'heading-1', level: 2}
];

## Heading 1
Some content here
```

The custom TOC export is not being recognized properly. The behavior seems backwards - it's either accepting exports it shouldn't or rejecting valid ones.

### Expected behavior

The loader should correctly identify when a file has a named export matching the TOC export name (default is `toc`) and use it accordingly. Valid TOC exports should be detected and invalid ones should be ignored.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
