# Bug Report

### Describe the bug

I'm experiencing an issue with string decoding in MDX content. When I have HTML entities or character references in my MDX files, they seem to be getting double-encoded instead of being properly decoded.

### Reproduction

```mdx
# Example MDX Content

This is a test with special characters: & < >

And some character references: &amp; &lt; &gt;
```

When this content is processed, the special characters `&`, `<`, and `>` are being escaped to `&amp;`, `&lt;`, and `&gt;` first, and then the decoding logic runs on top of that. This results in the output showing the escaped entities instead of the actual characters.

For example:
- Input: `&`
- Expected output: `&`
- Actual output: `&amp;`

The same happens with existing HTML entities - they get re-encoded before being decoded, which causes them to appear as literal text in the rendered output.

### Expected behavior

Special characters and HTML entities should be decoded correctly without double-encoding. The `&`, `<`, and `>` characters should either be left as-is or properly handled by the existing character escape/reference replacement logic, not pre-escaped before decoding.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
