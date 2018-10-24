
# run script on any change

    fswatch . | xargs make apply

# only update when Javascript source modified

    fswatch --exclude='.*' --include='\.js$' . | xargs make apply

# INBOX

## how to get logs?

    kubectl logs -f hello-node-75cb5684b9-mq5hdhttps://runnable.com/docker/python/dockerize-your-pyramid-application
