# Bug Report

### Broken link detection showing incorrect message type

I'm encountering an issue with the broken links checker where the error message shows the wrong type of broken link. When I have broken anchors in my documentation, the error message says they are "links" instead of "anchors", and vice versa.

### Reproduction

When I build my site with a broken anchor link like this:

```md
[Click here](#non-existent-section)
```

The error message incorrectly reports it as a broken "link" instead of a broken "anchor".

Similarly, when I have an actual broken link to another page:

```md
[Go to page](/docs/missing-page)
```

It gets reported as a broken "anchor" instead of a broken "link".

### Expected behavior

The error message should correctly identify:
- Broken anchors (links with `#`) as "anchor" 
- Broken page links as "link"

This makes it confusing when trying to fix broken links because the error messages are backwards.

### Additional context

This seems to have started recently. The messages used to be correct before.

---
Repository: /testbed
