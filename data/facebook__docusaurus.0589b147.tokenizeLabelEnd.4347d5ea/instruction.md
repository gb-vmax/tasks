# Bug Report

### Describe the bug

I'm experiencing an issue with nested link/image parsing in MDX content. When I have nested links or images in my markdown, they're not being parsed correctly - the parser seems to be matching the wrong opening and closing brackets.

### Reproduction

```markdown
[[link text](url)](outer-url)
```

or with images:

```markdown
[![alt text](image.png)](link-url)
```

The parser is incorrectly handling the bracket balancing for these nested structures. It appears to be matching brackets that should already be considered "balanced" or paired up.

### Expected behavior

Nested links and images should be parsed correctly. The parser should properly track which opening brackets have already been matched with their corresponding closing brackets, and not try to re-use them for outer link/image structures.

For example, `[![alt text](image.png)](link-url)` should parse as an image inside a link, with proper nesting.

### Additional context

This seems to have broken recently. The bracket matching logic appears to have been inverted - it's now selecting brackets that are already balanced instead of unbalanced ones, which causes the nesting to fail.

---
Repository: /testbed
