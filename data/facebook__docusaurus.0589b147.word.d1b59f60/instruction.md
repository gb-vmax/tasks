# Bug Report

### Describe the bug

I'm having an issue with MDX import/export statements not being recognized properly. When I try to use `export` statements in my MDX files, they're not being parsed correctly and the content isn't rendered as expected.

### Reproduction

```mdx
export const metadata = {
  title: 'My Page'
}

# Hello World

This is my MDX content.
```

The export statement at the top doesn't seem to be processed correctly. The parser appears to skip over it or treat it as regular text instead of recognizing it as an ESM export.

### Expected behavior

The `export` statement should be recognized and parsed as valid ESM syntax in the MDX file. The metadata should be exported and the rest of the content should render normally.

### Additional context

This seems to have started recently. Import statements appear to work fine, but export statements are having issues. Not sure if this affects all export statements or just certain patterns.

---
Repository: /testbed
