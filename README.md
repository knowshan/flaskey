**A tiny web app to add SSH public keys to authorized_keys file along with a command.**

This web app accepts SSH public keys from (authenticated) users and adds them to SSH_AUTH_KEY_FILE along with SSH_COMMAND value. The web app doesn't perform any user authentication, but instead relies on REMOTE_USER header passed by front-end server. The web app assumes that REMOTE_USER header is set by a web server after it's user authentication step (basic auth, Shibboleth, OAuth2 etc.).

**Use case**

SSH public key can be used to restrict user's action to a particular command. This feature can be used to allow users to execute a ceratin command on the system without giving them any system account. If SSH public keys can be associated with some other user/identity database, then that user/identity provider can be used to manage SSH public keys. For example, we can associate SSH public keys with a web application's users and restrict these public keys to allow users to SCP files to a particular directory without giving them any 'real' system account (they will use some shared account!). Real world examples using this technique are [Gitorius](https://groups.google.com/forum/?fromgroups=#!topic/gitorious/GsQDRidHBYs) and [gitosis](http://sitaramc.github.com/gitolite/glssh.html).

