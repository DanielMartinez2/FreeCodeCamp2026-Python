def add_setting(settings, option):
    key, value = option
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:    
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, option):
    key, value = option
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings.items():
        return 'No settings available.'
    else:
        text = 'Current User Settings:\n'
        for key, value in settings.items():
            text += f"{key.capitalize()}: {value}\n"
        return text    
test_settings = {
    'theme': 'dark',
    'volume': 'high',
    
}