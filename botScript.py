# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# import csv
# from datetime import datetime
# import random


# options = webdriver.ChromeOptions()

# driver = webdriver.Chrome(options=options)
# driver.get('http://localhost:3000') 
# actions = ActionChains(driver)
# BOT_DATA_FILE = 'bot_interaction_log.csv'

# with open(BOT_DATA_FILE, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['timestamp', 'mouseMovements', 'avgTypingSpeed', 'clicks', 'keypresses', 'Result'])

# def simulate_mouse_movements():
#     x_offset = random.randint(-100, 100)
#     y_offset = random.randint(-100, 100)
#     actions.move_by_offset(x_offset, y_offset).perform()
#     return (x_offset, y_offset)

# def simulate_mouse_clicks():
#     actions.click().perform()

# def simulate_typing():
#     start_time = time.time()
#     actions.send_keys(random.choice('abcdefghijklmnopqrstuvwxyz')).perform()
#     end_time = time.time()
#     typing_speed = end_time - start_time
#     return typing_speed

# def log_bot_actions(mouse_movements, avg_typing_speed, clicks, keypresses):
#     timestamp = datetime.now().isoformat()
#     with open(BOT_DATA_FILE, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([timestamp, mouse_movements, avg_typing_speed, clicks, keypresses, 'Bot'])

# def run_bot_for_duration(duration_minutes):
#     start_time = time.time()
#     clicks = 0
#     keypresses = 0
#     mouse_movements_count = 0
#     typing_speeds = []

#     while time.time() - start_time < duration_minutes * 60:
#         mouse_movements_count += 1
#         mouse_movement = simulate_mouse_movements()

#         clicks += 1
#         simulate_mouse_clicks()

#         typing_speed = simulate_typing()
#         typing_speeds.append(typing_speed)
#         keypresses += 1

#         avg_typing_speed = sum(typing_speeds) / len(typing_speeds) if typing_speeds else 0
#         log_bot_actions(mouse_movements_count, avg_typing_speed, clicks, keypresses)

#         time.sleep(1) 
# run_bot_for_duration(10)

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import datetime
import random

# Setup WebDriver and Options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('http://localhost:3000')
actions = ActionChains(driver)
BOT_DATA_FILE = 'bot_interaction_log.csv'

# Initialize logging file
with open(BOT_DATA_FILE, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'mouseMovements', 'avgTypingSpeed', 'clicks', 'keypresses', 'Result'])

# Move mouse to the center of the window
def move_to_center():
    window_size = driver.get_window_size()
    center_x = window_size['width'] // 2
    center_y = window_size['height'] // 2
    actions.move_by_offset(center_x, center_y).perform()

# Function to simulate mouse movements
def simulate_mouse_movements():
    window_size = driver.get_window_size()
    current_x = window_size['width'] // 2
    current_y = window_size['height'] // 2

    x_offset = random.randint(-50, 50)
    y_offset = random.randint(-50, 50)

    new_x = current_x + x_offset
    new_y = current_y + y_offset

    # Ensure the new coordinates are within bounds
    if 0 <= new_x <= window_size['width'] and 0 <= new_y <= window_size['height']:
        actions.move_by_offset(x_offset, y_offset).perform()
        return (x_offset, y_offset)
    return (0, 0)  # Return no movement if out of bounds

# Function to simulate mouse clicks
def simulate_mouse_clicks():
    actions.click().perform()

# Function to simulate typing
def simulate_typing():
    start_time = time.time()
    actions.send_keys(random.choice('abcdefghijklmnopqrstuvwxyz')).perform()
    end_time = time.time()
    typing_speed = end_time - start_time
    return typing_speed

# Function to log bot actions
def log_bot_actions(mouse_movements, avg_typing_speed, clicks, keypresses):
    timestamp = datetime.now().isoformat()
    with open(BOT_DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, mouse_movements, avg_typing_speed, clicks, keypresses, 'Bot'])

# Main function to run the bot for a specific duration
def run_bot_for_duration(duration_minutes):
    start_time = time.time()
    clicks = 0
    keypresses = 0
    mouse_movements_count = 0
    typing_speeds = []

    # Move to the center at the start
    move_to_center()

    while time.time() - start_time < duration_minutes * 60:
        mouse_movements_count += 1
        mouse_movement = simulate_mouse_movements()

        clicks += 1
        simulate_mouse_clicks()

        typing_speed = simulate_typing()
        typing_speeds.append(typing_speed)
        keypresses += 1

        avg_typing_speed = sum(typing_speeds) / len(typing_speeds) if typing_speeds else 0
        log_bot_actions(mouse_movements_count, avg_typing_speed, clicks, keypresses)

        time.sleep(1)
        
# Run the bot for 10 minutes
run_bot_for_duration(10)

# Close the browser
driver.quit()
