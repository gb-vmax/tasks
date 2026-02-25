A configuration manager needs to verify that a given text configuration file, located at <code>/home/user/sample_config.txt</code>, which is currently encoded in UTF-8, has been correctly converted to ISO-8859-1 encoding. Please perform the conversion from UTF-8 to ISO-8859-1 and save the converted file as <code>/home/user/sample_config_iso8859-1.txt</code>.

After completing the conversion, generate a log file at <code>/home/user/encoding_conversion_log.txt</code> containing the following information in exactly two lines:

1. The line "Original Encoding: UTF-8"
2. The line "Converted Encoding: ISO-8859-1"

Please ensure there is **no extra whitespace** at the end of each line or in the log file. The automated test will verify both the encoding of the new file and the exact content/format of the log file.
