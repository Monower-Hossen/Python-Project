from plyer import notification

notification.notify(
    title='Hello!',
    message='This is a desktop notification.',
    app_name='My App',
    timeout=10  # duration in seconds
)

#Install Plyer
#pip install plyer