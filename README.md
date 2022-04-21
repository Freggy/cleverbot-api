Cleverbot API
=============

This project provides a HTTP API to Cleverbot using headless browser fuckery so you don't need to use the official paid API. Igonre every python file but `api_new.py` in this project. It's a pet project I did a long time ago and I didn't want to clean it up. The Dockerfile is correct though.

Configuration
-------------

There are some environment variables you can set.

`CLEVERBOT_CACHE_MAX_SIZE`: The size of the session TTL cache 
`CLEVERBOT_CACHE_TTL`: How long a session should be kept in the cache

How to call the API
-------------------

Just curl it lmao

```
curl -H 'Session-Key: ThisIsMYSessionKey' http://localhost:1337/
```

The session key can be any arbitrary string. The server uses this to identify the correct Cleverbot session. Response looks like the following:

```json
{"response": "This is a message from Cleverbot"}
```

