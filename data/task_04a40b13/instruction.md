Hey, I need some help with a translation file I'm working on. I'm a localization engineer updating the French translation for our app, and I need to do two things quickly before submitting the file.

The translation file is at `/home/user/translations/fr.po`. It's a standard GNU gettext `.po` file. In this file, strings are represented as `msgid` / `msgstr` pairs. An untranslated string is one where `msgstr` is empty — meaning the line looks exactly like `msgstr ""` (with nothing between the quotes).

Here's what I need you to do:

**Step 1: Count the untranslated strings.**

Count how many entries have `msgstr ""` (an empty msgstr). This means the line matches exactly `msgstr ""` — not a multi-line continuation (those look like just `"..."` on their own line), just the lines that are literally `msgstr ""`.

Write the count to a new file at `/home/user/translations/untranslated_count.txt`. The file should contain exactly one line in this format:

```
Untranslated strings: <N>
```

Where `<N>` is the integer count. No trailing spaces, no extra blank lines — just that single line followed by a newline character.

**Step 2: Update the metadata in the `.po` file.**

The `.po` file has a header entry (the first `msgstr` block) that contains metadata lines. One of those metadata lines looks like this:

```
"X-Untranslated-Count: 0\n"
```

Update that line so the number reflects the count you just computed. It should become:

```
"X-Untranslated-Count: <N>\n"
```

Where `<N>` is the same count from Step 1. The rest of the file should remain completely unchanged.

Please make both of these changes for me.
</think>
