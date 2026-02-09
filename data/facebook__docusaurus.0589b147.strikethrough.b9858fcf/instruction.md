# Bug Report

### Strikethrough elements rendering with wrong tag name

I'm experiencing an issue with strikethrough rendering in MDX. After a recent update, strikethrough text is being rendered with `<s>` tags instead of the expected `<del>` tags.

### Reproduction
```mdx
This is ~~strikethrough~~ text.
```

When this gets processed, it's now rendering as:
```html
<s>strikethrough</s>
```

But it should render as:
```html
<del>strikethrough</del>
```

### Expected behavior
Strikethrough syntax should consistently render using `<del>` tags, not `<s>` tags. The `<del>` tag is semantically correct for deleted/removed text and is what was being used before.

### Additional context
This seems to have changed in the latest version. The behavior was working correctly previously where strikethrough always used `<del>` tags. Now it appears to be using `<s>` tags by default, which changes the semantic meaning of the content.

---
Repository: /testbed
