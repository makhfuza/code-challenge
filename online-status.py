statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Mike": "online"
}

def online_count(statuses):
    counter = 0
    for status in statuses.values():
        if status == 'online': counter += 1
    return counter

print(online_count(statuses))