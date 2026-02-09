# Bug Report

### Describe the bug

I'm experiencing an issue with JSX text parsing in MDX files. When using inline JSX components with attributes, the parser seems to be failing or not processing the attributes correctly. This appears to be related to how the tokenizer handles JSX text tags.

### Reproduction

```mdx
This is some text with an <InlineComponent attr="value" /> in the middle.
```

When parsing this MDX content, the inline JSX component's attributes are not being recognized or processed as expected. The component itself may render, but attribute values are lost or incorrectly parsed.

### Expected behavior

The inline JSX component should be parsed correctly with all its attributes preserved. The tokenizer should properly handle attribute names and values for JSX text tags (inline components).

### Additional context

This seems to have started happening recently. I'm using MDX with remark-mdx for parsing inline JSX components within text content. The issue specifically affects inline/text-level JSX tags rather than block-level ones.

---
Repository: /testbed
