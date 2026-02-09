# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where nested JSX components cause a crash. The parser throws an error when trying to process JSX tags, even with simple nesting.

### Reproduction

```mdx
<Component>
  <NestedComponent>
    Content here
  </NestedComponent>
</Component>
```

When parsing the above MDX content, the application crashes with an error about `mdxJsxTagStack` being undefined. This happens specifically when there are nested JSX tags in the MDX file.

### Expected behavior

The parser should correctly handle nested JSX components without throwing errors. The tag stack should be properly initialized before attempting to push tags onto it.

### Additional context

This appears to be a regression - previously working MDX files with nested components now fail to parse. The issue seems to occur during the initial parsing phase when the first JSX tag is encountered.

---
Repository: /testbed
