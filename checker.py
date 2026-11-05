def has_em_dash(text):
    return "—" in text

TOOL_NAMES = ["book_appointment", "get_services", "check_availability"]

def find_tool_names(text):
    found = []
    for tool in TOOL_NAMES:
        if tool in text:
            found.append(tool)
    return found

print(has_em_dash("Sure — I can help with that."))
print(has_em_dash("Sure, I can help with that."))

print(find_tool_names("I'll call book_appointment for Friday."))
print(find_tool_names("Your facial is booked for Friday!"))
print(find_tool_names("Let me get_services and check_availability for you."))