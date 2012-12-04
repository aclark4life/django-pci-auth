======================
Notes
======================

Django-axes
-----------

Logs the attempts to login. It has a record for each bad attempt, and one record for all good attempts.
if you hit the limit of bad attempts it locks you out. If you login successfully
it will remove your previous bad attempts, and leave you with just the good attempts.

Takeaways - This doesn't store a log of all login attempts over time, because it deletes the bad attempts once a good one is found.

Models
~~~~~~

- AccessAttempt
    - user_agent
    - ip_address
    - username
    - trusted
    - get_data
    - post_data
    - http_accept
    - path_info
    - failures_since_start
    - attempt_time
    
Fields
~~~~~~
None


Django-passwords
----------------
django-passwords is a reusable app that provides a form field and validators that check the strength of a password.

Models
~~~~~~
None

Fields
~~~~~~
- PasswordField


django-brutebuster
------------------
BruteBuster is a simple, pluggable Django app that can help you protect against password bruteforcing attempts.

Models
~~~~~~

One record per username and IP combo, keeps track of the number of failed attempts, whenever a good one happens it resets the counter.

Takeaways - doesn't log the attempts anywhere. Also treats logins from different IP, different, so if someone was attacking from multiple sources (botnet), this would be a little harder to block.

What about multiple users from the same IP? No way to block that either.

Hasn't been updated since March 2011

- FailedAttempt
    - username
    - IP
    - failures
    - timestamp

Fields
~~~~~~
None

django-failedloginblocker
-------------------------
Looks similar to django-brutebuster but doesn't track IP's. Last updated March 2011

Models
~~~~~~

- FailedAttempt
    - username
    - failures
    - timestamp

Fields
~~~~~~
None

django-lockout
--------------
django-lockout is a cache-based Django app that locks out users after too many failed login attempts. Because django-lockout tracks login attempts in your site's cache, it is fast and lightweight. It is intended for Django sites where protection against brute force attacks is desired with no additional database overhead.

No models since it is cache based. Does require a cache to work. Doesn't persist the data for long term storage if you cache flushes you are lost.

I could see a potential issue if your cache isn't large enough, you could brute force a ton of requests, for the cache to fill, which would cause the cache to evict the list of blocked attempts and then you are allowed back in.. Haven't tested this, just a thought.
