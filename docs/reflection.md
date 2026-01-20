The SHA256 hashes provide cryptographic proof of file integrity, and matching hashes indicate the files are identical 
at the binary level. If the hashes are different then that means the contents of the file changed.

While analyzing the files and hashes I did notice that the hashes show redhat.txt and redhat_2.txt are identical, 
meaning no changes occurred between 11:00 AM and 11:10 AM.

The hashes between redhat_3.txt and redhat_4.txt differ from one another and to me that indicates when changes started
happening. 

According to my observations it's safe to say that malicious activity may have begun around 11:10am and possibly a worm
or other malware could have generated from the firewall event. It is also likely that the log file could have been 
altered, or deleted purposely. If this was some sort of evidence then that would be reason why the event would have
taken place.

This possible attack continued approximately up to 11:30

I think what could be added to the script could be maybe the amount of times each worm appeared and which log file
contain the worm activity.