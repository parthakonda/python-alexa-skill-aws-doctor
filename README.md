# AWS Doctor - Alexa skill service

The purpose of this skill service is to assist in starting and stopping aws services. This is an interactive way of doing with alexa.

# How to start skill?

    You:
        open aws doctor

    Alexa:
        Q - Welcome, This is aws doctor. Version 1.o. Which AWS account that you want to control?

    ... alexa listing for your command

    You:
        use environment {environment}
        or
        select environment {environment}
    (if you provide environment name something like `dev` or `prod` or any)
    Alexa:
        Taking {environment} environment, which service you want to control?

    (if you provide environment name something like `dev` or `prod` or any)
    Alexa:
        Q - Assuming dev environment, which service you want to control?

    ... alexa listening for your command

    You:
        use service {service}
        or
        select service {service}

    Alexa:
        Q - confirmed {service} service, what do you want to do?

    ... alexa listening for your command

    You:
        {action} service
        action: [stop | shutdown | pause | start | play | start]

    Alexa:
        S - Service started
        or
        S - Service stopped

# Tech stack

    Python 2.7
    flask-ask

# How to serve your app over public?

Use ngrok

    ./ngrok http 5000
