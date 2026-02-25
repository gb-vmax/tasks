A recent security audit discovered that the translation file <code>/home/user/projects/i18n/en_US.po</code> contains potentially malicious HTML/JS code embedded in one of the message strings, which could lead to a cross-site scripting (XSS) vulnerability if not sanitized before use. As the localization engineer, identify the translation entry in <code>en_US.po</code> that contains a <code>&lt;script&gt;</code> tag, remove any potentially unsafe script tags from the message, and save the file with the sanitized content.

After updating the file, you must create a plain text log file at <code>/home/user/projects/i18n/update_log.txt</code>. This log should contain:

1. The date and time of your update in <b>YYYY-MM-DD HH:MM:SS</b> format (use the system’s local time).
2. The exact <b>msgid</b> of the translation that was sanitized.
3. The original (unsanitized) <b>msgstr</b> text from the file before your changes.
4. The sanitized <b>msgstr</b> as it appears after your changes.

Format your log exactly as below (replace &lt;...&gt; with the appropriate values):

<pre>
DATE: &lt;YYYY-MM-DD HH:MM:SS&gt;
MSGID: &lt;msgid value&gt;
ORIGINAL: &lt;original msgstr&gt;
SANITIZED: &lt;sanitized msgstr&gt;
</pre>
Be sure that the updated <code>en_US.po</code> file contains <b>no &lt;script&gt; tags in any msgstr values</b>.
