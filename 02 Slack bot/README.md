# Slcak bot with python

## Basic setup with slack application

Fisrst of all, you need to log in on the [slack website](https://slack.com) or application and make a new workspace. Then the slack workspace will be created like below.

<img width="450" alt="image" src="https://user-images.githubusercontent.com/39740066/176777018-215f4f3c-1798-4031-8b3c-2493811e3ee1.png">

After that, we need to make new app on the [slack api](https://api.slack.com/) webpage. Enter your own application name and select workspace that you want to to use the application. I used name of ```first slack bot``` for application.

<img width="450" alt="image" src="https://user-images.githubusercontent.com/39740066/176777716-3f39d399-4ca1-456f-a49c-53654e2c3084.png">

Click ```Bots``` functionality section and chose ```Review scopes to add``` to control permissions of this application. On the ```Bot Token Scopes```, add ```Chat:write``` Oauth scope. And install Oauth tokens to authenticate your app connection, then you can copy OAuth token. If you add any other scope, reinstallation app should be done.

## Start python project setting

### 1. Add environment variable and install prerequisitions.
For building environmental variables, ```.env``` file is a best option. In this project, ```SLACK_TOKEN`` variable is needed for authentication. And we need to install ```slackclient``` package by using pip library. 

```bash
pip3 install slackclient
pip3 install python-dotenv
```

This [slackclient](https://pypi.org/project/slackclient/) PyPI project is in maintenance mode now and slack-sdk project is the successor. The v3 SDK provides more functionalities such as Socket Mode, OAuth flow module, SCIM API, Audit Logs API, better asyncio support, retry handlers, and many more. We can change into ```slack-sdk``` after our development finished. And also, ```python-dotenv``` should be installed because of using environmental variables.



## References
- https://www.youtube.com/watch?v=KJ5bFv-IRFM&list=PLzMcBGfZo4-kqyzTzJWCV6lyK-ZMYECDc
- https://pypi.org/project/slackclient/
- https://pypi.org/project/python-dotenv/
