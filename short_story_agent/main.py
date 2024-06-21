from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import StoryTasks
from agents import StoryAgents

tasks = StoryTasks()
agents = StoryAgents()

print("## Welcome to the Story Crew")
print('-------------------------------')
story = input("What is the Story you would like to build?\n")

# Create Agents
writer = agents.Writer()
editor = agents.Editor()
illustrator = agents.Illustrator()
educational_consultant = agents.Educational_Consultant()
psychologist = agents.Psychologist()
librarian = agents.Librarian()
teacher = agents.Teacher()


# Create Tasks
writer_task = tasks.Writer_task(writer, story)
editor_task = tasks.Editor_task(editor, story)
illustrator_task = tasks.Illustrator_task(illustrator, story)
educational_Consultant_task = tasks.Educational_Consultant_task(educational_consultant, story)
psychologist_task = tasks.Psychologist_task(psychologist, story)
librarian_task = tasks.Librarian_task(librarian, story)
teacher_task = tasks.Teacher_task(teacher, story)


# Create Crew responsible for Copy
crew = Crew(
	agents=[
		writer,
		editor,
		illustrator,
		educational_consultant,
		psychologist,
		librarian,
		teacher,
	],
	tasks=[
		writer_task,
		editor_task,
		illustrator_task,
		educational_Consultant_task,
		psychologist_task,
		librarian_task,
		teacher_task,
	],
	verbose=True
)

story = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the story:")
print(story)
