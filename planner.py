from time import strftime
import sqlite3



conn = sqlite3.connect('events.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS eventsToPlot(event_name TEXT, datestamp TEXT, event_description TEXT)')

#user_first_name = raw_input("What is your first name?")

create_table()
def welcome():
  #"Welcome,  " + user_first_name + "."
  print "Calendar starting..."
  print "Today is: " + strftime("%A %B %d, %Y")
  print "The time is: " + 	strftime("%I:%M:%S")
  print "What would you like to do?"

def view_events():
	c.execute('SELECT * FROM eventsToPlot')
	for row in c.fetchall():
		print row

def run_planner():
	welcome()
	start = True
	user_choice = raw_input("Would you like to add, view, or delete an event? Or leave the Calendar?(A=add, V=view, D=delete, X=Exit)")
	user_choice = user_choice.upper()

	if user_choice == 'A':
		event = raw_input("What is your event?")
		date = raw_input("When is your event?")
		description = raw_input("What is happening during this event?")
		event_name = event
		datestamp = date
		event_description = description
		c.execute("INSERT INTO eventsToPlot (event_name, datestamp, event_description) VALUES (?,?,?)",
			(event, date, description))
		conn.commit()
		print "Your calendar now looks like this:"
		view_events()
	elif user_choice == 'V':
		view_events()
	elif user_choice == 'D':
		event_to_delete = raw_input("Which event would you like to delete?")
		c.execute("DELETE FROM eventsToPlot WHERE event_name=?", (event_to_delete,))
		conn.commit()
	elif user_choice == 'X':
		start = False
	else:
		print "Invalid command, program closing."
		start = False

	
run_planner()





c.close()
conn.close()


