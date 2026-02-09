# Bug Report

### Describe the bug

I'm experiencing an issue with nested MDX JSX tags where the parser seems to be losing track of tag context when processing deeply nested components. The tag stack appears to be getting corrupted, causing the parser to incorrectly associate closing tags with the wrong opening tags.

### Reproduction

```mdx
<Outer>
  <Middle>
    <Inner>
      Content here
    </Inner>
  </Middle>
</Outer>
```

When parsing this structure, the nested tags don't maintain their proper hierarchy. It seems like the tag stack isn't being properly managed when entering a new tag context.

### Expected behavior

The parser should correctly track the nesting level of JSX tags and maintain a proper stack so that closing tags match their corresponding opening tags, regardless of nesting depth.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
