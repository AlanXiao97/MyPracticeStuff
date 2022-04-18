import webbrowser
import pyautogui
import time

# these functions are recruited to locate button and space
def open_url():
	url="https://zoom.us/"
	webbrowser.open(url)

def locate_zoom_sign_in_button():
	time.sleep(1.0)
	sign_in_coordinate=pyautogui.locateCenterOnScreen('zoom_sign_in_button.png')
	return sign_in_coordinate

def locate_zoom_password_space(sign_in_coordinate):
	time.sleep(1.0)
	pyautogui.moveTo(sign_in_coordinate[0],sign_in_coordinate[1],0)
	time.sleep(0.5)
	pyautogui.click()
	time.sleep(1.0)
	password_space=pyautogui.locateCenterOnScreen('zoom_password_space.png')
	return password_space

# this function is used to type in login information in zoom.us using pyautogui
def to_login_zoom(user_id,password,password_space):
	pyautogui.typewrite(user_id)
	pyautogui.moveTo(password_space[0],password_space[1],0)
	time.sleep(0.5)
	pyautogui.click()
	time.sleep(1.0)
	pyautogui.typewrite(password)
	pyautogui.typewrite(['enter'])

# this function is used to log out the current accout
def sign_out_zoom():
	time.sleep(1.0)
	host_a_meeting=pyautogui.locateCenterOnScreen('host_a_meeting.png')
	pyautogui.moveTo(host_a_meeting[0],host_a_meeting[1],0)
	pyautogui.moveRel(100,-4,0)
	time.sleep(0.2)
	pyautogui.click()
	time.sleep(0.2)
	sign_out_button=pyautogui.locateCenterOnScreen('sign_out.png')
	pyautogui.moveTo(sign_out_button[0],sign_out_button[1],0)
	time.sleep(0.2)
	pyautogui.click()




open_url()
x=locate_zoom_sign_in_button()
y=locate_zoom_password_space(x)
to_login_zoom("sample@outlook.com","password",y)
sign_out_zoom()
