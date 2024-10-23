def add_time(start, duration, day_of_week=None):
    # Days of the week
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Convert day_of_week to proper case (first letter capital)
    if day_of_week:
        day_of_week = day_of_week.lower().capitalize()

    # Split start time into components
    start_time, period = start.split()  # e.g., "3:00" and "PM"
    start_hour, start_minute = map(int, start_time.split(":"))  # e.g., 3 and 00

    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(":"))  # e.g., 3 and 10
    
    # Convert the start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Add duration hours and minutes to start time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60  # Carry over extra minutes to hours
    end_minute %= 60  # Keep minutes within 0-59

    # Calculate days passed
    days_later = end_hour // 24  # Every 24 hours is one day
    end_hour %= 24  # Keep hours within 0-23

    # Convert back to 12-hour format
    if end_hour == 0:
        final_hour = 12
        final_period = "AM"
    elif end_hour < 12:
        final_hour = end_hour
        final_period = "AM"
    elif end_hour == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = end_hour - 12
        final_period = "PM"
    
    # Format the time string
    new_time = f"{final_hour}:{end_minute:02d} {final_period}"

    # Handle day of the week
    if day_of_week:
        day_index = days_of_week.index(day_of_week)
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    
    # Handle days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

